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

| Phase | Topic | Outcome |
|-------|-------|---------|
| 1 | Prerequisites: Linux, networking, YAML | Comfortable with terminal, ports, env vars |
| 2 | Docker / containers | Can containerize a FastAPI/LangGraph app |
| 3 | K8s core concepts | Know Pod, Deployment, Service, etc. |
| 4 | Hands-on with local cluster | Deploy your own app on `kind`/`minikube` |
| 5 | Config, secrets, storage, health | Production-style app config |
| 6 | Debugging with kubectl | Read logs, exec, diagnose crashes |
| 7 | Networking, Ingress, Istio basics | Understand how traffic reaches your pod |
| 8 | Packaging & delivery: Helm, CI/CD | Read Nike's deployment configs |
| 9 | Scaling & reliability | HPA, resources, probes, rollouts |
| 10 | Real-world: EKS/NPE + Nike repo | Trace `marketplace-api` end to end |
| 11 | Agent-specific topics | LLM apps on K8s: timeouts, streaming, GPUs |

Total: ~3-4 weeks at 1-2 hrs/day. We'll do it interactively in Cursor with small hands-on exercises.

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
