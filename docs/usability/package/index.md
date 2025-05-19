# Packaging

When you're just starting out, it's common to work with standalone scripts like `analysis.py` or `run_experiment.py`. But as your code grows in size, complexity, or audience, you need a structured way to distribute it, reuse it across projects, and install it in different environments. That's where packaging comes in.

Packaging a Python project involves organizing your code in a standard way, describing it with metadata, and optionally distributing it through tools like `pip` and platforms like PyPI (the Python Package Index).

Let’s start with the fundamentals.

## What Does It Mean to “Package” a Python Project?

To package a Python project means to:

1. Organize your code in a predictable directory structure
2. Describe your project using metadata (name, version, dependencies, etc.)
3. Build a distributable archive, like a `.whl` (wheel) or `.tar.gz` file
4. Allow others (or yourself) to install your code using a package manager like `pip`

Once packaged, your project can be:

- Installed as a dependency (`pip install mypackage`)
- Deployed in production environments
- Uploaded to PyPI or shared privately
- Imported just like any standard Python module

Packaging makes your work reproducible, maintainable, and shareable.

## Script vs. Module vs. Package

To understand packaging, it helps to understand the basic building blocks of Python code organization.

| Concept     | Description                                                           | Example                                          |
| ----------- | --------------------------------------------------------------------- | ------------------------------------------------ |
| Script  | A single `.py` file that you run directly                             | `run_simulation.py`                              |
| Module  | Any `.py` file that can be imported                                   | `utils.py` (used as `import utils`)              |
| Package | A directory with an `__init__.py` file that contains multiple modules | `mypackage/` with `__init__.py`, `core.py`, etc. |

In packaging, we're primarily working with packages. These can be installed, versioned, and reused across environments. Packaging turns your `mypackage/` folder into something that can be installed and run on another machine with zero setup beyond `pip install`.

For example, after packaging and installing:

```python
from mypackage.core import run_model
```

...just works, the same way importing `math` or `pandas` does.

## Why Packaging Matters

Packaging may seem like an advanced or optional step when you're just writing Python for your own use, but it brings several long-term benefits:

- Instead of copying files between projects, you install your code once and import it anywhere.
- Others can install your work via `pip`, GitHub, or PyPI.
- You define exact dependencies, which ensures your code runs consistently across machines.
- Structured projects are easier to test, document, extend, and collaborate on.
- Properly packaged software reflects maturity and readiness for real use, publication, or collaboration.

In research environments, reproducibility is critical. Packaging ensures that your codebase is stable, documented, and locked to specific versions. That’s essential for revisiting results or sharing your tools with other labs or collaborators.

## How Python Finds and Installs Packages

When you install a Python package (whether it’s your own or someone else’s), it ends up in a special directory called `site-packages`. This is the central location where Python stores installed libraries and tools.

Here’s what happens under the hood when you run:

```bash
pip install mypackage
```

1. `pip` fetches a `.whl` (wheel) or `.tar.gz` file from PyPI (or a local directory, if specified).
2. The archive is extracted into your environment’s `site-packages/` directory.
3. Python updates metadata so it knows where to find the installed package.
4. When your code says `import mypackage`, Python looks inside `site-packages` and loads your module.

You can see what’s installed by running:

```bash
pip list
```

And you can find the exact path of a package like this:

```python
import mypackage
print(mypackage.__file__)
```

When developing locally, it’s common to install your own package in “editable” mode:

```bash
pip install -e .
```

This creates a link to your working directory, so that changes you make to the code are reflected immediately without reinstalling. This is especially useful during development or when working in a collaborative setting.
