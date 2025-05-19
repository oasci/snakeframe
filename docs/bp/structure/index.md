# Project Structure

## Building a Package Hierarchy

Once you've decided on a top-level layout—typically using a `src/` directory for installable packages—the next step is organizing your code into a meaningful, maintainable hierarchy. This section explains how Python packages work at the file system level, how to structure your code as it grows, and how to avoid common mistakes when managing module visibility.

### What Makes a Package?

In Python, a package is simply a directory that contains a special file named `__init__.py`. This file tells Python, “this directory should be treated as a module namespace.”

#### Modules vs. Packages

| Concept     | What it is                               | Example                       |
| ----------- | ---------------------------------------- | ----------------------------- |
| Module  | A single `.py` file that can be imported | `config.py` → `import config` |
| Package | A directory with an `__init__.py` file   | `utils/` → `import utils.io`  |

This distinction is important because packages allow you to group multiple modules together under a common namespace, which is essential for building large and modular codebases.

### Core Package Layout

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

#### Explanation

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

### Keeping Top-Level Clean

It may be tempting to use your package’s `__init__.py` file as a place to write or organize logic—but resist the urge. Your `__init__.py` should serve as a public interface, not a dumping ground.

#### What to do in `__init__.py`:

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

#### What *not* to do:

* Don’t write core functionality directly in `__init__.py`
* Don’t use it for large amounts of logic, data processing, or constants
* Don’t import every submodule “just in case”—it slows imports and clutters the namespace

> Think of `__init__.py` as a curated entry point, not a code file.

## Organizing by Function vs. Layer

Once your project grows beyond a few modules, you’ll need to make thoughtful decisions about how to organize your internal structure. This isn’t just about where files go—it’s about how you and others navigate, extend, and maintain the project over time.

There are two common strategies for organizing subpackages in Python projects:

1. Layered Structure: Organizing by technical role (e.g., “core logic”, “API interface”, “utilities”)
2. Feature-Based Structure: Organizing by domain features (e.g., “molecules”, “simulations”)

Both approaches are valid. Each offers different strengths depending on the size, purpose, and complexity of your project.

### Layered Structure

In a layered structure, your code is grouped by its technical responsibility—regardless of the specific domain it serves.

```
mypackage/
  api/
    cli.py
    web.py
  core/
    model.py
    simulation.py
  utils/
    io.py
    math.py
```

#### Folder Roles

* `api/`: Entry points and interfaces—e.g., CLI commands, REST endpoints, or notebooks.
* `core/`: The essential logic that defines what your software *does*. This is your business or scientific logic.
* `utils/`: Supporting functionality that is general-purpose and not tied to the domain (e.g., string manipulation, file loading, error formatting).

#### Benefits

* Separation of concerns: Each folder serves a clearly defined purpose.
* Familiarity: This structure is common in web frameworks and enterprise applications.
* Pluggability: It’s easy to swap out infrastructure—like replacing a CLI with a web UI—without touching your core logic.

#### When to Use It

* Your project has multiple “delivery mechanisms” (e.g., a CLI *and* an API).
* You want to isolate interfaces from internal logic.
* You expect to evolve your user interface or input/output mechanisms over time.

> 🧠 Mental model: You’re building a layered cake—each layer has a clear role and responsibility.

### Feature-Based Structure

In a feature-based structure, code is grouped by domain or functional area. Each folder encapsulates everything related to a specific feature, including logic, configuration, and utilities.

```
mypackage/
  molecules/
    align.py
    visualize.py
    io.py
  simulation/
    run.py
    config.py
    slurm.py
```

#### Folder Roles

* `molecules/` might contain everything related to molecular manipulation.
* `simulation/` might handle simulation configuration, orchestration, and results.

Each subpackage becomes a sort of mini-application, responsible for its own domain. Logic, helpers, and configs live side-by-side—often closer to how subject-matter experts think about the problem.

#### Benefits

* Cohesion: All code related to a feature lives together.
* Discoverability: Easier for new contributors or domain experts to find what they need.
* Maintainability: You can evolve one feature without accidentally affecting others.

#### When to Use It

* Your project is research- or domain-driven.
* You’re working with a team of specialists who each own part of the problem space.
* The user mental model aligns with distinct functional areas.

> 🧠 Mental model: You’re building modules like LEGO bricks—each one complete and self-contained.

### Which Should You Use?

There’s no universal rule, but here are some guiding questions:

| Question                                              | Prefer Layered | Prefer Feature-Based |
| ----------------------------------------------------- | -------------- | -------------------- |
| Are your features tightly interconnected?             | ✅              | 🚫                   |
| Are your interfaces likely to change?                 | ✅              | 🚫                   |
| Do domain experts need to navigate the code?          | 🚫             | ✅                    |
| Are you building a platform with multiple subsystems? | ✅              | ✅ (with nesting)     |

### Hybrid Approaches

Many mature projects adopt a hybrid structure—feature-based at the top, but layered within each feature.

Example:

```
mypackage/
  simulation/
    api/
      cli.py
    core/
      run.py
      config.py
    utils/
      file_io.py
```

This combines the clarity of feature boundaries with the benefits of layering inside each submodule.
