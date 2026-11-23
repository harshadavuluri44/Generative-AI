# Phase 3 - Kubernetes Core Concepts

You already know how code becomes an image (Phase 2). An image just sits in a registry until
something runs it. Running one container on one machine is easy (`docker run`). Running **dozens of
services, each with several copies, across many machines, and keeping them alive** is the hard part.
Kubernetes (K8s) is the software that does that job.

This file builds the picture from scratch, in this order:

1. The big picture, using an everyday analogy
2. The machines: what a cluster is and what runs on it
3. The people (components) inside the cluster and what each one does
4. The objects you describe in YAML: Pod, ReplicaSet, Deployment, Service, and so on
5. The one idea that ties everything together
6. A complete story from `kubectl apply` to a running app

---

## 1. The big picture: a restaurant analogy

Think of a large restaurant chain.

| Restaurant | Kubernetes |
|------------|------------|
| The restaurant's whole operation | **Cluster** |
| Management office | **Control plane** |
| Kitchens in different buildings | **Worker nodes** (EC2 machines) |
| A recipe | **Image** |
| A cook preparing one dish from a recipe | **Container** |
| A cooking station (one or more cooks working together) | **Pod** |
| The order slip: "Make 3 portions of dish X" | **Deployment YAML** |
| The manager who reads the order slip | **Controllers** |
| The person who decides which kitchen gets which order | **Scheduler** |
| The kitchen supervisor in each building | **kubelet** |
| The waiter's counter with one fixed phone number | **Service** |
| The front door where customers enter | **Ingress / Gateway** |

You (the developer) never go into a kitchen and cook. You hand the **order slip** (YAML) to the
management office, and the office makes sure the right number of dishes is always being cooked, even if a
cook faints or a kitchen burns down. That is the core of Kubernetes.

---

## 2. The machines: what a cluster is

A **cluster** is a group of machines that work together, managed as one unit. It has two kinds of
machines.

```
                         CLUSTER
 ┌────────────────────────────────────────────────────┐
 │  CONTROL PLANE  (decides)                          │
 │  API server | etcd | scheduler | controller manager│
 └───────────────▲────────────────────────────────────┘
                 │  instructions down, status reports up
   ┌─────────────┼───────────────┬───────────────┐
   │             │               │               │
 ┌─▼───────────┐ ┌▼────────────┐ ┌▼────────────┐
 │ WORKER NODE │ │ WORKER NODE │ │ WORKER NODE │   (do the work)
 │ kubelet     │ │ kubelet     │ │ kubelet     │
 │ containerd  │ │ containerd  │ │ containerd  │
 │ [pod] [pod] │ │ [pod]       │ │ [pod] [pod] │
 └─────────────┘ └─────────────┘ └─────────────┘
```

- **Worker node**: a normal Linux machine (on AWS EKS, an EC2 instance). Its only job is to run pods.
  Your app's containers live here.
- **Control plane**: the machines that run the cluster's "management software". It never runs your app. It
  decides *what* should run and *where*. On EKS, AWS runs and maintains it for you, so you never log
  into it.

You talk to the cluster only through the control plane's front door (the API server). You do not SSH
into worker nodes to start things.

---

## 3. The components inside the cluster, and who does what

Everything below is just **software running as processes**. Nothing here is magic; each has one
clear job.

### 3.1 Control plane components

**API server** - the front door and the only entry point
- *What*: a web server that accepts requests like "create this Deployment", "list pods", "delete this pod".
- *Who talks to it*: `kubectl`, Helm, Jenkins, and also every other component in the cluster
  (the scheduler, controllers and kubelets all talk to it; they never talk to each other directly).
- *How it works*: it checks that you are allowed to do the request (authentication and permissions) and
  that the YAML is valid, then saves it.

**etcd** - the database
- *What*: a small, reliable key-value database holding the cluster's state: every Deployment, pod,
  Service, Secret, and so on.
- *Who talks to it*: only the API server. Others read and write state by asking the API server.
- *How to think of it*: the filing cabinet that holds the "order slips" and the current status of every
  order.

**Scheduler** - decides which node runs each new pod
- *What*: a loop that looks for pods that have been created but have no node yet.
- *How it decides*: it compares what the pod asks for (CPU and memory `requests`, any placement rules)
  against the free capacity on each node, filters out nodes that don't fit, and picks the best of the rest.
- *What it does not do*: it does **not** start the container. It only writes "this pod belongs on node 2"
  through the API server.

**Controller manager** - the supervisors that keep reality matching your YAML
- *What*: a bundle of many small loops, each called a **controller**. There is a Deployment controller,
  a ReplicaSet controller, a Node controller, a Job controller, and so on.
- *How it works*: each controller repeatedly compares **desired state** (what the YAML says) with
  **actual state** (what exists), and takes action to close the gap, such as creating or deleting pods.
  (More in section 5.)

### 3.2 Worker node components

**kubelet** - the supervisor on each node
- *What*: an agent (a Linux service) running on every worker node.
- *How it works*: it keeps asking the API server "which pods are assigned to my node?". When it sees a
  new one, it tells the container runtime to start that pod's containers. It then keeps watching them:
  restarts crashed containers, runs health probes, and reports status back to the API server.
- *Scope*: it only manages pods on **its own node**.

**Container runtime (containerd)** - the thing that really runs containers
- *What*: software that pulls images from the registry and starts/stops containers on the node.
- *Who tells it what to do*: the kubelet. This is the "`docker run` equivalent" from Phase 2. Most EKS
  nodes use `containerd` directly rather than the `docker` command.

**kube-proxy** - local network plumbing
- *What*: sets up network rules on the node so traffic sent to a Service address reaches one of the
  right pods. (Details in Phase 7.)

### 3.3 Who does what: summary

| Component | Lives on | Job in one sentence | Talks to |
|-----------|----------|---------------------|----------|
| API server | Control plane | Receives and validates all requests; the single front door | Everyone |
| etcd | Control plane | Stores all cluster state | API server only |
| Scheduler | Control plane | Chooses a node for each unplaced pod | API server |
| Controller manager | Control plane | Creates/deletes objects to match your YAML | API server |
| kubelet | Each worker node | Makes the node's assigned pods actually run and healthy | API server, containerd |
| containerd | Each worker node | Pulls images; starts and stops containers | kubelet, registry |
| kube-proxy | Each worker node | Routes Service traffic to pods | API server |

---

## 4. The objects: what you describe in YAML

In Kubernetes, everything you want is described as an **object** in a YAML file. You submit the file
with `kubectl apply -f file.yaml`; the API server stores it; the components from section 3 then make it real.

Every object has the same four top-level parts:

```yaml
apiVersion: apps/v1       # which version of the K8s API defines this type
kind: Deployment          # the TYPE of object you want
metadata:                 # identity: name, namespace, labels
  name: my-agent-api
spec:                     # the DESIRED state: what you want (you write this)
  ...
# status:                 # the ACTUAL state (K8s writes this, you never do)
```

The most important idea: **`spec` is what you want; `status` is what K8s sees.** K8s works to make
`status` equal `spec`.

Below, the objects are presented in the order they build on each other.

### 4.1 Pod - the smallest thing K8s runs

**What it is**: a wrapper around **one or more containers** that always run together on the same node.

**What the containers in one pod share**:
- the same network: one IP address, and they reach each other via `localhost`
- optionally the same storage volumes

**Usually**: one pod = one main container (your app). Sometimes extra helper containers called
**sidecars** run alongside, for example `istio-proxy` in your NPE logs is a sidecar injected next to your app.

**Important behaviour**:
- Pods are **disposable**. If a pod dies it is not repaired; a **new pod with a new name and new IP**
  replaces it.
- That is why you should never depend on a pod's IP or on anything stored inside a pod.

**Who creates pods**: you rarely do. A higher-level object (Deployment, Job...) creates them for you.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hello
spec:
  containers:
    - name: api
      image: my-registry/hello-api:1.0      # the image from Phase 2
      ports:
        - containerPort: 8000
```

If you apply only this, K8s runs one pod. If it dies, **nothing brings it back**, because nobody is
watching it. That limitation is why the next two objects exist.

### 4.2 ReplicaSet - keeps a fixed number of identical pods alive

**What it is**: an object saying "there must always be exactly N pods that look like this template".

**How it works** (done by the ReplicaSet controller):
1. It counts the pods that match its label selector.
2. Too few? It creates pods. Too many? It deletes pods.
3. It repeats this forever.

So if a pod is deleted or its node dies, the ReplicaSet notices the count dropped and creates a replacement.
You will rarely write a ReplicaSet yourself; a Deployment creates and manages them.

### 4.3 Deployment - what you will write and see most

**What it is**: an object that manages ReplicaSets so you get **zero-downtime updates and rollbacks**.

**How it works**: when you update the image version in the YAML and re-apply:
1. The Deployment controller creates a **new ReplicaSet** for the new version.
2. It gradually scales the new ReplicaSet **up** (new pods start) while scaling the old one **down**
   (old pods stop). At every moment some pods are serving traffic. This is a **rolling update**.
3. The old ReplicaSet is kept, scaled to 0, so a rollback (`kubectl rollout undo`) is just scaling it back up.

```
Deployment: my-agent-api  (replicas: 3, image 1.0.1)
  ├── ReplicaSet (image 1.0.0)  -> 0 pods   (kept for rollback)
  └── ReplicaSet (image 1.0.1)  -> 3 pods
         ├── Pod  my-agent-api-7d9f8c6b5-x2k4p   -> Container
         ├── Pod  my-agent-api-7d9f8c6b5-m8q2z   -> Container
         └── Pod  my-agent-api-7d9f8c6b5-r5tv9   -> Container
```

**Reading a pod name**: `my-agent-api-7d9f8c6b5-x2k4p` = `<Deployment name>-<ReplicaSet hash>-<random pod id>`.
When you see this in `kubectl get pods` you can tell which Deployment and which version it came from.

**The chain to remember**: **Deployment -> ReplicaSet -> Pods -> Containers**

### 4.4 Labels and selectors - how objects find each other

K8s objects don't hold direct references to each other. They find each other by **labels**.

- **Label**: a key/value tag you attach to an object, such as `app: my-agent-api`.
- **Selector**: a rule that says "pick all objects that have this label".

```yaml
# Deployment: "I manage pods labelled app=my-agent-api"
spec:
  replicas: 3
  selector:
    matchLabels: { app: my-agent-api }
  template:                          # the blueprint for each pod
    metadata:
      labels: { app: my-agent-api }  # every pod created gets this label
    spec:
      containers:
        - name: api
          image: my-registry/my-agent-api:1.0.0
```

The Deployment's `selector` must match the pod template's `labels`; otherwise the Deployment would
create pods and then not recognise them as its own. A Service (next) uses the same mechanism, so a
label mismatch there means the Service sends traffic to nothing. This is one of the most common beginner bugs.

### 4.5 Service - a stable address in front of changing pods

**The problem**: pods are disposable and every new pod has a new IP. If another app stored a pod's IP,
it would break the next time that pod is replaced. With 3 replicas, which one should it call?

**What a Service is**: an object that gets a **fixed IP and a fixed DNS name**, and forwards traffic
to whichever pods currently match its label selector and are **Ready**.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-agent-api
spec:
  selector: { app: my-agent-api }     # forward to pods with this label
  ports:
    - port: 80                        # the port callers use on the Service
      targetPort: 8000                # the port your container listens on
```

**How a request flows**:
```
Another pod calls  http://my-agent-api
   -> cluster DNS resolves the name to the Service's fixed IP
   -> kube-proxy rules on the node pick one of the healthy pods
   -> request reaches that pod's port 8000
```

**Who keeps the list of pods current**: K8s automatically updates the Service's list of pod IPs as pods
come and go. A pod only gets traffic once its readiness probe passes (Phase 5).

**Types of Service**:
| Type | Reachable from | Typical use |
|------|----------------|-------------|
| **ClusterIP** (default) | Inside the cluster only | Service-to-service calls |
| NodePort | A port opened on every node | Testing |
| LoadBalancer | A cloud load balancer (AWS) | Direct external exposure |

### 4.6 Ingress / Gateway - letting outside traffic in

A ClusterIP Service is only reachable inside the cluster. Users on the internet need a way in.
**Ingress** (or, in Istio setups, a **Gateway** plus **VirtualService**) is a set of routing rules,
such as "requests for `api.example.com/chat` go to Service `my-agent-api`". A controller (nginx, Istio
ingress gateway, AWS load balancer controller) reads those rules and does the actual routing.

```
User -> Ingress / Gateway -> Service -> Pod -> Container
```

### 4.7 Namespace - folders inside the cluster

A cluster is shared by many teams and environments. A **Namespace** groups objects so names don't clash and
access can be limited per team. `my-agent-api` in namespace `dev` and `my-agent-api` in `qa` are two
separate objects. Most `kubectl` commands apply to **one namespace at a time**, which is why you
always add `-n <namespace>`.

### 4.8 ConfigMap and Secret - config outside the image

You should not bake settings into an image (it must be the same image in dev, qa and prod).

| Object | Holds | Example |
|--------|-------|---------|
| **ConfigMap** | Non-sensitive settings | `LOG_LEVEL=info`, an API base URL |
| **Secret** | Sensitive values | API keys, DB passwords (base64-encoded, not encrypted by default) |

**How they reach your app**: when the kubelet starts the container, it injects the values as **environment
variables** or **mounted files**. Your code just calls `os.getenv(...)`, the same as in Phase 1.
(Nike uses Cerberus for secrets; see Phase 5.)

### 4.9 Job and CronJob - tasks that finish

A Deployment's pods are expected to run forever. Some work should run once and stop.
- **Job**: runs a pod until its process exits with code `0` (success), retrying on failure. Example: a database migration.
- **CronJob**: creates Jobs on a schedule, like Linux `cron`.

### 4.10 StatefulSet, DaemonSet, and storage (awareness only)

| Object | What it does | Example |
|--------|--------------|---------|
| **StatefulSet** | Pods with stable names (`db-0`, `db-1`) and their own disk | Databases |
| **DaemonSet** | Exactly one pod on every node | Log collectors, monitoring agents |
| **PersistentVolumeClaim (PVC)** | A request for durable storage | "I need 10 GB" |
| **PersistentVolume (PV)** | The actual disk that satisfies it | An AWS EBS volume |

A container's own filesystem disappears with the container, so durable data needs a volume. For agent apps,
the usual answer is: **keep state in an external database or Redis, not in the pod.**

### 4.11 All objects at a glance

| Object | Meaning | Created by | You will see it when... |
|--------|---------|------------|-------------------------|
| Pod | Containers running together on one node | Deployment / Job | Reading logs, `kubectl exec` |
| ReplicaSet | Keeps N identical pods alive | Deployment | The hash in pod names |
| Deployment | Rolling updates and rollbacks | You (YAML/Helm) | Almost every service |
| Service | Stable address + load balancing | You | Service-to-service calls |
| Ingress/Gateway | Routes outside traffic in | You / platform | Exposing an API or UI |
| Namespace | Folder to separate teams/apps | Platform team | Every `kubectl -n` |
| ConfigMap/Secret | Config and sensitive values | You / platform | Env vars, API keys |
| Job/CronJob | Run-to-completion / scheduled | You | Migrations, batch tasks |
| StatefulSet/DaemonSet | Special workloads | Platform | Databases, node agents |
| PV/PVC | Durable storage | You / platform | Stateful apps |

---

## 5. The idea behind everything: desired state and the reconciliation loop

### 5.1 Two ways to give instructions

| Style | You tell the system | Example |
|-------|---------------------|---------|
| **Imperative** (how) | Each step to take | `docker run` three times, then another if one crashes |
| **Declarative** (what) | The end result you want | "3 replicas of image X" in YAML |

Kubernetes is **declarative**. You write the final state in YAML and submit it. K8s works out the steps.

### 5.2 The reconciliation loop

Every controller runs this loop forever:

```
repeat:
    desired = what the YAML says              (replicas: 3)
    actual  = what really exists right now    (2 pods running)
    if actual != desired:
        take the action that closes the gap   (create 1 pod)
```

This single loop is what makes Kubernetes "self-healing":

| Event | Who notices | What happens |
|-------|-------------|--------------|
| A container crashes | kubelet | Restarts the container |
| A pod is deleted | ReplicaSet controller | Creates a replacement pod |
| A node (EC2) dies | Node controller + ReplicaSet controller | Pods are recreated; scheduler places them on other nodes |
| You change `replicas: 3` to `5` | ReplicaSet controller | Two new pods are created |
| You change the image tag | Deployment controller | New ReplicaSet created; rolling update |

**Practical consequence**: don't "fix" things by editing a running pod. The next reconciliation will
replace the pod from the template and your change will vanish. Change the YAML (the desired state) instead.

---

## 6. Putting it together: the full story of `kubectl apply`

You have this Deployment YAML (3 replicas, image `my-registry/my-agent-api:1.0.0`) and run:

```bash
kubectl apply -f deployment.yaml
```

| Step | Who | What happens |
|------|-----|--------------|
| 1 | **kubectl** (on your laptop or Jenkins) | Reads the YAML and sends it to the API server over HTTPS |
| 2 | **API server** | Checks who you are and whether you may do this; validates the YAML |
| 3 | **API server -> etcd** | Saves the Deployment as the desired state |
| 4 | **Deployment controller** | Sees a new Deployment with no ReplicaSet; creates one |
| 5 | **ReplicaSet controller** | Sees "wanted 3 pods, found 0"; creates 3 pod objects. They exist only as records and have no node yet (status `Pending`) |
| 6 | **Scheduler** | Sees 3 pods with no node; picks a node for each, based on free CPU/memory; records the choice |
| 7 | **kubelet** (on each chosen node) | Sees "a pod is assigned to me" |
| 8 | **kubelet -> containerd** | Asks the runtime to pull the image and start the container |
| 9 | **containerd** | Pulls the image from the registry (if not cached on this node), starts the container; the `CMD` runs (`uvicorn ...`) |
| 10 | **kubelet** | Runs the readiness probe; once it passes, reports the pod as Ready |
| 11 | **Service** | Adds Ready pods to its list of targets |
| 12 | **Ingress/Gateway -> Service -> Pod** | User traffic now reaches your app |

After that, the reconciliation loop keeps watching. If a pod disappears later, steps 5 to 10 run again
for the replacement.

```
you -> kubectl -> API server -> etcd
                      │
      controllers create ReplicaSet and Pods
                      │
              scheduler picks nodes
                      │
        kubelet -> containerd -> container running
                      │
        Service -> Ingress -> users
```

---

## Checkpoint (answer in your own words)
1. What are the two kinds of machines in a cluster, and what does each do?
2. Name the four control plane components and give one job for each.
3. Who actually starts the container: the scheduler, the kubelet or the API server? What do the other two do?
4. What is the difference between a Pod, a ReplicaSet and a Deployment?
5. Why does a Service exist if every pod already has an IP address?
6. How does a Service know which pods to send traffic to? What happens if the labels don't match?
7. What does a Namespace do, and why do you add `-n` to `kubectl` commands?
8. A pod crashes and a new one appears with a different name and IP. Which object created it, and why?
9. Explain "desired state + reconciliation loop" using the example of changing `replicas` from 3 to 5.
10. When would you use a Job instead of a Deployment?
11. Why should an agent not keep conversation memory in the pod's own memory or filesystem?
12. Walk through the 12 steps of section 6 from memory and say who performs each.

## Hands-on exercises (no cluster needed yet; about 45 min)
1. Open `deploy/npe_component_dev.yaml` (compass_ai) and `app.qa.yaml` (MCP server). For each, mark:
   `kind`, `metadata.name`, `spec`, image, ports, env vars, labels.
2. In the Deployment YAML in the README cheat sheet, find: the replica count, the label the Deployment
   selects on, the label on the pod template, the container port, and the CPU/memory requests.
3. Write a Service YAML that would route port 80 to that Deployment's port 8000.
4. Draw from memory the chain for `marketplace-api`:
   Deployment -> ReplicaSet -> Pods -> Containers, with a Service in front and Ingress before it.
5. Predict: if you change the image tag from `1.0.0` to `1.0.1`, which objects are created and in what
   order? You will confirm this on a real cluster in Phase 4.

Next: **Phase 4** - install `kubectl` and `kind`, apply these objects for real, kill a pod, and watch
the reconciliation loop bring it back.
