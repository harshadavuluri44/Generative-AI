'''

1. User -> Host: user sends a question
2. Host -> LLM: Host sends the user's question + list of available tools (which it got earlier from server via tools/list through the client) to LLM
3. LLM -> Host: LLM decides it needs a tool and returns a structured "call tool X with these args" response - it does not call anything itself; it just outputs that decision
4. Host -> Client -> server: Host tells it embedded MCP client to send a tools/call request: Client forwards it over the protocol to the server.
5. Server executes the tool and sends the result back to client.
6. Client -> Host: Client hands the raw result back to the Host.
7. Host -> LLM: Host appends the tool result to the conversation and sends it back to the LLM.
8. LLM -> Host -> User: LLM generates the final natural language answer: Host returns it to the user.



NOTE

1. The Client doesn't call tools; it's just a protocol relay between Host and Server

        Client mediates between Host and Server


FINAl


User question to Host -> Host send user question + available tools list to LLM -> LLM decides which tool to call + arguments to HOST -> 
Host tells its CLIENT to call this tool with these argument -> CLient sends the tool-call request to MCP SERVER -> 
Server executes the tool and returns the result to CLIENT -> CLIENT sends the result back to HOST -> 
HOST appends the result to the conversation and sends to LLM -> LLM generates the final answer and gives to HOST -> HOST sends the answer back to user


-----------------------------------------------------------------------------------------------------------------------------------------------------------


The AGENT is NOT just a raw LLM call. It's a loop that works like this:

1. User sends a question
2. The agent send question + available tool descriptions to LLM (via ChatDatabricks)
3. The LLM decides: "I need to call tool X with these arguments"
4. The agent executes that tool call via MCP server
5. The tool result comes back, agent sends it to LLM again
6. The LLM either calls another tools or returns a final answer.


SO ChatDatabricks is brain, and MCP server is hands. The agent framework (e.g., LangChain) manages the loop between them.


Deploy means

Right now, Agent only runs inside a notebook. Deploy means make it a live API endpoint that other apps can call.

The steps are:

1. Log with MLflow - package your agent code + dependencies into a versioned artifact.
2. Deploy to Model Serving - Databricks hosts it as a REST endpoint


After Deployment, any application (a web app, slack bot) can call our agent via an API.


-----------------------------------------------------------------------------------------------------------------------------------------------------------

ChatDatabricks vs Direct Serving Endpoint call - which one gets used, and when?

There are two ways backend code can get an answer out of a Databricks LLM:

    A. Direct serving endpoint call (no tools)
       - Hand-written HTTP call (e.g. httpx/requests) straight to:
             https://<databricks-host>/serving-endpoints/<endpoint-name>/invocations
       - Body: {"messages": [...], "temperature": ..., "max_tokens": ...}
       - Model can ONLY return plain text - it was never told any tools exist,
         so it has no way to "ask" for one.
       - Used for simple one-shot chat: build one prompt -> get one reply -> done.

    B. ChatDatabricks (LangChain wrapper) - used only when tool-calling/agent looping is needed
       - Code does: llm = ChatDatabricks(endpoint=<endpoint-name>, temperature=...)
                    bound_llm = llm.bind_tools([...tool schemas...])
                    bound_llm.invoke(messages) / bound_llm.astream(messages)
       - IMPORTANT: ChatDatabricks does NOT replace/bypass the serving endpoint.
         Under the hood it still does the exact same HTTP call as (A):
             self.client.predict(endpoint=self.endpoint, inputs=data)
         (that "client" is an MLflow deployment client -> same
         /serving-endpoints/<endpoint>/invocations URL, same JSON body shape).
       - What ChatDatabricks ADDS on top of the raw call:
           1. bind_tools() -> attaches tool schemas to the request so the model
              CAN choose to request a tool call.
           2. Parses the response into either:
                - a message with tool_calls populated  -> agent runs the tool,
                  feeds the result back, calls the LLM again (loop)
                - a plain text message                 -> that's the final answer,
                  loop stops.
           3. .stream()/.astream() convenience for token-by-token streaming.

    So the "decide if a tool is needed" step is NOT a separate step before
    calling the LLM. The very first LLM call IS the decision point - the
    model's response shape (tool_calls vs plain text) tells the agent loop
    what to do next. An LLM call happens either way; only the ChatDatabricks
    path ever gives the model the *option* to request a tool.

Who decides which of A/B gets used for a given user request?
    - This is NOT a runtime/dynamic decision based on the user's question.
    - It's a hardcoded, build-time routing decision - which API endpoint (and
      therefore which frontend chat widget) the request goes through decides it:

          Simple FAQ / site-help widget  -> /chatbot            -> (A) direct serving endpoint call
          Smart Search / tool-using agent -> /mcp/query/stream    -> (B) ChatDatabricks + bind_tools

    - Example from marketplace-api:
          ChatbotService.generate_response()   -> httpx POST to /serving-endpoints/.../invocations  (A)
          MCPService + MCPAgent.run_stream()   -> ChatDatabricks(...).astream(messages)               (B)

Bottom line: A serving endpoint call happens 100% of the time, no matter which
path is used. ChatDatabricks is a client library sitting ON TOP of the serving
endpoint (adds tool-calling + streaming ergonomics), not an alternative
transport that avoids it.

'''