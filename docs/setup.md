# Setup your package

## Options

Template generator will ask you to fill some variables.

### `project_name`

**Default:** `python_project`

[Check the availability of possible name](http://ivantomic.com/projects/ospnc/) before creating the project.
Make sure it is lowercase, no spaces, and uses `_` if desired.

### `project_description`

**Default:** based on the `project_name`

Brief description of your project.

### `organization`

**Default:** based on the `project_name`

Name of the organization. We need to generate LICENSE and to specify ownership in `pyproject.toml`.

### `license`

**Default:** `Apache-2.0`

One of `Apache-2.0`, `MIT`, `BSD-3-Clause` and `GPL-3.0-only`.

### `min_python_version`

**Default:** `3.9`

Minimum version of Python for this package.

### `dev_python_version`

**Default:** `3.12`

Python version used for local development.
It is used for specifying the conda environment.

### `git_host`

**Default:** `GitHub`

Which website will host the repository: `GitHub` or `GitLab`?

### `docs`

**Default:** `mkdocs`

Which documentation engine do you want to use: `mkdocs` or `sphinx`?

### `user_name`

**Default:** based on the `organization`

GitHub username for hosting.
Also used to set up `README.md`, `pyproject.toml` and template files for GitHub.

### `email`

**Default:** based on the `organization`

Email for `CODE_OF_CONDUCT.md` and to specify the ownership of the project in `pyproject.toml`.

### `line_length`

**Default:** 88

The max length per line (used for codestyle with `black` and `isort`). NOTE: This value must be between 50 and 300.
