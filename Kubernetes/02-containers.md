# Phase 2 - Containers (Docker)

## Why this phase exists
Kubernetes does not run your Python code directly. It runs **container images**. If you understand
images, containers, and the Dockerfile, then a K8s Deployment is just "run this image N times".

```
Your code + dependencies -> Dockerfile -> IMAGE -> pushed to REGISTRY -> run as CONTAINER(s)
       (Part A)               (Part B)     (Part B)     (Part C)           (Part C)
```

---

## Part A - Why containers

### A1. The problem: "works on my machine"
Your laptop has Python 3.11, a specific `pip` set, certain env vars. The server has Python 3.8 and
different libraries. The same code behaves differently. A container packages the **app + its
dependencies + its runtime** into one unit that behaves the same everywhere.

### A2. What a container really is
A container is **a normal Linux process** (recall Phase 1, A3) that is **isolated**:
- its own filesystem view (it only sees files from its image)
- its own process list (it thinks it is PID 1)
- its own network namespace (its own `localhost`, own IP, own ports)
- optional CPU/memory limits

It is **not** a mini computer. It shares the host's Linux kernel.

### A3. Containers vs Virtual Machines
| | VM (e.g. EC2) | Container |
|---|---------------|-----------|
| Includes | Full OS + kernel | App + libs only (shares host kernel) |
| Size | GBs | MBs to a few hundred MB |
| Start time | Minutes | Seconds or less |
| Isolation | Strong (hardware-level) | Lighter (OS-level) |
| Density | A few per host | Dozens per host |

Why it matters: K8s packs many containers onto each EC2 worker node, which is why it is efficient.

### A4. Key lifecycle rule (from Phase 1)
A container lives **only as long as its main process**. If `uvicorn` exits, the container stops. Hence
the main process must run in the **foreground** (no daemonizing).

---

## Part B - Image, Dockerfile, layers

### B1. Image vs container
| Term | Meaning | Analogy |
|------|---------|---------|
| **Image** | Read-only template: filesystem + startup command | Class / recipe / installer |
| **Container** | A running instance of an image | Object / the cooked dish / running app |

One image can start many containers (that is what `replicas: 3` does).

### B2. Dockerfile
A text file of instructions to build an image, step by step.

| Instruction | Meaning |
|-------------|---------|
| `FROM python:3.10-slim` | Start from a base image (OS + Python) |
| `WORKDIR /app` | Set the working directory (like `cd /app`) |
| `COPY src/ ./src/` | Copy files from your machine into the image |
| `RUN pip install -r requirements.txt` | Run a command at **build time** |
| `ENV KEY=value` | Set an environment variable |
| `EXPOSE 8000` | Documents the port the app uses (does not publish it by itself) |
| `USER appuser` | Run as non-root user |
| `CMD [...]` | The command to run at **container start** (the main process) |
| `HEALTHCHECK` | How to test the container is healthy |

`RUN` = happens once while building. `CMD` = happens every time a container starts.

### B3. Layers and caching
Each instruction creates a **layer**. Docker caches layers; if nothing changed up to a step, it reuses
the cache. So order matters:
```dockerfile
COPY requirements.txt .        # changes rarely
RUN pip install -r requirements.txt   # cached unless requirements change
COPY src/ ./src/               # changes often, placed LAST
```
Putting `COPY src/` before `pip install` would reinstall dependencies on every code change (slow builds).

### B4. Multi-stage builds
Use one stage to build (compilers like `gcc`), and copy only the results into a clean final stage.
Result: a smaller, safer production image. The marketplace-api Dockerfile does exactly this:
- Stage 1 `builder`: installs `gcc`, runs `pip install`
- Stage 2: fresh `python:3.10-slim`, copies only installed packages with `COPY --from=builder`

### B5. `.dockerignore`
Lists files that should not be sent into the build (`.git`, `.venv`, `__pycache__`, secrets). Like
`.gitignore` for Docker.

---

## Part C - Registries, commands, runtime config

### C1. Registry
A server that stores images (Docker Hub, AWS ECR, Artifactory). Image name format:
```
registry.example.com/team/my-agent-api:1.0.0
|------ registry ----|--- repo ------|-- tag
```
- **Tag** = a version label (`1.0.0`, `latest`). Avoid `latest` in production: it is ambiguous.
- Jenkins builds the image and pushes it to the registry; K8s pulls it from there
  (a failure to pull = `ImagePullBackOff`, Phase 6).

### C2. Essential commands
| Command | Meaning |
|---------|---------|
| `docker build -t my-api:1.0 .` | Build an image from the Dockerfile in `.` |
| `docker images` | List local images |
| `docker run -p 8000:8000 my-api:1.0` | Start a container, map host:container port |
| `docker run -d --name api ...` | Run in background (detached) with a name |
| `docker ps` / `docker ps -a` | List running / all containers |
| `docker logs -f api` | Follow logs (stdout/stderr) |
| `docker exec -it api /bin/sh` | Open a shell inside a running container |
| `docker stop api` / `docker rm api` | Stop (SIGTERM, then SIGKILL) / remove |
| `docker push registry/my-api:1.0` | Upload image to registry |

Note how closely these map to K8s: `docker logs` -> `kubectl logs`, `docker exec` -> `kubectl exec`.

### C3. Ports
`-p 8000:8000` = `host_port:container_port`. The container's port is invisible from outside unless
published. And the app **must bind `0.0.0.0`** inside the container (Phase 1, B3), otherwise
`-p` forwarding reaches nothing.

### C4. Environment variables
```bash
docker run -e LLM_MODEL=gpt-4o -e LOG_LEVEL=info my-api:1.0
docker run --env-file .env my-api:1.0
```
Never bake secrets into the image (anyone with the image can read them). Inject at runtime.

### C5. Volumes
A container's filesystem is **ephemeral**: deleted when the container is removed. A **volume** mounts
persistent storage or a host folder into the container.
```bash
docker run -v $(pwd)/data:/app/data my-api:1.0
```
In K8s this becomes PersistentVolumes / ConfigMap mounts (Phase 5). For agents: do not keep state in
the container filesystem.

---

## Part D - Reading the real marketplace-api Dockerfile
File: `products/nike-marketplace/python/marketplace-api/python/Dockerfile`

| Lines / instruction | What it does | Concept |
|---------------------|--------------|---------|
| `FROM python:3.10-slim as builder` | Stage 1 base | Multi-stage |
| `apt-get install gcc g++` | Compilers to build Python wheels | Build-only deps |
| `COPY requirements.txt` then `pip install` | Deps layer before code | Layer caching |
| `pip install --user` | Installs into `/root/.local` so it is easy to copy out | Multi-stage handoff |
| `FROM python:3.10-slim` | Clean Stage 2 | Small image |
| `useradd -m -u 1000 appuser` / `USER appuser` | Non-root | Security (Phase 1, A5) |
| `COPY --from=builder --chown=...` | Copy packages from Stage 1 | Multi-stage |
| `COPY src/`, `alembic/` | App code and DB migrations | App layer |
| `ENV PYTHONUNBUFFERED=1` | Logs appear immediately in stdout | `kubectl logs` |
| `ENV PYTHONPATH=/app/src` | Python import path | Env vars |
| `HEALTHCHECK ... /health` | Container health test | Probes (Phase 5) |
| `EXPOSE 8000` | Documents port | Ports |
| `CMD ["opentelemetry-instrument", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]` | The main process | `0.0.0.0`, foreground process |

---

## Part E - Template: Dockerfile for a small FastAPI / LangGraph app
```dockerfile
FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Checkpoint (answer in your own words)
1. What is the difference between an image and a container?
2. How is a container different from a VM?
3. What is the difference between `RUN` and `CMD`?
4. Why is `COPY requirements.txt` + `pip install` placed before `COPY src/`?
5. Why use a multi-stage build?
6. You run `docker run my-api` and `curl localhost:8000` fails, though the logs show the app started.
   Give two likely causes. (Hint: `-p`, `--host`.)
7. Why must you never store chat history/agent memory only in the container filesystem?
8. What happens to a container if its main process exits?

## Hands-on exercises (about 2-3 days at 1-2 hrs/day)
1. Install Docker Desktop (or Colima); run `docker run hello-world` and `docker run -it python:3.11-slim python`.
2. Write a tiny FastAPI app (`main.py` with `/health`), plus `requirements.txt`.
3. Write the Dockerfile from Part E; `docker build -t hello-api:1.0 .`
4. `docker run -p 8000:8000 hello-api:1.0`; test with `curl -i localhost:8000/health`.
5. Break it on purpose: change CMD to `--host 127.0.0.1`, rebuild and see `curl` fail. Fix it.
6. Run detached with `-d --name api`; use `docker logs -f`, `docker exec -it api /bin/sh`
   (try `ps aux`, `env`, `ls /app`), and `docker stop api`.
7. Pass an env var with `-e` and print it from the app.
8. Reorder `COPY` and `RUN pip install`; rebuild after a code change and compare build times.
9. Read the marketplace-api Dockerfile using the Part D table; mark every concept.
10. (Optional) Convert your Dockerfile to multi-stage and compare image sizes with `docker images`.
