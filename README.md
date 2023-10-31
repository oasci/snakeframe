<h1 align="center">snakeframe</h1>

<h4 align="center">A cookiecutter template for accessible, reproducible Python packages</h4>

<div align="center">

[![Build status](https://github.com/oasci/snakeframe/workflows/build/badge.svg?branch=main&event=push)](https://github.com/oasci/snakeframe/actions?query=workflow%3Abuild)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/oasci/snakeframe/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/oasci/snakeframe)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/oasci/snakeframe/blob/main/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/oasci/snakeframe/releases)
[![License](https://img.shields.io/github/license/oasci/snakeframe)](https://github.com/oasci/snakeframe/blob/main/LICENSE)
![Coverage Report](assets/images/coverage.svg)

</div>

## TL;DR

```bash
cookiecutter gh:oasci/snakeframe
```

> All you need is the latest version of cookiecutter

## Features

In this [cookiecutter 🍪](https://github.com/cookiecutter/cookiecutter) template we combine state-of-the-art libraries and best development practices for Python.

### Development features

- Supports `Python 3.9` and higher.
- [`Poetry`](https://python-poetry.org/) as a dependencies manager. See configuration in [`pyproject.toml`](https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/pyproject.toml) and [`setup.cfg`](https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/setup.cfg).
- Automatic codestyle with [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort) and [`pyupgrade`](https://github.com/asottile/pyupgrade).
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with code-formatting.
- Type checks with [`mypy`](https://mypy.readthedocs.io); docstring checks with [`pylint`](https://pylint.readthedocs.io/en/latest/); security checks with [`safety`](https://github.com/pyupio/safety) and [`bandit`](https://github.com/PyCQA/bandit)
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).
- Ready-to-use [`.editorconfig`](https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.editorconfig) and [`.gitignore`](https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.gitignore).

### Deployment features

- `GitHub` integration: issue and pr templates.
- `Github Actions` with predefined [build workflow](https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name.lower().replace('%20'%2C%20'_').replace('-'%2C%20'_')%20%7D%7D/.github/workflows/build.yml) as the default CI/CD.
- Everything is already set up for security checks, code style checks, code formatting, testing, linting, etc with [`Makefile`](https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name.lower().replace('%20'%2C%20'_').replace('-'%2C%20'_')%20%7D%7D/Makefile). More details in [makefile-usage](#makefile-usage).
- Always up-to-date dependencies with [`@dependabot`](https://github.com/dependabot).
  You only need to [enable it](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates).
- Automatic release notes with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). You may see the list of labels in [`release-drafter.yml`](https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name.lower().replace('%20'%2C%20'_').replace('-'%2C%20'_')%20%7D%7D/.github/workflows/release-drafter.yml).
  Works perfectly with [Semantic Versions](https://semver.org/) specification.

### Open source community features

- Ready-to-use [Pull Requests templates](https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/PULL_REQUEST_TEMPLATE.md) and several [Issue templates](https://github.com/oasci/snakeframe/tree/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/ISSUE_TEMPLATE).
- Files such as: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically.
- [`Stale bot`](https://github.com/apps/stale) that closes abandoned issues after a period of inactivity. (You will only [need to setup free plan](https://github.com/marketplace/stale)). Configuration is [here](https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/.stale.yml).
- [Semantic Versions](https://semver.org/) specification with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter).

## How to use it

### Installation

To begin using the template consider updating `cookiecutter`

```bash
pip install -U cookiecutter
```

then go to a directory where you want to create your project and run:

```bash
cookiecutter gh:oasci/snakeframe
```

### Input variables

Template generator will ask you to fill some variables.

The input variables, with their default values:

|     **Parameter**     |      **Default value**      | **Description**                                                                                                                                                               |
|:---------------------:|:---------------------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project_name`           | `python_project`            | [Check the availability of possible name](http://ivantomic.com/projects/ospnc/) before creating the project. Make sure it is lowercase, no spaces, and uses `_` if desired. |
| `project_description`    | based on the `project_name` | Brief description of your project. |
| `organization`           | based on the `project_name` | Name of the organization. We need to generate LICENCE and to specify ownership in `pyproject.toml`. |
| `license`                | `MIT`                       | One of `MIT`, `BSD-3`, `GNU GPL v3.0` and `Apache Software License 2.0`. |
| `minimal_python_version` | `3.11`                       | Minimal Python version. One of `3.9`, `3.10` and `3.11`. It is used for builds, GitHub workflow and formatters (`black`, `isort` and `pyupgrade`). |
| `github_name`            | based on the `organization` | GitHub username for hosting. Also used to set up `README.md`, `pyproject.toml` and template files for GitHub. |
| `email`                  | based on the `organization` | Email for `CODE_OF_CONDUCT.md` and to specify the ownership of the project in `pyproject.toml`. |
| `version`                | `0.1.0`                     | Initial version of the package. Make sure it follows the [Semantic Versions](https://semver.org/) specification. |
| `line_length`            | 88                         | The max length per line (used for codestyle with `black` and `isort`). NOTE: This value must be between 50 and 300. |
| `create_example_template` | `cli`                      | If `cli` is chosen generator will create simple CLI application with [`Typer`](https://github.com/tiangolo/typer) and [`Rich`](https://github.com/willmcgugan/rich) libraries. One of `cli`, `none` |

### Initial set up

#### Initialize `poetry`

By running `make install`

After you create a project, it will appear in your directory, and will display [a message about how to initialize the project](https://github.com/oasci/snakeframe/tree/main/%7B%7B%20cookiecutter.project_name%20%7D%7D#very-first-steps).

#### Initialize `pre-commit`

By running `make pre-commit-install`. Make sure to set up git first via `git init`.

### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions](https://semver.org/) standard.
- Make a commit to `GitHub`.
- Create a `GitHub release`.
- And... publish `poetry publish --build`

### Makefile usage

[`Makefile`](https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/Makefile) contains a lot of functions for faster development.

<details>
<summary>1. Setup conda</summary>
<p>

```bash
make conda-setup
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks could be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `isort` and `black`.

```bash
make formatting
```

</p>
</details>

<details>
<summary>4. Type checks</summary>
<p>

Run `mypy` static type checker

```bash
make mypy
```

</p>
</details>

<details>
<summary>5. Tests with coverage badges</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>6. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint
```

the same as:

```bash
make test && make check-codestyle && make mypy && make check-safety
```

</p>
</details>

<details>
<summary>7. Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypycache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/oasci/snakeframe/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter).
As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready.
With the categories option, you can categorize pull requests in release notes using labels.

## ![shield](assets/shield.svg) License

Code contained in this project is released under the [MIT License](https://spdx.org/licenses/MIT.html) as specified in [`LICENSE.md`](https://github.com/oasci/snakeframe/blob/main/LICENSE.md).
This license grants you the freedom to use, modify, and distribute it as long as you include the original copyright notice contained in [`LICENSE.md`](https://github.com/oasci/snakeframe/blob/main/LICENSE.md) and the following disclaimer.

> Portions of this code were incorporated and adapted with permission from [snakeframe](https://github.com/oasci/snakeframe) by OASCI licensed under the [MIT License](https://github.com/oasci/snakeframe/blob/main/LICENSE.md).
