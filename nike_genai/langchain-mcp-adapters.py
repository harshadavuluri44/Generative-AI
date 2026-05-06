'''
=======================================
MCP CLIENT: Cursor (Built-in) vs LangChain (langchain-mcp-adapters)
=======================================


KEY COMPONENTS
--------------

1. FastMCP Server
   - Exposes external data/tools (Confluence, Slack, Databricks, etc.) over the MCP protocol.
   - Runs as a standalone process (e.g. on localhost:8000/sse).
   - Any MCP-compatible client can connect to it.

2. MCP Client
   - Connects to the MCP server, discovers available tools, calls them, and returns results.
   - Both Cursor and langchain-mcp-adapters serve this role — just in different contexts.


--------------------------------------------------------------------------------------------------------------


CURSOR AGENT (Built-in MCP Client)
-----------------------------------

Cursor IDE has a native MCP client embedded in its agent runtime.

    Cursor Agent  ──(MCP protocol over SSE)──►  FastMCP Server

- No adapter library needed.
- Configuration lives in .cursor/mcp.json:

      {
        "mcpServers": {
          "platforms-mcp-server": {
            "url": "http://localhost:8000/sse"
          }
        }
      }

- On startup, Cursor's MCP client reads mcp.json, connects to the server,
  fetches the list of available tools, and makes them callable by the agent.

This is why route-and-research-l3 does NOT use langchain-mcp-adapters —
it relies entirely on Cursor's built-in MCP client.


--------------------------------------------------------------------------------------------------------------


CUSTOM LANGCHAIN AGENT (langchain-mcp-adapters as MCP Client)
--------------------------------------------------------------

LangChain agents do NOT natively speak MCP. To connect them to an MCP server,
you need langchain-mcp-adapters, which acts as the MCP client.

    LangChain Agent  ──(langchain-mcp-adapters)──►  FastMCP Server

- langchain-mcp-adapters connects to the MCP server.
- Discovers available tools and converts them into LangChain-compatible tool objects.
- The LangChain agent can then call these tools as part of its reasoning loop.


--------------------------------------------------------------------------------------------------------------


SUMMARY
-------

+-------------------------+-------------------------------+----------------------------------+
|                         | Cursor Agent                  | Custom LangChain Agent           |
+-------------------------+-------------------------------+----------------------------------+
| Has MCP client?         | Yes (built into Cursor IDE)   | No (needs an adapter)            |
| What acts as client?    | Cursor's native MCP client    | langchain-mcp-adapters library   |
| Configuration           | .cursor/mcp.json              | Code-level setup via adapter     |
| Adapter library needed? | No                            | Yes (langchain-mcp-adapters)     |
+-------------------------+-------------------------------+----------------------------------+

Both approaches talk to the same FastMCP server — the only difference is
what serves as the MCP client on the agent side.

'''
