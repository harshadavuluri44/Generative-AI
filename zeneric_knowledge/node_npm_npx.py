'''
Node.js is NOT a language. It is a runtime engine.

    Python interpreter  ->  the engine that RUNS Python code
    Node.js             ->  the engine that RUNS JavaScript code

JavaScript is the language (the code we write). Node.js is the engine that reads and runs it.

------------------------------------------------------------------------------------------------

npm and npx are helper tools that come bundled with Node.js (just like pip comes with Python).
They don't run code themselves — they download packages and hand them to Node.js to execute.

    pip install package  =  npm install package

pip is not Python; it's a helper that downloads the package. Python itself runs the code.
Same idea: npm/npx download packages, Node.js runs them.

------------------------------------------------------------------------------------------------

When we install Node.js, we get two commands automatically:

    npm  =  Node Package Manager — installs packages permanently.
    npx  =  Node Package Execute  — downloads a package, runs it once, then discards it.

# without npx
npm install -g @modelcontextprotocol/inspector   # install globally first
inspector                                        # then run it

# with npx
npx @modelcontextprotocol/inspector              # download + run in one step

Internally, npx calls "node filename.js" after downloading the package.

npx is perfect for tools we run occasionally (like MCP Inspector) because we always get the
latest version and don't clutter the system with permanent installs.
'''
