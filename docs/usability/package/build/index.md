# Building

Once you've defined your package’s metadata and structure, the next step is to build it. Building a package means converting your project from a collection of source files into a standardized archive format that can be installed using tools like `pip` or uploaded to a package index like PyPI.

## Types of Distributions

Python packages can be distributed in two formats:

### Source Distribution (sdist)

- File extension: `.tar.gz`
- Contains your raw source code and metadata files
- When installed, it is built on the user’s machine
- Slower to install and more prone to build issues
- Required for compatibility with some older tools

A source distribution is essentially a compressed copy of your project with special metadata. It's useful for sharing the full editable source code, including any optional build steps (like C extensions or data generation).

### Built Distribution (Wheel)

- File extension: `.whl`
- Pre-built and ready to install with `pip`
- Fast installation—no compilation step needed
- Preferred by modern Python packaging tools

Wheels are the standard format used when you run `pip install`. They are platform-independent for pure-Python packages (like yours), and their internal structure allows tools to install them quickly and safely.

> Best Practice: Always build both types and upload both to PyPI, even if you're primarily using wheels.

## How to Build

Before you can build your project, you need to install the Python build tools:

```bash
pip install build
```

This uses the [`build`](https://pypa-build.readthedocs.io/) package, which is a frontend to your specified build backend (like `setuptools` or `hatch`). It's standardized and works with any project using a `pyproject.toml` file.

### Build Your Project

From the root of your project (where `pyproject.toml` lives), run:

```bash
python -m build
```

This will:

1. Read `pyproject.toml` to determine your build system
2. Generate both a `.tar.gz` and a `.whl` file
3. Save them in a newly created `dist/` directory

Example output:

```
dist/
  mypackage-0.1.0.tar.gz
  mypackage-0.1.0-py3-none-any.whl
```

You can now install either of these locally with `pip`, upload them to PyPI, or share them with collaborators.

## Inspecting the Build

Once your package is built, it’s a good habit to inspect the contents and validate the metadata before publishing.

### Inside a `.whl` file

Wheels are ZIP archives. You can explore their contents by unzipping them:

```bash
unzip dist/mypackage-0.1.0-py3-none-any.whl -d wheel_contents/
```

You’ll find files like:

- `mypackage/` — your package code
- `mypackage-0.1.0.dist-info/` — metadata files:

  * `METADATA`: project name, version, license, dependencies
  * `RECORD`: list of all files and checksums
  * `entry_points.txt`: for command-line interfaces (if defined)

### Inside a `.tar.gz` file

Source distributions can be extracted with:

```bash
tar -xvzf dist/mypackage-0.1.0.tar.gz
```

This will reveal your full source tree, including files like:

- `setup.cfg`, `pyproject.toml`, or `setup.py` (depending on build system)
- `src/`, `tests/`, and other top-level folders
- The full license and readme files

This is what users will receive if they choose to build your package from source.

### Validating the Package

Before publishing, use `twine` to validate the structure of your package:

```bash
pip install twine
twine check dist/*
```

This command verifies that your distributions have:

- Valid metadata
- A properly formatted `long_description`
- Required fields for PyPI upload

