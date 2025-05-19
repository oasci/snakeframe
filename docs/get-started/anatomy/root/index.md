# Root Configuration Files

At the top level of your project folder (also known as the project root), you'll find several key configuration files.
These files don’t contain your code, but they orchestrate how your code is run, tested, formatted, documented, and shared.

## `pyproject.toml`

This is the central configuration file for your project.
It’s a standardized file introduced by [PEP 518](https://peps.python.org/pep-0518/) and expanded in later PEPs.
It replaces the older `setup.py`, `setup.cfg`, and other fragmented tools.

The `pyproject.toml` file contains:

- Project metadata: name, version, authors, description, license
- Build system: tells Python how to build your project (e.g.
with `hatchling` or `setuptools`)
- Tool settings: this is where tools like `black`, `mypy`, or `pytest` can optionally store their configuration

Think of it as the project’s “command center.” Modern tools read from it automatically, and you’ll rarely need to manually run long commands—just let `pyproject.toml` do the work.

## `pixi.toml`

This file is used by Pixi, a modern environment and task manager (like `conda` or `poetry`, but faster and more reproducible).
It defines:

- The version of Python used in development
- All dependencies (runtime and development)
- Custom commands (like `pixi run lint`)

Pixi ensures that every contributor works in the same environment with the same tools.
This drastically reduces "works on my machine" bugs and makes onboarding new developers seamless.

## Linter and Tooling Configs

To keep your code clean and consistent, we use automated tools like linters, formatters, and type checkers.
Each has its own config file:

- `.ruff.toml`: Configures `ruff`, a fast all-in-one linter and formatter.
- `.mypy.ini`: Settings for `mypy`, which checks for type errors in your code.
- `.isort.cfg`: Defines how `isort` should order your import statements.
- `.flake8`: Legacy support for older linting tools if needed.
- `.coveragerc`: Controls how code coverage is measured.
- `.pytest.ini`: Additional settings for test discovery and behavior.

You don't need to remember all the options.
These are pre-configured in the template with sensible defaults, and the tools will automatically pick them up.

