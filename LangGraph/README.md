# LangGraph Learning Roadmap

A hands-on, build-first path. No 5-hour videos: each step is a short read (official docs) plus a small script you write yourself. Target: ~1–2 hrs per step, ~2 weeks total.

**Rule:** after each step, write a runnable `.py`/notebook in this folder. If you can't run it, you haven't learned it.

## Prerequisites (skip what you know)

- Python: type hints, `TypedDict`, `async` basics
- LangChain basics: chat models, prompts, tools (see `../Langchain`)
- Access to the Databricks AI Gateway model service (below)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -U langgraph langchain langchain-openai python-dotenv
```

### LLM: Databricks AI Gateway (Unity Gateway) model service

All examples use our own model service instead of a public OpenAI key.

| Item | Value |
|------|-------|
| Workspace | `https://nike-sole-react-3.cloud.databricks.com` |
| Model service | `development.team_compass_ai.lg_model` |
| Base URL (OpenAI-compatible) | `https://nike-sole-react-3.cloud.databricks.com/ai-gateway/mlflow/v1` |
| Auth | Bearer token from `.env` → `databricks_token_langgraph` |

**`.env`** (git-ignored, never commit; see `.env.example`):
```
databricks_token_langgraph=<your token>
```

#### Which endpoint type: Chat Completions vs. Responses?

**Use MLflow Chat Completions.** (Recommendation; also what the rest of this roadmap assumes.)

| | Chat Completions (`/chat/completions`) | Responses (`/responses`) |
|---|---|---|
| Message format | `messages: [{role, content}]` | `input: [{role, content: [{type: input_text}]}]` |
| LangChain / LangGraph support | Default for `ChatOpenAI`; tool calling, streaming, `ToolNode`, `create_react_agent` all just work | Supported only via `use_responses_api=True`; fewer tutorials |
| Docs & examples | Nearly every LangGraph tutorial | Newer, sparse |
| Strengths | Stable, universal, simplest | Built-in server-side tools, reasoning items, stateful conversations |

Why Chat Completions: LangGraph already manages state/memory itself (checkpointers), so Responses' server-side state is redundant, and every tutorial's message format matches Chat Completions. Switch to Responses later only if you need reasoning-model features. Anthropic Messages is only for the native Anthropic SDK; skip it.

Note: some models behind the gateway may not support every endpoint type or tool calling. If Step 5 (tool calling) fails, check which endpoints the model supports on the service's Overview tab.

#### Smoke test (`00_setup/test_llm.py`)

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="development.team_compass_ai.lg_model",
    base_url="https://nike-sole-react-3.cloud.databricks.com/ai-gateway/mlflow/v1",
    api_key=os.environ["databricks_token_langgraph"],
    temperature=0,
)

print(llm.invoke("Say hello in one short sentence.").content)
```

Reuse this `llm` in every later step (put it in a shared `llm.py` and import it).

Optional Responses variant: add `use_responses_api=True` to `ChatOpenAI`.

#### Reference: raw OpenAI SDK (from the service's Overview tab)

Same base URL for both; only the method differs. `ChatOpenAI` calls these for you.

```python
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.environ["databricks_token_langgraph"],
    base_url="https://nike-sole-react-3.cloud.databricks.com/ai-gateway/mlflow/v1",
)

# MLflow Chat Completions (recommended)
chat = client.chat.completions.create(
    model="development.team_compass_ai.lg_model",
    messages=[{"role": "user", "content": "What is Databricks?"}],
    max_tokens=1024,
)
print(chat.choices[0].message.content)

# MLflow Responses
resp = client.responses.create(
    model="development.team_compass_ai.lg_model",
    max_output_tokens=256,
    input=[{"role": "user", "content": [{"type": "input_text", "text": "What is Databricks?"}]}],
)
print(resp.output_text)
```

Note: the Databricks snippet reads `DATABRICKS_TOKEN`; our `.env` uses `databricks_token_langgraph`, so the code above reads that instead.

If it fails: `401/403` → token expired or lacks permission on the service; `404` → check base URL/endpoint path against the cURL on the service's Overview tab; `400` on tools → model doesn't support tool calling.

Docs: https://langchain-ai.github.io/langgraph/

---

## Phase 1 — Core Concepts (Days 1–3)

| Step | Topic | Build |
|------|-------|-------|
| 1 | **Mental model**: State, Nodes, Edges, `StateGraph`, `compile()`, `invoke()` | Hello-world graph with 2 nodes, no LLM |
| 2 | **State & reducers**: `TypedDict`/Pydantic, `Annotated[list, add_messages]` | Counter/list state showing overwrite vs. append |
| 3 | **Conditional edges & routing**: `add_conditional_edges`, `START`/`END` | Router node that picks a branch by input |
| 4 | **Chatbot with LLM**: `MessagesState`, calling a chat model in a node | Minimal chatbot graph |

Checkpoint: explain why LangGraph models agents as graphs instead of chains.

## Phase 2 — Agents & Tools (Days 4–6)

| Step | Topic | Build |
|------|-------|-------|
| 5 | **Tool calling**: `bind_tools`, `ToolNode`, `tools_condition` | Agent with calculator + search tool (ReAct loop by hand) |
| 6 | **Prebuilt agent**: `create_react_agent` | Rebuild step 5 in 5 lines; compare |
| 7 | **Streaming**: `stream_mode` = `values` / `updates` / `messages` | Token streaming to terminal |

## Phase 3 — Persistence & Human-in-the-Loop (Days 7–9)

| Step | Topic | Build |
|------|-------|-------|
| 8 | **Checkpointers & threads**: `MemorySaver`, `SqliteSaver`, `thread_id` | Chatbot that remembers across invocations |
| 9 | **Human-in-the-loop**: `interrupt()`, `Command(resume=...)` | Approval step before a tool executes |
| 10 | **Time travel & state editing**: `get_state`, `update_state`, history | Rewind and replay from a past checkpoint |
| 11 | **Long-term memory**: `Store` API | Save user preferences across threads |

## Phase 4 — Advanced Patterns (Days 10–12)

| Step | Topic | Build |
|------|-------|-------|
| 12 | **Subgraphs** & modular graphs | Nest a graph as a node |
| 13 | **Parallelism**: fan-out/fan-in, `Send` API (map-reduce) | Summarize N docs in parallel |
| 14 | **Multi-agent**: supervisor, swarm/handoffs (`Command(goto=...)`) | Supervisor with researcher + writer agents |
| 15 | **Common patterns**: reflection, plan-and-execute, agentic RAG | Self-correcting RAG over your `../rag` work |

## Phase 5 — Production (Days 13–14)

| Step | Topic | Build |
|------|-------|-------|
| 16 | **Observability**: LangSmith (or MLflow) tracing | Trace a multi-step run |
| 17 | **Error handling**: retry policies, recursion limit, timeouts | Make a flaky tool resilient |
| 18 | **Testing & evals**: node-level unit tests, trajectory evals | Test suite for your agent |
| 19 | **Deploy**: LangGraph Server / Platform, `langgraph.json`, LangGraph Studio | Run your agent locally in Studio |

---

## Capstone

Build one real project end-to-end, e.g. **a metadata-discovery assistant**: supervisor routes to a search agent and a SQL/catalog agent, with human approval before any write, persistent memory, and tracing.

## Best Resources (short, high-signal)

- Official Quickstart + "Build a basic chatbot" tutorial series
- LangGraph Concepts guide (Low-level concepts, Persistence, Human-in-the-loop)
- LangChain Academy — "Introduction to LangGraph" (free, short video+notebook modules)
- `langgraph` GitHub `examples/` and `how-tos`

## Suggested Folder Layout

```
LangGraph/
├── README.md
├── 01_basics/
├── 02_agents_tools/
├── 03_persistence_hitl/
├── 04_advanced_patterns/
├── 05_production/
└── capstone/
```

## Progress Tracker

- [ ] Phase 1 — Core concepts
- [ ] Phase 2 — Agents & tools
- [ ] Phase 3 — Persistence & HITL
- [ ] Phase 4 — Advanced patterns
- [ ] Phase 5 — Production
- [ ] Capstone
