# Setup your package

## Options

Template generator will ask you to fill some variables.

`project_name` (**Default:** `python_project`)

> [Check the availability of possible name](http://ivantomic.com/projects/ospnc/) before creating the project.
> Make sure it is lowercase, no spaces, and uses `_` if desired.

`project_description` (**Default:** based on the `project_name`)

> Brief description of your project.

`organization` (**Default:** based on the `project_name`)

> Name of the organization. We need to generate LICENSE and to specify ownership in `pyproject.toml`.

`license` (**Default:** `MIT`)

> One of `MIT`, `BSD-3`, `GNU GPL v3.0` and `Apache Software License 2.0`.

`min_python_version` (**Default:** `3.9`)

> Minimal Python version.
> One of `3.9`, `3.10` and `3.11`.
> It is used for builds, GitHub workflow and formatters (`black`, `isort` and `pyupgrade`).

`dev_python_version` (**Default:** `3.11`)

> Python version used for local development.
> It is used for specifying the conda environment.

`user_name` (**Default:** based on the `organization`)

> GitHub username for hosting.
> Also used to set up `README.md`, `pyproject.toml` and template files for GitHub.

`email` (**Default:** based on the `organization`)

> Email for `CODE_OF_CONDUCT.md` and to specify the ownership of the project in `pyproject.toml`.

`line_length` (**Default:** 88)

> The max length per line (used for codestyle with `black` and `isort`). NOTE: This value must be between 50 and 300.

## Setup

### Initialize `poetry`

By running `make install`

After you create a project, it will appear in your directory, and will display [a message about how to initialize the project](https://github.com/oasci/snakeframe/tree/main/%7B%7B%20cookiecutter.project_name%20%7D%7D#very-first-steps).

### Initialize `pre-commit`

By running `make pre-commit-install`. Make sure to set up git first via `git init`.
