<h1 align="center">snakeframe</h1>

<h4 align="center">A cookiecutter template for accessible, reproducible Python packages</h4>

<h4 align="center" style="padding-bottom: 0.5em;"><a href="https://snakeframe.oasci.org">Documentation</a></h4>

<p align="center">
  <a href="https://github.com/psf/black" target="_blank">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Black style">
  </a>
  <a href="https://github.com/oasci/snakeframe/blob/main/.pre-commit-config.yaml" target="_blank">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="License">
  </a>
  <a href="https://github.com/oasci/snakeframe/releases" target="_blank">
    <img src="https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg" alt="License">
  </a>
  <a href="https://github.com/oasci/snakeframe/blob/main/LICENSE.md" target="_blank">
    <img src="https://img.shields.io/github/license/oasci/snakeframe" alt="License">
  </a>
</p>

## TL;DR

All you need is [cookiecutter][cookiecutter].

```bash
cookiecutter gh:oasci/snakeframe
```

## Features

In this [cookiecutter 🍪][cookiecutter] template we combine state-of-the-art libraries and best development practices for Python.

### Development

- Supports `Python 3.9` and higher.
- Seamless [`conda`][conda]+[`poetry`][poetry] dependencies manager with [conda][conda-lock] and [poetry][poetry-lock] files.
- Automatic codestyle with [`black`][black], [`isort`][isort], and [`pylint`][pylint].
- [`pre-commit`][pre-commit] hooks with code-formatting.
- Type checks with [`mypy`][mypy].
- Testing with [`pytest`][pytest].
- Ready-to-use [`.editorconfig`][.editorconfig] and [`.gitignore`][.gitignore].

### Deployment

- `GitHub` integration: issue and pull request templates.
- `Github Actions` with predefined [build workflow][build.yml] as the default CI/CD.
- Everything is already set up for code style checks, code formatting, testing, linting, etc. with [`Makefile`][makefile].
- Always up-to-date dependencies with [`@dependabot`][dependabot].
  You only need to [enable it][dependabot-configure].
- Automatic release notes with [`Release Drafter`][release drafter].
  You may see the list of labels in [`release-drafter.yml`][release-drafter.yml].
  Works perfectly with [Semantic Versions][semver] specification.

### Community

- [Pull Request][pr-template] and several [Issue][issue-template] templates.
- Files such as: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically.
- [`Stale action`][stale action] that closes abandoned issues after a period of inactivity.
- [`Sphinx`][sphinx] documentation automatically built with [deploy-docs.yml][docs.yml].
  You just need to activate pages and set source to `GitHub Actions`.

## Deploying

A note to maintainers.

We use [bump-my-version](https://github.com/callowayproject/bump-my-version) to release a new version.
This will create a git tag that is used by [poetry-dynamic-version](https://github.com/mtkennerly/poetry-dynamic-versioning) to generate version strings and update `CHANGELOG.md`.

For example, to bump the `minor` version you would run the following command.

```bash
poetry run bump-my-version bump minor
```

After releasing a new version, you need to push and include all tags.

```bash
git push --follow-tags
```

## License

Code contained in this project is released under the [MIT License](https://spdx.org/licenses/MIT.html) as specified in [`LICENSE.md`][snakeframe-license].
This license grants you the freedom to use, modify, and distribute it as long as you include the original copyright notice contained in [`LICENSE.md`][snakeframe-license] and the following disclaimer.

> Portions of this code were incorporated and adapted with permission from [snakeframe](https://github.com/oasci/snakeframe) by OASCI under the [MIT License](https://github.com/oasci/snakeframe/blob/main/LICENSE.md).

[snakeframe-license]: https://github.com/oasci/snakeframe/blob/main/LICENSE.md
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[poetry]: https://python-poetry.org/
[conda]: https://conda.org/
[conda-lock]: https://conda.github.io/conda-lock/
[poetry-lock]: https://python-poetry.org/docs/basic-usage/#installing-dependencies
[black]: https://github.com/psf/black
[isort]: https://github.com/PyCQA/isort
[pylint]: https://github.com/pylint-dev/pylint
[pre-commit]: https://github.com/pre-commit/pre-commit
[mypy]: https://github.com/python/mypy
[pytest]: https://docs.pytest.org/en/7.4.x/
[.editorconfig]: https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.editorconfig
[.gitignore]: https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.gitignore
[build.yml]: https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/workflows/build.yml
[makefile]: https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/Makefile
[dependabot]: https://github.com/dependabot
[dependabot-configure]: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#enabling-github-dependabot-version-updates
[release drafter]: https://github.com/marketplace/actions/release-drafter
[release-drafter.yml]: https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/workflows/release-drafter.yml
[semver]: https://semver.org/
[stale action]: https://github.com/actions/stale
[pr-template]: https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/PULL_REQUEST_TEMPLATE.md
[issue-template]: https://github.com/oasci/snakeframe/tree/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/ISSUE_TEMPLATE
[sphinx]: https://snakeframe.oasci.org/
[docs.yml]: https://github.com/oasci/snakeframe/blob/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/workflows/deploy-docs.yml
