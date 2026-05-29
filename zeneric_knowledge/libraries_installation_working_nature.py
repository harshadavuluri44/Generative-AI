"""
Library Installation & Runtime Behavior — Personal Reference Notes
===================================================================


1. INSTALLATION — WHAT HAPPENS WHEN YOU INSTALL A LIBRARY?
------------------------------------------------------------------------------------------------------------------------------

    When you run:

        $ uv add requests          (or uv sync / pip install requests)

    The installer:
        1. Downloads the library's package files from PyPI (Python Package Index — pypi.org)
        2. Also downloads any sub-dependencies the library needs
        3. Copies all their .py source files (and any compiled extensions) into a directory called site-packages

    Where is site-packages?

        With a virtual environment (.venv):
            .venv/lib/python3.x/site-packages/

        Without a virtual environment (system-wide pip install):
            /usr/lib/python3.x/site-packages/       (Linux)
            /Library/Frameworks/.../site-packages/   (macOS)

    So "installing a library" simply means downloading its files and placing them
    on your disk inside site-packages. Nothing is loaded into memory yet.



2. RUNTIME — WHAT HAPPENS WHEN YOUR CODE RUNS?
------------------------------------------------------------------------------------------------------------------------------

    Libraries are NOT loaded all at once when your program starts.
    They are loaded on demand, only when an `import` statement is executed.

    Example:

        import requests          # ← this is the moment the library gets loaded
        requests.get("https://example.com")

    What happens at `import requests`:

        Step 1 — Find
            Python searches for the module in this order:
                a. sys.modules cache  (already imported? reuse it)
                b. Built-in modules   (sys, os, etc.)
                c. sys.path dirs      (includes site-packages, your project folder, etc.)

        Step 2 — Compile
            Python compiles the .py source into bytecode (.pyc files).
            These are cached in __pycache__/ folders for faster future imports.

        Step 3 — Execute
            The module's top-level code runs once. Functions and classes are
            defined (registered in memory), but not called yet.

        Step 4 — Bind
            The module object is placed into sys.modules and bound to the
            name you used (e.g., `requests`), so your code can use it.

    After import:
        - The module's objects (functions, classes, constants) live in RAM.
        - The CPU executes them only when your code actually calls them.
        - If you never import a library, it stays on disk untouched — even if installed.



3. QUICK MENTAL MODEL
------------------------------------------------------------------------------------------------------------------------------

    Installation (disk)                         Runtime (memory)
    ──────────────────                          ────────────────
    PyPI  ──download──►  site-packages/         import statement
                         (files on disk)        ──load──►  RAM
                                                           │
                                                           ▼
                                                        your code calls
                                                        functions/classes



4. COMMON MISCONCEPTIONS
------------------------------------------------------------------------------------------------------------------------------

    ✗  "Installing a library loads it into RAM."
        → No. Installation only puts files on disk. The `import` statement loads them.

    ✗  "All installed libraries are loaded when Python starts."
        → No. Only the modules you explicitly import (and their dependencies) are loaded.

    ✗  ".venv contains running code."
        → No. .venv is just a folder of files on disk. It becomes active only when
          Python's sys.path is pointed at it (via activation or `uv run`).

"""
