'''

Whenever user gives a Natural Language prompt to MCP client, it is send in JSON-RPC format to MCP server.


For example:


1. LLM receives a NL prompt - e.g. "Find me all published data assets related to revenue."
2. The LLM decides (from its system context + tool descriptions) that it needs to call get_assets.
3. The MCP client (Cursor etc.) intercepts that tool decision and serializes it into a JSON-RPC 2.0 request and sends it over HTTP to your FastMCP server.
4.  The server executes get_assets(), hits the Nike Catalog API, gets data back.
5. The result flows back as a JSON-RPC 2.0 response to the client, which feeds it back to the LLM as tool output.


So the user's natural language prompt never travels over JSON-RPC. Only the structured tool invocation decisions (which tool, which arguments) do.


{
    "jsonrpc": "2.0",
    "id": "1",
    "method": "tools/call",
    "params": {
        "name": "get_assets",
        "arguments": {"query": "show me revenue datasets"}
    }
}


'''