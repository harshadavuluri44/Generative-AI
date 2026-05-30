"""
================================================================================
 pip vs uv  +  pyproject.toml vs uv.lock — Personal Reference Notes
================================================================================

Big-picture idea
----------------
    pip is the old, default Python package installer.
    uv  is the modern, much faster replacement (written in Rust) that ALSO manages your virtual environment and your lock file for you.

    One-line difference to remember:
        - With pip, YOU create the .venv manually.
        - With uv, the .venv is created automatically the first time you sync.


--------------------------------------------------------------------------------
 1. THE TWO INSTALLERS
--------------------------------------------------------------------------------

    pip
        - Ships with Python by default.
        - Only installs packages. Doesn't manage venvs or lock files.

    uv
        - Separate tool, installed once on your machine.
        - Does everything: install packages, create venv, resolve versions,
          generate a lock file, run your Python scripts.

    Handy uv commands:

        uv --version          # check the installed uv version
        uv self update        # upgrade uv itself


--------------------------------------------------------------------------------
 2. THE TWO KEY FILES IN A UV PROJECT
--------------------------------------------------------------------------------

    Every uv-managed project has these two files at its root:

    (a) pyproject.toml   — written and edited by HUMANS
    (b) uv.lock          — written and maintained by UV (never edit by hand)


    (a) pyproject.toml  →  "What does this project need?"
    ----------------------------------------------------
        - The main project configuration file.
        - Easy to read and edit manually.
        - Declares high-level / loose requirements.

        Typically contains:
            - Project metadata     (name, version, description, authors, ...)
            - Required libraries   (e.g. requests >= 2.28)
            - Python version       (e.g. requires-python = ">=3.10")
            - Tool configs         (ruff, black, pytest, mypy, etc.)

        Mental model:
            "These are the libraries my project needs to run."


    (b) uv.lock  →  "Exactly which versions did we end up with?"
    -----------------------------------------------------------
        - Auto-generated and updated by uv.
        - DO NOT edit by hand.
        - Hard to read (full URLs, hashes, etc.) — that's intentional.

        Contains:
            - Exact pinned version of every package
            - Every transitive sub-dependency
            - The fully resolved dependency tree, with hashes

        Mental model:
            "These are the EXACT versions every teammate / CI / prod
             must install to get a reproducible environment."


    Side-by-side:

        pyproject.toml  →  declares WHAT is needed     (e.g. requests >= 2.28)
        uv.lock         →  records WHAT WAS RESOLVED   (e.g. requests == 2.31.0)


--------------------------------------------------------------------------------
 3. THE MODERN UV WORKFLOW (adding a dependency)
--------------------------------------------------------------------------------

    Option A — Let uv do everything (recommended):

        $ uv add requests

        This single command will:
            1. Install the package into the project's .venv
            2. Add it to pyproject.toml
            3. Update uv.lock with the resolved versions


    Option B — Edit pyproject.toml manually, then sync:

        1. Open pyproject.toml and add the dependency yourself.
        2. Run:

               $ uv sync

        3. uv installs the packages and regenerates uv.lock to match.


--------------------------------------------------------------------------------
 4. COLLABORATING — RUNNING A PROJECT ON A NEW MACHINE
--------------------------------------------------------------------------------

    Scenario:
        - User 1 created the project and pushed it to git.
        - The repo contains both pyproject.toml and uv.lock.
        - User 2 clones the repo and wants to run it.

    All User 2 has to do:

        $ uv sync

    What this does:
        - Creates a .venv automatically (if one doesn't exist).
        - Installs every dependency at the EXACT versions from uv.lock.
        - Result: User 2's environment is identical to User 1's.


--------------------------------------------------------------------------------
 5. RUNNING PYTHON FILES
--------------------------------------------------------------------------------

    Preferred (uv way):

        $ uv run main.py

    Traditional way:

        $ python3 main.py

    Why prefer `uv run`?
        - It makes sure the project's .venv is active.
        - It makes sure all dependencies are installed at the locked versions
          BEFORE executing the script.
        - No need to manually `source .venv/bin/activate` first.


--------------------------------------------------------------------------------
 6. QUICK CHEAT SHEET
--------------------------------------------------------------------------------

    uv --version                # is uv installed? which version?
    uv self update              # upgrade uv itself

    uv init                     # start a new uv project in the current folder
    uv add <package>            # add a dependency  (updates pyproject + lock)
    uv remove <package>         # remove a dependency
    uv sync                     # install everything from uv.lock into .venv
    uv lock                     # re-resolve and regenerate uv.lock
    uv run <file.py>            # run a script inside the project's .venv

"""
