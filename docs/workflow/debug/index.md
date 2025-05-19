# Debugging

Debugging is an integral part of the software development lifecycle. It involves identifying, isolating, and resolving defects or unexpected behaviors in a program. A disciplined approach to debugging not only improves code quality but also enhances developer productivity and collaboration. This section outlines common pitfalls, effective debugging tools, and platform-aware practices for diagnosing issues in Python applications.

## Common Installation and Import Errors

Python's dynamic import system and its dependence on external packages can often result in runtime errors if environments are misconfigured. The most frequent issues include:

**1. ModuleNotFoundError / ImportError**

These typically arise when a package is not installed or is installed in the wrong environment.

```bash
ModuleNotFoundError: No module named 'requests'
```

**Diagnosis and Resolution:**

* Verify the package is installed: `pip list` or `pip show <package>`.
* Ensure you're using the correct Python interpreter: `which python` or `where python` (Windows).
* Use virtual environments (`venv`, `virtualenv`, `conda`) to isolate dependencies.

**2. Circular Imports**

Circular imports occur when two or more modules depend on each other during import time. This often results in partially initialized modules and `AttributeError`.

**Solution:**

* Refactor shared logic into a third module.
* Delay imports (move them inside functions or methods) to break the cycle.

## Using `pdb`, Breakpoints, and Logging Best Practices

**The `pdb` Debugger**

Python’s built-in debugger, `pdb`, allows step-by-step execution and inspection of code state:

```python
import pdb; pdb.set_trace()
```

This launches an interactive shell at that point in execution.

**Common Commands:**

* `n`: next line
* `s`: step into function
* `c`: continue
* `p <expr>`: print expression
* `q`: quit

**Python 3.7+ Shortcut:**

```python
breakpoint()
```

This is a cleaner and more configurable way to invoke the debugger. It respects the `PYTHONBREAKPOINT` environment variable, allowing integration with other debuggers (e.g., `ipdb`).

**Logging Best Practices**

While `print()` can be helpful during early-stage debugging, structured logging is essential for diagnosing issues in production.

Use Python's built-in `logging` module:

```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug("Starting process")
```

**Recommendations:**

* Use levels appropriately (`debug`, `info`, `warning`, `error`, `critical`).
* Avoid logging sensitive data.
* Configure different handlers for file, console, or external systems.

## Resolving Dependency Conflicts and Version Mismatches

Python projects often rely on third-party packages, which can have incompatible dependencies. Common symptoms include:

* `pip` installing a newer version of a package that breaks compatibility.
* Different environments (development vs. production) behaving inconsistently.

**Prevention and Resolution:**

1. **Use `requirements.txt` or `pyproject.toml` to pin dependencies.**

```bash
pip freeze > requirements.txt
```

2. **Use virtual environments consistently.**

Create and activate environments with:

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. **Use dependency resolution tools:**

* [`pip-tools`](https://pypi.org/project/pip-tools/): for safer resolution.
* [`poetry`](https://python-poetry.org/): for modern dependency and packaging management.

4. **When conflicts arise:**

* Inspect with `pipdeptree` to see what is requiring conflicting versions.
* Upgrade/downgrade selectively, and test compatibility before committing changes.

## Platform-Specific Considerations (Windows vs. macOS vs. Linux)

Python is cross-platform, but subtle differences in OS behavior can affect development and debugging.

**1. Path Handling**

Use `os.path` or `pathlib` for portable path construction:

```python
from pathlib import Path

data_file = Path("data") / "input.csv"
```

Avoid hardcoding Windows-style (`C:\\path\\to\\file`) or POSIX-style (`/usr/local/...`) paths.

**2. Line Endings**

Text files edited on Windows may use `\r\n`, while Linux/macOS use `\n`.

Solution:

* Open files in universal mode: `open(file, newline='')`
* Normalize line endings during processing.

**3. Permissions**

* On Linux/macOS, scripts may require executable permissions: `chmod +x script.py`
* On Windows, permissions issues can manifest as `PermissionError` when accessing locked or restricted files.

**4. Shell and Executables**

Scripts that use subprocesses or shell commands may behave differently across platforms:

```python
import subprocess

 Windows-safe
subprocess.run(["dir"], shell=True)

 POSIX-safe
subprocess.run(["ls", "-l"])
```

To write portable code, prefer `shutil` or high-level libraries when possible.

**5. Environment Variables**

Use `os.environ.get("ENV_VAR")` instead of hardcoding paths or secrets, and document any OS-specific dependencies clearly.
