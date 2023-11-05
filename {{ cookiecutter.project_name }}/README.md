<h1 align="center">{{ cookiecutter.project_name }}</h1>

<h4 align="center">{{ cookiecutter.project_description }}</h4>

<h4 align="center" style="padding-bottom: 0.5em;"><a href="https://{{ cookiecutter.github_name }}.github.io/{{ cookiecutter.project_name }}">Documentation</a></h4>

<p align="center">
  <a href="https://github.com/psf/black" target="_blank">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Black style">
  </a>
  <a href="https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/.pre-commit-config.yaml" target="_blank">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="License">
  </a>
  <a href="https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/releases" target="_blank">
    <img src="https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg" alt="License">
  </a>
  <a href="https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/LICENSE.md" target="_blank">
    <img src="https://img.shields.io/github/license/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}" alt="License">
  </a>
</p>

TODO: Add in outline

## Deploying

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

Code contained in this project is released under the {{ cookiecutter.license }} License as specified in [`LICENSE.md`][license].
This license grants you the freedom to use, modify, and distribute it as long as you include the original copyright notice contained in [`LICENSE.md`][license] and the following disclaimer.

> Portions of this code were incorporated and adapted with permission from [{{ cookiecutter.project_name }}](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}) by {{ cookiecutter.github_name }} licensed under the [MIT License](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/LICENSE.md).

[license]: https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/LICENSE.md
