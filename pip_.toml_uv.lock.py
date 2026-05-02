"""
pip, pyproject.toml, uv, and uv.lock — Personal Reference Notes
================================================================


1. PACKAGE INSTALLERS
------------------------------------------------------------------------------------------------------------------------------

    pip
        - The traditional Python package installer.
        - Ships with Python by default.

    uv
        - A modern, much faster alternative to pip.
        - Written in Rust; handles installs, locking, and virtual environments.



2. KEY FILES
------------------------------------------------------------------------------------------------------------------------------

    pyproject.toml  (human-written config file)

        - The main project configuration file.
        - Easy to read and edit manually.

        Contains:
            - Project metadata (name, version, description, etc.)
            - Required libraries (dependencies)
            - Python version constraint
            - Tool configurations (linters, formatters, etc.)

        In short: "These are the libraries required to run this project."


    uv.lock  (auto-generated lock file)

        - Created and maintained automatically by uv.
        - NOT meant to be edited by hand.
        - Contains full resolved URLs, hashes, etc. — difficult to read.

        Contains:
            - Exact pinned versions for every package
            - All sub-dependencies (transitive dependencies)
            - The fully resolved dependency tree

        In short: "These are the exact versions everyone should install."


    pyproject.toml vs uv.lock

        pyproject.toml  — Declares *what* the project needs  (e.g. requests>=2.28)
        uv.lock         — Records *exactly* what was resolved (e.g. requests==2.31.0)



3. MODERN UV WORKFLOW
------------------------------------------------------------------------------------------------------------------------------

    Option A — Add a package via the CLI:

        $ uv add requests

        This automatically:
            1. Installs the package
            2. Adds it to pyproject.toml
            3. Updates uv.lock


    Option B — Edit pyproject.toml manually, then sync:

        1. Add the dependency to pyproject.toml by hand
        2. Run:  $ uv sync
        3. uv installs the packages and regenerates uv.lock



4. COLLABORATING — SETTING UP ON A NEW MACHINE
------------------------------------------------------------------------------------------------------------------------------

    Scenario: User 1 created the codebase. User 2 clones it and wants to run it.
              The repo already contains pyproject.toml and uv.lock.

    All User 2 needs to do:

        $ uv sync

    This installs every dependency at the exact locked versions.



5. RUNNING PYTHON FILES
------------------------------------------------------------------------------------------------------------------------------

    $ uv run main.py       (preferred)
    $ python3 main.py      (traditional)

    Prefer `uv run` — it ensures the correct virtual environment is active
    and all dependencies are installed at the required versions before execution.

"""
