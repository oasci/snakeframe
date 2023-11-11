<h1 align="center">{{ cookiecutter.project_name }}</h1>

<h4 align="center">{{ cookiecutter.project_description }}</h4>

TODO: Add in information about {{ cookiecutter.project_name }}

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

Code contained in this project is released under the {{ cookiecutter.license }} License as specified in `LICENSE.md`.
This license grants you the freedom to use, modify, and distribute it as long as you include the original copyright notice contained in `LICENSE.md` and the following disclaimer.

> Portions of this code were incorporated and adapted with permission from {{ cookiecutter.project_name }} by {{ cookiecutter.github_name }} licensed under the {{ cookiecutter.license }} License.
