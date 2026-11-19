# Kubernetes Roadmap (for an Agent / Backend Developer)

Goal: understand what happens to your code (e.g. `marketplace-api`) after you `git push`, well enough to
debug it, read its config, and talk to platform teams. This is **not** a "become a cluster admin" roadmap.

---

## 0. Your questions, answered first

### What is Kubernetes (K8s)?
**A system that runs and manages containers across a group of machines.**
You tell it *what you want* ("run 3 copies of this app, give each 1 CPU, expose port 8000"),
and it continuously works to make reality match that. It is software that runs on servers, not something you code in.

### Is it a language like bash? A framework like Spark?
Neither. Closest analogies:

| Thing | What it is | Kubernetes comparison |
|-------|-----------|-----------------------|
| bash / Python | Language to write logic | K8s is **not** this. You don't write logic in it. |
| Spark | Framework: you import it and call its API in your code | K8s is **not** this. Your code never imports Kubernetes. |
| Operating system / scheduler | Decides what runs where, restarts things | **This is closest.** K8s = "an operating system for a cluster of machines". |

So: it's a **platform + a concept (declarative infrastructure)**. You interact with it via:
1. **YAML files** (configuration, not programming): describe the desired state.
2. **`kubectl` CLI**: commands to inspect/apply that state (`kubectl get pods`, `kubectl logs ...`).
3. (Optional) Helm, Kustomize: templating tools over YAML.

Your agent logic (LangGraph, FastAPI...) is plain Python. K8s just *runs* it.

### Why can't we just run the same code on EC2?
**You can.** An EC2 instance is just a Linux VM; `python main.py` works. The question is what you must
then handle yourself:

| Problem | On plain EC2 | On Kubernetes |
|---------|-------------|---------------|
| App crashes at 3am | You write systemd/supervisor scripts, or wake up | Auto-restarted |
| Traffic grows | Launch more EC2s, set up load balancer by hand | Change `replicas: 3` -> `10` (or autoscale) |
| Deploy new version without downtime | Custom scripts, risky | Built-in rolling updates + rollback |
| Machine dies | App is gone until someone reacts | Pods rescheduled onto other machines |
| 50 services (API, UI, MCP...) | 50 hand-managed setups, "works on my machine" drift | One uniform way to run all of them |
| Secrets / config | Files on servers | Secrets/ConfigMaps injected uniformly |
| Packing machines efficiently | One app per VM, wasted capacity | Many apps share nodes, bin-packed |

For 1 small app, EC2 is fine and simpler. K8s pays off with **many services, many teams, need for
resilience and standardisation** - which is why Nike has a platform (NPE) for it.

### What is NPE then?
NPE is Nike's internal platform **on top of AWS EKS**. EKS = AWS-managed Kubernetes (AWS runs the control
plane for you). NPE adds Nike-specific stuff: login (`npectl`), Cerberus secrets, Istio networking,
CI/CD (Jenkins), namespaces/policies. You already saw traces of this in the repo:
`marketplace-api/python/Dockerfile` (container image) and `infrastructure/AutoJenkinsfile` (pipeline).

### Chain of events for your code
```
your Python code
   -> Dockerfile        (packages code + dependencies into an IMAGE)
   -> Jenkins pipeline  (builds image, pushes to a registry)
   -> K8s YAML / Helm   (says: run this image, N copies, these env vars, this port)
   -> EKS cluster       (runs it as Pods on EC2 worker nodes)
   -> Istio / Ingress   (routes user traffic to your Pods)
```
Note: EKS worker nodes **are EC2 machines**. K8s doesn't replace EC2; it manages a fleet of them for you.

---

## 1. Roadmap overview

| Phase | Topic | Time | Outcome |
|-------|-------|------|---------|
| 1 | Prerequisites: Linux, networking, YAML | 1 day | Comfortable with terminal, ports, env vars |
| 2 | Docker / containers | 2-3 days | Can containerize a FastAPI/LangGraph app |
| 3 | K8s core concepts | 3-4 days | Know Pod, Deployment, Service, etc. |
| 4 | Hands-on with local cluster | 3-4 days | Deploy your own app on `kind`/`minikube` |
| 5 | Config, secrets, storage, health | 2-3 days | Production-style app config |
| 6 | Debugging with kubectl | 2 days | Read logs, exec, diagnose crashes |
| 7 | Networking, Ingress, Istio basics | 2-3 days | Understand how traffic reaches your pod |
| 8 | Packaging & delivery: Helm, CI/CD | 2-3 days | Read Nike's deployment configs |
| 9 | Scaling & reliability | 2 days | HPA, resources, probes, rollouts |
| 10 | Real-world: EKS/NPE + Nike repo | 3 days | Trace `marketplace-api` end to end |
| 11 | Agent-specific topics | ongoing | LLM apps on K8s: timeouts, streaming, GPUs |

Total: ~3-4 weeks at 1-2 hrs/day. We'll do it interactively in Cursor with small hands-on exercises.

---

## 2. Phase details

### Phase 1 - Prerequisites
- Linux basics: processes, files, env vars, `ps`, `curl`, `ls`, `cat`, permissions
- Networking basics: IP, port, DNS, HTTP, localhost vs 0.0.0.0, load balancer, reverse proxy
- YAML syntax (lists, maps, indentation)
- Checkpoint: explain what `uvicorn app:app --host 0.0.0.0 --port 8000` does and why `0.0.0.0` matters.

### Phase 2 - Containers (Docker)
- Why containers: "works on my machine", isolation vs VMs
- Image vs container, Dockerfile, layers, multi-stage builds, registries
- Commands: `docker build`, `run`, `ps`, `logs`, `exec`, `push`
- Ports, env vars, volumes
- Exercise: read `products/nike-marketplace/python/marketplace-api/python/Dockerfile` line by line, then build
  and run a tiny LangGraph/FastAPI app in Docker.

### Phase 3 - Kubernetes core concepts (the heart)
Architecture:
- **Cluster** = Control plane (brain) + Worker nodes (EC2 machines that run your stuff)
- Control plane parts: API server, scheduler, controller manager, etcd
- Node parts: kubelet, container runtime, kube-proxy

Core objects (all defined in YAML):
| Object | One-line meaning |
|--------|------------------|
| Pod | Smallest unit; one or more containers running together |
| ReplicaSet | Keeps N identical pods alive |
| Deployment | Manages ReplicaSets; rolling updates, rollbacks. **You'll see this most.** |
| Service | Stable internal address/load balancer for a set of pods |
| Ingress / Gateway | Routes outside traffic to Services |
| Namespace | Logical folder to separate teams/apps |
| ConfigMap / Secret | Config and sensitive values injected into pods |
| Job / CronJob | Run-to-completion tasks / scheduled tasks |
| StatefulSet, DaemonSet | Special workloads (databases, per-node agents) |
| PersistentVolume(Claim) | Durable storage |

Key idea to internalise: **declarative desired state + reconciliation loop.**

### Phase 4 - Hands-on locally
- Install `kubectl` and `kind` (or minikube / Docker Desktop K8s)
- `kubectl get/describe/apply/delete`
- Write your first Pod, then Deployment, then Service YAML
- Exercise: deploy the hello-graph app (from `LangGraph/01_basics`) as a Deployment with 3 replicas;
  kill a pod and watch it come back; change image version and watch rolling update.

### Phase 5 - Config, secrets, storage, health
- Env vars, ConfigMap, Secret (and why Nike uses Cerberus instead of plain Secrets)
- Resource `requests` / `limits` (CPU, memory) and what OOMKilled means
- Probes: liveness, readiness, startup (why `/health` endpoints exist)
- Volumes basics

### Phase 6 - Debugging (most practical skill for you)
- `kubectl logs [-f] [--previous]`, `describe pod`, `exec -it`, `port-forward`, `get events`
- Pod states: Pending, CrashLoopBackOff, ImagePullBackOff, OOMKilled, Evicted
- Flow: "my API returns 500" -> which pod -> logs -> events -> resources
- Link to repo skill: `.cursor/skills/npe-kubectl-logs/`

### Phase 7 - Networking
- Pod IPs vs Service DNS (`svc.namespace.svc.cluster.local`)
- ClusterIP / NodePort / LoadBalancer
- Ingress controllers; service mesh and **Istio** (sidecar `istio-proxy`, VirtualService, Gateway)
- Why requests can time out before reaching your app (relevant for long LLM calls / streaming / SSE)

### Phase 8 - Packaging & delivery
- Helm: charts, `values.yaml`, templates (most Nike-style deployments are templated)
- Kustomize overview
- CI/CD: Jenkins -> build image -> push -> deploy; GitOps idea (ArgoCD/Flux)
- Terraform vs K8s YAML (infra vs app). See `marketplace-api/infrastructure/terraform`.

### Phase 9 - Scaling & reliability
- Manual scaling, HPA (autoscale on CPU/custom metrics)
- Rolling updates, rollbacks, PodDisruptionBudget
- Node autoscaling (Cluster Autoscaler / Karpenter on EKS)
- Graceful shutdown (SIGTERM) - matters for in-flight agent requests

### Phase 10 - Real world: EKS + NPE
- EKS architecture: managed control plane, EC2/Fargate nodes, IAM roles for service accounts (IRSA)
- What NPE adds: `npectl`, `runtime login`, Cerberus, Istio, namespaces, policies
- Capstone: trace `marketplace-api` from `Dockerfile` -> `AutoJenkinsfile` -> deployed pod -> logs -> route.
  Also compare `marketplace-ui` and the MCP server (Databricks Apps, a different runtime - good contrast).

### Phase 11 - Agent-specific topics
- Stateless services and where agent state/memory lives (Redis, DB, not pod memory)
- Long-running / streaming requests: timeouts at ingress, Istio, client
- Concurrency: workers per pod vs number of pods
- Secrets for LLM API keys, config per environment (dev/qa/prod)
- GPU workloads and model serving (awareness only)
- Observability: logs, metrics, tracing (MLflow traces, Datadog etc.)

---

## 3. Cheat sheet (will grow as we learn)

```bash
kubectl get pods -n <namespace>
kubectl describe pod <pod> -n <namespace>
kubectl logs <pod> -n <namespace> -f
kubectl exec -it <pod> -n <namespace> -- /bin/sh
kubectl get deployments,svc,ingress -n <namespace>
kubectl apply -f file.yaml
kubectl rollout status deployment/<name>
kubectl rollout undo deployment/<name>
kubectl port-forward svc/<name> 8000:8000
```

A minimal Deployment, just to show it's config, not code:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-agent-api
spec:
  replicas: 3                    # "I want 3 copies running"
  selector:
    matchLabels: { app: my-agent-api }
  template:
    metadata:
      labels: { app: my-agent-api }
    spec:
      containers:
        - name: api
          image: my-registry/my-agent-api:1.0.0   # built from your Dockerfile
          ports:
            - containerPort: 8000
          resources:
            requests: { cpu: "500m", memory: "512Mi" }
            limits:   { memory: "1Gi" }
```

---

## 4. How we'll learn (in Cursor)

1. One phase at a time; I explain with analogies, using your own repo as examples.
2. Each phase ends with a small hands-on exercise and a checkpoint question.
3. We keep notes per phase in this folder (`01-containers.md`, `02-core-concepts.md`, ...).
4. Capstone: explain `marketplace-api` deployment end to end, in your own words.

**Next step:** say "Start Phase 1" (or jump to Phase 2 if you already know Docker).
