'''

MCP INSPECTOR 
------------------------------------------------------------------------------------------

What is MCP Inspector?

MCP Inspector is a generic open-source debugging tool made by MCP creators (Anthropic). It has nothing to do with any specific company's code.


    Think of it like Postman:
        Postman         -> lets us call any REST API visually (we pick endpoint, fill params, click send)
        MCP Inspector   -> lets us call any MCP server visually (we pick tool, fill args, click Run)

Code is Published at: https://github.com/modelcontextprotocol/inspector

It is a TypeScript application published on npm registry (not PyPI). That is why we run it with npx, not pip.

------------------------------------------------------------------------------------------

Why USE MCP INSPECTOR? (PURPOSE)

Normally an AI agent (Claude, Cursor, etc.) connects to an MCP server and calls tool automatically. 
MCP Inspector lets a HUMAN do the same thing manually - to verify the server works correctly before plugging it into an AI.


    PRODUCTION:  AI Agent   -  MCP  -   MCP Server   -  Upstream API
    QA TESTING:  Human via Inspector - MCP - MCP Server - Upstream API

we are replacing the AI agent with ourself during testing.

------------------------------------------------------------------------------------------

HOW IT WORKS - STEP BY STEP

Step 1: Run the Inspector on your MAC terminal

        npx @modelcontextprotocol/inspector

        what happens internally:
            npx downloads the Inspector package (JS files)
            npx hands those files to Node.js to execute
            Node.js starts a tiny local web server on your MAC (port 6724 by default)
            Terminal prints:  "http://localhost:6724"
    "localhost" = on our own computer, not the internet, not any cloud.


Step 2: Open the browser

    Go to http://localhost:6724
    A visual UI loads - this is the Inspector interface running locally.

Step 3: Connect to the MCP server

Step 4: List tools

Step 5: Call a tool



NOTE - There is no LLM or AI agent running in MCP Inspector. It is a pure developer tool - a dumb HTTP client with a nice UI






















'''