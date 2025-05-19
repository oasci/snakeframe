# Application Programming Interfaces (APIs)

An Application Programming Interface (API) defines how parts of a program—or entirely separate programs—interact with one another through well-defined, stable boundaries. APIs are how you expose your code for others to use—whether those others are colleagues, external developers, future you, or even other parts of your own system.

## What Is an API?

At its core, an API is a contract—it defines how other code is allowed to interact with a system. That contract includes:

- What functions or classes exist
- What arguments they accept and what they return
- What behaviors or side effects are guaranteed
- What errors may be raised

This contract allows code to be reused without knowing its internal implementation. For example, when you use:

```python
from numpy import mean
```

You’re using NumPy’s API. You don’t need to read its source code to trust what it does—you just need to know how to call it and what it returns.

## Why APIs Matter

A good API:

- Makes code reusable across projects or domains
- Enables collaboration by creating a shared interface between teams or components
- Improves maintainability by isolating change: internals can evolve as long as the interface stays stable
- Creates trust: users rely on the interface being predictable and well-documented

Without an API, you risk building a tightly-coupled system where every module knows too much about every other module. That makes change expensive and error-prone.

## Types of APIs in Python Projects

###  Module-Level APIs

These are public functions or classes that your package exposes.

Example:

```python
# mypackage/core.py

def compute_energy(molecule):
    ...
```

```python
# user code
from mypackage.core import compute_energy
```

Here, `compute_energy()` is part of your public API—it should be stable, documented, and safe to use.

To keep your internal and public APIs distinct:

- Use underscores (`_`) to prefix private functions (`_helper()`)
- Use `__all__` in `__init__.py` to declare what’s public
- Document public APIs in your documentation site (not internal helpers)

### CLI APIs (Command Line Interfaces)

If your tool is meant to be used from the terminal, your API might be a CLI. This can be as simple as:

```python
# cli.py
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    run_analysis(args.input)
```

You can expose this in `pyproject.toml`:

```toml
[project.scripts]
mypackage = "mypackage.cli:main"
```

Now users can run your tool with:

```bash
mypackage --input data.csv
```

The CLI becomes a stable contract—once published, changing its behavior or flags can break workflows. Treat it as carefully as any other API.

### Web APIs

If your tool needs to be accessed remotely or by other software, you might build an HTTP API using frameworks like:

- `FastAPI` (modern, async, type-safe)
- `Flask` (lightweight, flexible)
- `Django` (batteries-included)

Example using FastAPI:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/energy")
def get_energy(molecule_id: str):
    return {"energy": compute_energy(molecule_id)}
```

Web APIs should:

- Be versioned (`/v1/`, `/v2/`)
- Be documented (e.g., with OpenAPI or Swagger)
- Validate inputs and return predictable output

### Plugin APIs

Some systems expose APIs for extension—where others can register new functionality or behaviors.

This often takes the form of:

- A registry pattern (`register_plugin(plugin)`)
- Dynamic loading via entry points (`importlib.metadata`)
- Custom interfaces or base classes for implementers

Example:

```python
# Base plugin interface
class SimulationBackend:
    def run(self, config): raise NotImplementedError

# User plugin
class GROMACSBackend(SimulationBackend):
    def run(self, config):
        ...
```

This pattern is common in scientific tooling, where labs want to plug in their own backend or analysis routines.

## How to Design a Good API

### Be Explicit and Predictable

Avoid magic or implicit behavior. Users should never be surprised.

Bad:

```python
def process(data): ...
```

Better:

```python
def process_csv_file(file_path: str) -> pd.DataFrame: ...
```

### Name Things Clearly

Names should reflect what something does and how it's used—not internal implementation details.

Prefer `normalize_vector()` over `do_math()`.

### Separate Concerns

Your API should expose clean, focused actions—not giant multifunctional objects.

```python
# Better to separate responsibilities
def load_data()
def validate_data()
def analyze_data()
```

### Document Everything Public

Every public function, method, or CLI flag should have:

- A clear docstring
- Expected inputs and return types
- Description of side effects or raised exceptions

### Avoid Breaking Changes

Once an API is published, assume someone depends on it. If you must break it:

- Bump the major version
- Announce and document the change clearly
- Offer a transition path or deprecated alias
