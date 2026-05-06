'''

----------------------  WHAT IS MCP? -----------------------------

MCP (Model Context Protocol) lets AI assistants call external tools (Python functions) running on your local machine.


------------------------------ LOCALHOST --------------------------------

Cursor Agent calls MCP Server on localhost (the same machine).
localhost uses the same RAM, CPU — similar to running code in your terminal.

http://localhost:8000/sse  ==  http://127.0.0.1:8000/sse

host  ->  127.0.0.1  ->  which machine should the code run on? (localhost = same machine)
port  ->  8000       ->  which door on that machine?


------------------------------ MCP ARCHITECTURE -----------------------------

MCP HOST    ->  The app where user interacts with AI assistant.
                Examples: Cursor, VS Code, Claude Desktop.

MCP CLIENT  ->  A component that maintains a connection to an MCP server and obtains context from an MCP server for the MCP host to use




MCP SERVER  ->  A Python program that registers and executes tools (custom Python functions)
                that provide data or context to the LLM based on user requests.
                Note: Code runs on localhost using the laptop's own CPU and RAM.


------------------------------ MCP vs RAG --------------------------------

RAG  ->  Provides static knowledge to LLM (whatever we stored in vector DB beforehand).
MCP  ->  Provides dynamic knowledge to LLM (real-time data fetched when the question is asked).


------------------------------ KEY LIBRARIES --------------------------------

FastMCP                   ->  Framework to build MCP servers in Python.
langchain-mcp-adapters   ->  Library to connect LangChain AI agents to MCP servers.
python-dotenv            ->  Library to load .env file variables into os.environ.


------------------------------ HOW MCP WORKS (FLOW) --------------------------------

1. User provides input (question/prompt) to MCP Host (e.g., Cursor).
2. MCP Client (inside the host) queries connected MCP Servers to discover all available tools and their descriptions.
3. Host sends the user's question + list of available tools to the LLM.
4. LLM analyzes the question and responds with which tool(s) to call and with what arguments.
5. MCP Client invokes the selected tool(s) on the appropriate MCP Server(s),
   which execute the underlying Python functions on localhost (using the machine's own CPU and RAM).
6. Tool results are sent back to the LLM as additional context.
7. LLM generates the final answer using the original question + tool results.
8. Output is displayed to the user in the MCP Host.


------------------------------ SERVER CODE EXPLAINED --------------------------------

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("test-mcp-server", host="127.0.0.1", port=8000)

    "test-mcp-server"  ->  Name of the server (clients use this to identify it).
    host="127.0.0.1"   ->  Listen on localhost only (same machine).
    port=8000           ->  Listen on port 8000.


------------------------------ Registering tools --------------------------------

mcp.tool()(confluence_search)

    mcp.tool()  is a decorator factory. It returns a decorator function.
    (confluence_search)  immediately passes the function to that decorator.

    This is the SAME as writing:

    @mcp.tool()
    def confluence_search(query: str) -> str:
        ...

    We use the manual style when the function is already defined in another file.
    It tells the MCP server: "expose this Python function as a tool that AI agents can call."
    The server reads the function's name, type hints, and docstring to auto-generate the tool schema.


------------------------------ Starting the server --------------------------------

mcp.run(transport="sse")

    Starts the MCP server using SSE (Server-Sent Events) as the transport protocol.
    SSE is an HTTP-based protocol that keeps a long-lived connection open,
    so the server stays alive and handles multiple tool calls without restarting.




------------------------------------------------------------------------------------------------


NOTE

MAKE SURE TO START THE MCP SERVER BEFORE ASKING ANY QUESTIONS TO AI AGENT.

'''