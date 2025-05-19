# Metadata

In Python packaging, this metadata is defined in the `pyproject.toml` file, which is located in the root of your project. This file is the standardized entry point for building, installing, and configuring Python packages and tools. Think of it as your project’s identity card and configuration hub.

Good metadata is not just for machines. It helps users, contributors, and automated tools understand what your project is, how to use it, and whether it’s compatible with their environment.

## Required Fields

The following fields are essential to package your project correctly and publish it to places like PyPI.

### `name`

This is the name of your package as it will appear on PyPI and be installed via `pip`.

```toml
name = "mypackage"
```

- This must be unique across PyPI.
- It should match your importable package name (e.g., `import mypackage`).
- Use lowercase letters, numbers, and hyphens (`-`); underscores are discouraged.

### `version`

The version of your package, typically using semantic versioning: `MAJOR.MINOR.PATCH`.

```toml
version = "0.1.0"
```

Semantic versioning helps users and tools understand whether an update introduces new features, bug fixes, or breaking changes.

- `0.x.x` = experimental or early-stage
- `1.0.0` and up = stable public API

### `description`

A one-line summary of your project’s purpose.

```toml
description = "A toolkit for analyzing molecular dynamics simulations."
```

This appears on PyPI and in search results. Keep it clear and concise.

### `authors` and `maintainers`

A list of people responsible for the project, with optional email addresses.

```toml
authors = [{ name = "Jane Doe", email = "jane@example.com" }]
maintainers = [{ name = "Lab XYZ", email = "dev@xyzlab.org" }]
```

Use `authors` for creators and `maintainers` for ongoing support roles. For academic teams, this might include lab members, institutional emails, or shared accounts.

### `license`

An [SPDX license identifier](https://spdx.org/licenses/) indicating the license your code is released under.

```toml
license = { text = "MIT" }
```

Common examples:

- `MIT`: permissive, simple
- `Apache-2.0`: permissive with patent clause
- `GPL-3.0-only`: strong copyleft
- `BSD-3-Clause`: permissive with attribution

Including a license is essential for open-source distribution.

## Optional but Recommended Fields

These fields are not required for building or installing your package, but they greatly improve clarity, usability, and discoverability—especially if you plan to share your project publicly.

### `readme`

Specifies the file to be used as the long description on PyPI.

```toml
readme = "README.md"
```

This file must exist and be in Markdown or reStructuredText format. It gives users a detailed overview of your project directly on its PyPI page.

### `homepage`, `repository`, `documentation`

These links point users to relevant resources:

```toml
homepage = "https://mypackage.org"
repository = "https://github.com/your-org/mypackage"
documentation = "https://mypackage.org/docs"
```

- `homepage`: general landing page
- `repository`: source code
- `documentation`: full user or API docs

Tools like `pip` and PyPI use these links to guide users.

### `keywords`, `classifiers`

These help with discoverability in the Python ecosystem:

```toml
keywords = ["simulation", "molecular-dynamics", "bioinformatics"]

classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
]
```

Classifiers are standardized and can indicate things like Python version compatibility, maturity level, license, and domain. You can browse the full list of valid classifiers [here](https://pypi.org/classifiers/).

### `requires-python`

Declares the minimum Python version your package supports:

```toml
requires-python = ">=3.9"
```

This ensures that users with incompatible Python versions will get a warning and prevents installation in unsupported environments.

## Tool-Specific Sections

Beyond core metadata, `pyproject.toml` allows you to configure tools like linters, type checkers, and testing frameworks in a centralized way. This keeps your project clean and avoids configuration sprawl.

### Build Backend Configuration

If you're using `setuptools` (common) or another build tool like `hatch`, you’ll need to define the backend:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

This tells Python how to build your package when someone runs `pip install`.

### Package Discovery

If you’re using the `src/` layout, you'll need to tell `setuptools` how to find your code:

```toml
[tool.setuptools.packages.find]
where = ["src"]
```

This tells the build system to look inside the `src/` directory for packages, rather than assuming they live at the root.

### Tool Configurations

You can configure development tools inside `pyproject.toml` under their own `[tool.*]` sections. For example:

```toml
[tool.black]
line-length = 88

[tool.mypy]
strict = true

[tool.pytest.ini_options]
minversion = "6.0"
```

This approach avoids a clutter of separate config files (like `.flake8`, `.mypy.ini`, etc.) and keeps your project more portable.
