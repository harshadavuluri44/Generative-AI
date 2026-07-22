'''
Complete End to End MCP Flow


1. Server Startup
    Developer starts the FastMCP server
    uvicorn starts -> FastAPI + FastMCP app is live
    Cursor/Claude Desktop connects to it via mcp config

2. Handshake
    who does this: The MCP client (Cursor/Claude Desktop)
    The MCP client sends a handshake request to the server
    The server responds with a handshake response
    The MCP client and server are now connected

3. Discovery
    who does this: The MCP client (Cursor/Claude Desktop)
    MCP client sends POST / method - tools/list and Server response back with result
    MCP client stores the result in its tool catalog

4. User Types a Message
    MCP client send this + tools to LLM

    LLM thinks: I have a tool called get_assets that fetches catalog assets.

5. Tool execution
    MCP client -> MCP server

6. LLM generates answer

    MCP client feeds the tool result back to LLM.

'''