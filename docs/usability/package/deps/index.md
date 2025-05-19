# Dependency Management

Managing dependencies is a critical part of creating a reliable and installable Python package. When someone installs your package—whether from PyPI, GitHub, or a local build—they also need any third-party libraries your code relies on to function correctly.

In Python packaging, dependencies are defined in the `pyproject.toml` file under the `[project]` section. This section allows you to distinguish between:

- Runtime dependencies (required for the package to work)
- Development dependencies (used for testing, formatting, linting, etc.)
- Optional dependencies (extras for advanced users or optional features)

Choosing the right dependencies—and how you version them—is essential for maintaining compatibility, avoiding conflicts, and offering a smooth experience for your users.

## Declaring Runtime Dependencies

Runtime dependencies are the packages your code directly depends on to execute correctly. These are the only dependencies you should declare in the `[project]` section:

```toml
[project]
dependencies = [
  "numpy>=1.23",
  "requests~=2.29"
]
```

This tells `pip` to install these dependencies whenever your package is installed, whether from source, a wheel, or PyPI.

Do not include development tools like `pytest`, `mypy`, or `black` in your runtime dependencies. These belong in your development environment (`pixi.toml`, `requirements-dev.txt`, etc.)—not in the package's install metadata.

Why?

- End users don’t need them
- It increases installation time and complexity
- It pollutes the dependency tree for other projects

## Version Pinning Strategies

How you declare version constraints impacts how flexible—or fragile—your package becomes when used in other environments.

Here are three common strategies:

### Loose Pinning

```toml
dependencies = ["requests >=2.0"]
```

- Accepts any version greater than or equal to 2.0
- Gives maximum flexibility to users
- May lead to incompatibility if a future version introduces breaking changes

Use with caution—best suited for internal tools or rapid iteration.

### Tight Pinning

```toml
dependencies = ["requests ==2.29.1"]
```

- Locks the version to exactly one release
- Ensures complete reproducibility
- Risks dependency conflicts with users' environments

This approach is sometimes used in tightly controlled production deployments or research reproducibility contexts, but should be avoided in reusable libraries.

### Compatible Release (`~=`)

```toml
dependencies = ["requests ~=2.29"]
```

- Means “compatible with 2.29, but less than 3.0”
- Accepts patch-level updates (e.g., 2.29.1, 2.29.2)
- Prevents breaking changes while allowing safe upgrades

## Optional and Extra Dependencies

Some features of your package may only be needed in certain scenarios—such as generating documentation, running tests, or using optional integrations.

Instead of including these in your core dependencies, you can declare them as extras:

```toml
[project.optional-dependencies]
docs = ["mkdocs", "mkdocstrings"]
tests = ["pytest", "mypy"]
```

Users can install these extras like this:

```bash
pip install mypackage[docs]
pip install mypackage[docs,tests]
```

This keeps your package lightweight by default, while still supporting advanced use cases.

Extras are especially useful when:

- You want to support documentation generation or testing in CI
- Your project integrates with large optional packages (e.g., `tensorflow`, `matplotlib`)
- You want to separate domain-specific features (e.g., `[aws]`, `[cli]`, `[dev]`)
