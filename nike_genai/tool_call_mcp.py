"""

How MCP Tool Calls Work?
----------------------------------------------------------------------------------------------------------

RPC (Remote Procedure Call)
---------------------------
RPC lets you call a function that runs in a different process or machine as if it were a local function call. Instead of importing the function
directly, the caller sends a structured message over the network describing which function to invoke and with what arguments, and gets back the result.


JSON-RPC is an RPC protocol that uses JSON as its message format.


The MCP Tool-Call Flow
--------------------------------------------------------------------------------------------------------------
1. Cursor's built-in MCP client decides it needs to call a tool
   (e.g. `confluence_search`).

2. That function isn't available inside Cursor — it lives in a separate server process (`server.py`, running on 127.0.0.1:8000). 
   So Cursor can't import and call it directly.

3. Instead, Cursor sends a `tools/call` JSON-RPC message over the transport layer (SSE in our case) to the server. 
   The message contains the tool name and arguments.

4. FastMCP's built-in `tools/call` handler receives that message, matches the tool name to the Python function registered via `mcp.tool()`
   (e.g. `mcp.tool()(confluence_search)`), executes it, and sends the result back to Cursor over the same transport.



In short: Cursor asks the server to run a function on its behalf by sending a JSON message, and the server replies with the result — that's
the "Remote Procedure Call."



----------------------------------------------------------------------------



Tool calling is the higher-level action - the agent (Cursor) deciding " I need to run mcp tool"

tools/call is the specific JSON-RPC method name that carries that request over the wire to your MCP server.




"""
