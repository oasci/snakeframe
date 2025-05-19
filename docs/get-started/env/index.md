# Environment Setup & Dependency Management

One of the most common sources of frustration in Python development—especially in collaborative or academic settings—is getting everyone’s environment to work the same way. Different Python versions, conflicting package versions, or mismatched dependencies can cause confusing bugs or failed installs.

This project template uses [Pixi](https://prefix.dev/docs/pixi/) to solve that problem.
Pixi is a modern tool for managing Python environments and dependencies. It provides fully isolated, reproducible environments that are fast to create and easy to share. Unlike `venv`, `pip`, or even `conda`, Pixi manages everything in a single, lockable configuration that works across operating systems and platforms—perfect for teams, research labs, or CI/CD pipelines.

## Creating a Reproducible Environment with Pixi

The first step in working with your project is to install its development environment. This ensures that your local setup matches what the project expects—including Python version, dependencies, linters, testing tools, and more.

### Step 1: Install Pixi

If you haven’t already installed Pixi, follow the instructions at [pixi.sh/latest/#installation](https://pixi.sh/latest/#installation). On Unix systems, the quick install looks like:

```bash
curl -sSL https://prefix.dev/install.sh | bash
```

Make sure the `pixi` command is available in your terminal before proceeding.

### Step 2: Install the Environment

Once you're inside the project directory, run:

```bash
pixi install
```

This reads the `pixi.toml` file and installs:

- The specific version of Python defined for development
- All declared dependencies (both runtime and dev)
- Any additional tools required for building, testing, or linting

Unlike `pip install -r requirements.txt`, which installs packages without enforcing versions consistently, `pixi install` uses a lockfile to guarantee the exact same versions are installed across systems. This ensures that what works for one contributor works for everyone.

### Step 3: Activate the Environment

To enter your environment and start working:

```bash
pixi shell
```

This activates the virtual environment managed by Pixi, giving you access to:

- Your exact Python interpreter (`python`, `python3`)
- Installed packages (e.g., `pytest`, `mkdocs`)
- All command-line tools available in the environment

Once inside the shell, you can run tests, serve documentation, or develop with confidence that your setup matches the project’s configuration.

## Managing Dependencies

As you develop new features, you may need to add, upgrade, or remove packages from the environment. Pixi makes this simple and safe.

### Adding a Dependency

To add a new package to your environment:

```bash
pixi add numpy
```

You can also specify a version constraint:

```bash
pixi add pandas@>=1.5,<2.0
```

This updates both the `pixi.toml` file (which lists your dependencies) and the lockfile (which pins exact versions for reproducibility).

> For runtime dependencies, make sure to also add the package to `pyproject.toml` under `[project.dependencies]` so it's included when building or distributing the package.

### Upgrading a Package

To upgrade a package to the latest compatible version:

```bash
pixi add package_name --update
```

Pixi resolves the new dependency graph and updates the lockfile accordingly.

### Removing a Package

To remove a package:

```bash
pixi remove package_name
```

This deletes it from the environment definition and lockfile.

## Lockfiles: Reproducibility for Teams and CI

Pixi automatically generates and maintains a `pixi.lock` file. This file records the exact versions of every package installed, including transitive dependencies.

Why this matters:

- Anyone who clones the repo and runs `pixi install` will get the exact same environment.
- CI pipelines and deployment environments will behave exactly as your local setup.
- Updates to packages are explicit and tracked in version control.

Just like `poetry.lock` or `package-lock.json` in JavaScript projects, the lockfile is a key part of reproducible development.

You should commit the `pixi.lock` file to version control. It ensures every contributor, server, and machine runs the same code under the same conditions.
