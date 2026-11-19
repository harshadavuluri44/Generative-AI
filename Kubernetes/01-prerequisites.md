# Phase 1 - Prerequisites: Linux, Networking, YAML

## Why this phase exists
Kubernetes runs your app as a **container**, and a container is a **Linux process**. Everything you do
with K8s (logs, exec, env vars, ports, config files) is Linux + networking + YAML. If these three are
fuzzy, K8s feels like magic. If they are clear, K8s feels like "the same thing, automated".

```
Your Python code -> runs as a Linux process -> listens on a network port -> configured with YAML
                    (Part A)                   (Part B)                      (Part C)
```

---

## Part A - Linux basics

### What is Linux, and why does it matter?
Linux is an operating system (like macOS/Windows). Servers (EC2 machines, EKS nodes, containers)
almost all run Linux. Your Mac is Unix-based, so the commands are nearly identical.
When you `kubectl exec` into a pod you land in a **Linux shell**.

### A1. The terminal and shell
- **Terminal** = the window. **Shell** (bash/zsh) = the program that reads your commands.
- Servers have no GUI; the shell is the only interface.

### A2. Files and directories
| Command | Meaning |
|---------|---------|
| `pwd` | where am I |
| `ls -la` | list files (incl. hidden, permissions) |
| `cd <dir>` | change directory |
| `cat file` | print a file |
| `mkdir`, `rm`, `cp`, `mv` | create / delete / copy / move |

Why it matters: in a container, your code lives at a path like `/app` (see `WORKDIR /app` in the
marketplace-api Dockerfile). Config files get mounted at paths like `/etc/config/...`.

### A3. Processes
- A **process** = a running program. Your `uvicorn` server is one process, with a **PID** (id number).
- `ps aux` lists processes, `kill <pid>` stops one.
- **Signals**: how the OS tells a process to stop.
  - `SIGTERM` = "please shut down gracefully"
  - `SIGKILL` = "die now" (cannot be handled)
- **Exit code**: `0` = success, non-zero = failure. `echo $?` shows the last one.

Why it matters: K8s stops a pod by sending SIGTERM, waits (default 30s), then SIGKILL. Exit code `137`
means killed (often out-of-memory). A container lives **only as long as its main process lives**: if
the process exits, the container is considered finished, and K8s restarts it (CrashLoopBackOff!).

### A4. Environment variables
Key-value settings given to a process from outside the code.
```bash
export LLM_MODEL=gpt-4o
echo $LLM_MODEL
```
```python
import os
os.getenv("LLM_MODEL")
```
Why it matters: same code runs in dev/qa/prod, only env vars differ. K8s injects env vars into pods.
This is how your agents get API URLs, feature flags, etc.

### A5. Permissions and users
- `ls -l` shows `-rwxr-xr--`: read/write/execute for owner, group, others.
- `root` = all-powerful user. Good practice: run apps as non-root (see `useradd ... appuser` in the
  Dockerfile). K8s clusters often block root containers.

### A6. Pipes, redirects, logs
- `cmd1 | cmd2` sends output of one into the next. `cmd > file` writes to a file.
- `grep ERROR`, `tail -f` (follow a log live).
- **Containers log to stdout/stderr**, not files. `kubectl logs` just reads that stream. So `print()` and
  `logging` to console is what you see.

### A7. Package managers & scripts (light)
`pip install`, `apt-get install`, and shell scripts (`.sh`, e.g. `start_local.sh`). The Dockerfile uses these.

---

## Part B - Networking basics

### B1. IP address
A machine's address on a network, e.g. `10.0.3.17`. In K8s every **pod gets its own IP** (and it changes
when the pod is replaced - why `Service` exists later).

### B2. Port
An IP finds the machine; a **port** finds the program on it. `10.0.3.17:8000` = "the program listening on
8000". Common: 80 HTTP, 443 HTTPS, 5432 Postgres, 8000 FastAPI default.

### B3. localhost vs 0.0.0.0 (very common bug)
| Address | Meaning |
|---------|---------|
| `127.0.0.1` / `localhost` | "this machine only". Nobody outside can connect. |
| `0.0.0.0` | "listen on all network interfaces". Reachable from outside. |

If your app binds to `127.0.0.1` inside a container, traffic from other pods/the load balancer **can't
reach it** even though the app is running. Hence `uvicorn --host 0.0.0.0`.

### B4. DNS
Turns names into IPs: `google.com` -> `142.250.x.x`. In K8s, services get internal DNS names, e.g.
`marketplace-api.my-namespace.svc.cluster.local`, so apps call each other by name, not IP.

### B5. HTTP basics
Request = method (GET/POST) + URL + headers + body. Response = status code + body.
- `2xx` ok, `4xx` client error (401 unauthorized, 404 not found), `5xx` server error (500, 502, 503, 504).
- `curl` is the tool to test: `curl -i http://localhost:8000/health`
- Streaming/SSE (what your chat agent likely uses) = a response that stays open and sends chunks.

### B6. Reverse proxy and load balancer
- **Reverse proxy**: sits in front of your app, forwards requests (e.g. nginx, Istio/Envoy).
- **Load balancer**: spreads requests across several copies of your app.
```
User -> Load balancer -> [ app copy 1 | app copy 2 | app copy 3 ]
```
This is what K8s Service + Ingress do for you. `istio-proxy` in your NPE logs is a reverse proxy.
504/502 errors often come from a proxy, not your code.

### B7. Firewall / security groups (awareness)
Rules saying who can talk to which port. Cloud equivalent: AWS Security Groups. If "it works locally but
not deployed", this (or binding address) is a frequent culprit.

---

## Part C - YAML

### What is it?
A plain text format for configuration (not a programming language). K8s resources are all YAML.

### Rules
- **Indentation = structure** (spaces only, never tabs; usually 2).
- **Map**: `key: value`
- **List**: lines starting with `- `
- Comments with `#`. Strings usually need no quotes, but quote things like `"8000"` or `"true"` when needed.

```yaml
name: my-agent
replicas: 3
env:                    # map
  LLM_MODEL: gpt-4o
  LOG_LEVEL: info
ports:                  # list
  - 8000
  - 9090
containers:             # list of maps
  - name: api
    image: my-api:1.0
  - name: sidecar
    image: proxy:2.1
```

Same data as JSON, but friendlier. You can see real YAML in this repo:
`products/nike-compass-ai/marketplace-mcp/mcp_server/nim_mcp_server/app.yaml`.

Common mistakes: wrong indentation, tabs, forgetting `- ` in lists, number vs string.

---

## Checkpoint (answer in your own words)
Explain `uvicorn app:app --host 0.0.0.0 --port 8000`:
- What process does it start?
- What does `--host 0.0.0.0` do and what breaks if it's `127.0.0.1` in a container?
- What does `--port 8000` mean for someone who wants to call it?
- How would you verify it works? (`curl ...`)
- If the process crashes, what does K8s do?

## Hands-on exercises (about 45 min)
1. `pwd`, `ls -la`, `cd` through your Generative-AI folder.
2. `export GREETING=hello`; run `python3 -c "import os; print(os.getenv('GREETING'))"`.
3. Start a server: `python3 -m http.server 8000`; in another terminal `curl -i localhost:8000`; then
   `lsof -i :8000` to see the process and PID; stop it with Ctrl+C (that's a SIGINT/SIGTERM-like signal).
4. Run it bound to localhost only vs all: `python3 -m http.server 8000 --bind 127.0.0.1` vs `--bind 0.0.0.0`.
5. Write a small YAML file with a map, list, and list of maps; load it with Python
   (`import yaml; print(yaml.safe_load(open("x.yaml")))`) and compare with JSON.
6. Open the marketplace-api `Dockerfile` and `app.yaml`; highlight every Linux/network/YAML concept above.
