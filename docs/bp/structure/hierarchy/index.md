# Building a Package Hierarchy

Once you've decided on a top-level layout—typically using a `src/` directory for installable packages—the next step is organizing your code into a meaningful, maintainable hierarchy. This section explains how Python packages work at the file system level, how to structure your code as it grows, and how to avoid common mistakes when managing module visibility.

## What Makes a Package?

In Python, a package is simply a directory that contains a special file named `__init__.py`. This file tells Python, “this directory should be treated as a module namespace.”

### Modules vs. Packages

| Concept     | What it is                               | Example                       |
| ----------- | ---------------------------------------- | ----------------------------- |
| Module  | A single `.py` file that can be imported | `config.py` → `import config` |
| Package | A directory with an `__init__.py` file   | `utils/` → `import utils.io`  |

This distinction is important because packages allow you to group multiple modules together under a common namespace, which is essential for building large and modular codebases.

## Core Package Layout

Here’s a clean example of a scalable, modular package layout inside a `src/` directory:

```
src/
  mypackage/
    __init__.py
    core.py
    config.py
    utils/
      __init__.py
      io.py
      math.py
```

### Explanation

* `mypackage/` is the root package—this name should match the one used in `pyproject.toml` and `pip install`.
* `core.py` and `config.py` are top-level modules, holding domain-specific logic.
* `utils/` is a subpackage used to collect general-purpose, reusable functions (e.g., for I/O or math).
* Each directory contains an `__init__.py`, making them importable as packages.

This layout is:

* Scalable: New modules can be added without cluttering the root.
* Discoverable: Logical separation makes navigation easy for contributors.
* Flexible: Submodules can be tested and reused independently.

With this structure, users of your package can do:

```python
from mypackage.core import run_analysis
from mypackage.utils.math import normalize
```

Which is clean, readable, and clear.

## Keeping Top-Level Clean

It may be tempting to use your package’s `__init__.py` file as a place to write or organize logic—but resist the urge. Your `__init__.py` should serve as a public interface, not a dumping ground.

### What to do in `__init__.py`:

* Expose key functionality in a simplified namespace:

  ```python
  from .core import run_simulation
  from .config import load_config
  ```

  Now users can do:

  ```python
  from mypackage import run_simulation
  ```

* Initialize package-wide settings or state (sparingly)

* Define the package’s `__all__` list (optional):

  ```python
  __all__ = ["run_simulation", "load_config"]
  ```

### What *not* to do:

* Don’t write core functionality directly in `__init__.py`
* Don’t use it for large amounts of logic, data processing, or constants
* Don’t import every submodule “just in case”—it slows imports and clutters the namespace

> Think of `__init__.py` as a curated entry point, not a code file.

