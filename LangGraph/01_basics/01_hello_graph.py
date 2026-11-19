"""Step 1: LangGraph mental model - State, Nodes, Edges, compile, invoke. No LLM."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# 1. STATE: the shared data every node reads from / writes to
class State(TypedDict):
    name: str
    greeting: str
    shout: str


# 2. NODES: plain functions. Input = current state, output = partial update
def make_greeting(state: State) -> dict:
    return {"greeting": f"Hello, {state['name']}!"}


def make_shout(state: State) -> dict:
    return {"shout": state["greeting"].upper()}


# 3. GRAPH: register nodes, wire edges
builder = StateGraph(State)
builder.add_node("make_greeting", make_greeting)
builder.add_node("make_shout", make_shout)

builder.add_edge(START, "make_greeting")
builder.add_edge("make_greeting", "make_shout")
builder.add_edge("make_shout", END)

# 4. COMPILE: validates the graph and returns a runnable
graph = builder.compile()

# 5. INVOKE: pass initial state, get final state
result = graph.invoke({"name": "Harsha"})
print("Final state:", result)

# Peek at each step as it happens
for step in graph.stream({"name": "Harsha"}, stream_mode="updates"):
    print("Step:", step)

# Visualize
print(graph.get_graph().draw_mermaid())
