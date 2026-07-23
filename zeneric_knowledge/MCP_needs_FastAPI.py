'''
Why is FastAPI needed for MCP?
------------------------------------------------------------------------------------------------

FastMCP (mcp) is the MCP layer - it knows about tools, prompts, and the MCP protocol. But MCP is just a protocol.
It needs something to actually receive HTTP requests over the network - that's where FastAPI comes in.


Think of it like this:

    Discover Products (Button on NIM UI) (MCP client)
        |
        | HTTP request (Streamable HTTP transport)
        ↓
    FastAPI app  ← handles HTTP, middleware, auth, lifecycle
        |
        ↓
    FastMCP (mcp)  ← speaks the MCP protocol, routes to tools/prompts  

------------------------------------------------------------------------------------------------


FastMCP alone can't serve HTTP in a production deployment. FastAPI is the web server wrapper that gives the MCP server:

    Proper HTTP handling
    Middleware (logging, auth headers, etc.)
    




'''