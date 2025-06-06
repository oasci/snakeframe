<h1 align="center">snakeframe</h1>

<h4 align="center">A cookiecutter template for accessible, reproducible Python packages</h4>

## TL;DR

All you need is [cookiecutter][cookiecutter].

```bash
cookiecutter gh:oasci/snakeframe
```

## Features

In this [cookiecutter 🍪][cookiecutter] template we combine state-of-the-art libraries and best development practices for Python.

### Development

-   Supports `Python 3.10` and higher.
-   Seamless [`conda`][conda] + [`pip`][pypi] dependencies manager with [`pixi`][pixi].
-   Automatic codestyle with [`ruff`][ruff] and [`isort`][isort].
-   Type checks with [`mypy`][mypy].
-   Testing with [`pytest`][pytest].
-   Ready-to-use [`.editorconfig`][.editorconfig] and [`.gitignore`][.gitignore].

### Deployment

-   Github Actions or GitLab pipelines.
-   Code style checks, code formatting, testing, linting, etc. already setup with [`pixi tasks`][pixi-tasks].
-   [`Sphinx`][sphinx] or [`MkDocs`][mkdocs] documentation.

### Community

-   [Pull Request][pr-template] and several [Issue][issue-template] templates.
-   Files such as: `LICENSE` and `CODE_OF_CONDUCT.md` are generated automatically.

## License

Code contained in this project is released under the [MIT License](https://spdx.org/licenses/MIT.html) as specified in [`LICENSE.md`][snakeframe-license].
This license grants you the freedom to use, modify, and distribute it as long as you include the original copyright notice contained in [`LICENSE.md`][snakeframe-license] and the following disclaimer.

> Portions of this code were incorporated and adapted with permission from [snakeframe](https://github.com/oasci/snakeframe) by OASCI under the [MIT License](https://github.com/oasci/snakeframe/blob/main/LICENSE.md).

[snakeframe-license]: https://github.com/oasci/snakeframe/blob/main/LICENSE.md
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[pypi]: https://pypi.org/
[conda]: https://conda.org/
[pixi]: https://pixi.sh/latest/
[ruff]: https://docs.astral.sh/ruff/
[isort]: https://github.com/PyCQA/isort
[pylint]: https://github.com/pylint-dev/pylint
[pre-commit]: https://github.com/pre-commit/pre-commit
[mypy]: https://github.com/python/mypy
[pytest]: https://docs.pytest.org/en/7.4.x/
[.editorconfig]: https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.editorconfig
[.gitignore]: https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.gitignore
[pixi-tasks]: https://pixi.sh/latest/workspace/advanced_tasks/
[mkdocs]: https://squidfunk.github.io/mkdocs-material/
[pr-template]: https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/PULL_REQUEST_TEMPLATE.md
[issue-template]: https://github.com/oasci/snakeframe/tree/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/ISSUE_TEMPLATE
[sphinx]: https://snakeframe.oasci.org/
