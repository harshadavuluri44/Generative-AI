'''
An SDK (Software Development Kit) is a collection of tools, libraries, documentation, and code samples proivided by a platform or company to help developers 
build applications.

It typically includes:
    
        Libraries/APIs, Documentation, Code samples



MCP SDK is a set of official developer tools that make it easier to build applications and services that can communicate with AI models and other MCP-compliant
systems.


It helps developers quickly create servers and clients that exchange context, tools and data.

---------------------------------------------------------------------------------------------------------------------------------

Example :

    MCP SDK provides classes like FastMCP


        from mcp.server.fastmcp import FastMCP

        mcp = FastMCP("test-mcp-server", host="127.0.0.1", port=8000)

        mcp.run()





'''