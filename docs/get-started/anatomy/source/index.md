# Source Code Layout

Your Python code is the heart of your project.
Structuring it well from the beginning not only improves readability and maintainability—it also makes packaging, testing, and distributing your project significantly easier.

This section introduces the standard layout used in this template and explains how it compares to other layouts you might see in real-world scientific or open-source projects.

## The Template Layout: `src/`-based Projects

In this template, your Python package lives inside a `src/` directory:

```
src/
  your_package/
    __init__.py
    core.py
    utils.py
```

This is called the “src layout”, and it’s a best practice in modern Python packaging.
The `src/` directory is not required by Python, but it offers significant advantages—especially in larger or long-term projects.

### Why the `src/` layout?

Using a `src/` directory enforces the idea that your package must be installed before it can be used.
This avoids common mistakes like accidental imports from the wrong directory when running tests.

When Python installs your project, it does one of two things:

- For development: It installs a *link* to the source folder (`pip install -e .`), allowing live editing
- For production: It copies and compiles the package to the environment’s `site-packages` directory

The `src/` layout helps simulate that separation and makes sure you’re always importing the installed package—not some local version that only works on your machine.

## What About Flat Layouts?

Some projects use this layout:

```
my_project/
  main.py
  helper.py
  test_main.py
```

This flat structure is fine for scripts or throwaway code but quickly becomes limiting:

- There’s no clear separation between code, tests, and metadata
- Python imports may behave differently after installation
- You can’t package or distribute the project easily

If you’re writing reusable code—even just for your own research group—the `src/` layout is a future-proof foundation.

## Package Installation and Discovery

When you install a package with `pip install .`, Python does the following:

1. Looks for a `pyproject.toml` or `setup.py`
2. Identifies the source code directory and builds it into a distributable format
3. Installs it to the environment’s `site-packages` directory
4. Adds an entry in `sys.path` so your code can be imported like any standard module

This is why `src/` layouts shine: they make sure your code isn’t accidentally on `sys.path` during testing or development, which can hide import bugs.

Whether your code is in `src/your_package/` or `your_package/` directly, Python needs to know:

- What the package is called (`[project] name = "your_package"`)
- Where the package lives (`packages = ["your_package"]` or auto-discovery)

## Choosing the Right Layout for Your Team

Use a `src/` layout if:

- You want to prevent accidental imports during development
- You value clean test environments and installation behavior
- You’re building reusable code, tools, or libraries

Use a flat or direct-layout (no `src/`) if:

- You already have an established internal layout (e.g.
in a research lab)
- You have good test discipline and enforce installation before use
- You prefer simpler directory structures for exploratory projects

Just remember: be consistent, and make sure everything is explicitly installable through `pyproject.toml`.

