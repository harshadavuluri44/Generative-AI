'''

Cursor Agent prefers to call MCP Server/external tool on localhost on the same machine.


localhost is the same machine which gets same RAM, CPU to execute code which is similar to run on terminal.



http://localhost:8000/sse  == http://127.0.0.1:8000/sse


host  ->  localhost -> which machine should the code run?
port  ->  8000      -> which door






MCP HOST -   Place where user intreacts with AI Assistant.

    Examples: Cursor, VS code, etc.



MCP CLIENT   ->  Runtime bridge inside the host that connects user/assistant requests to MCP servers, using .mdc configs as its map.

MCP Server ->  Python program that registers and executes tools (custom python functions) that provides data or context to LLM based on user request.

    Note: Python code runs on localhost with RAM, CPU from laptop.


'''