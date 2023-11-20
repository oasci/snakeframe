<h1 align="center">{{ cookiecutter.project_name }}</h1>

<h4 align="center">{{ cookiecutter.project_description }}</h4>

Add in information about {{ cookiecutter.project_name }} here.

## Setup instructions

Here are some quick instructions to setup your Python project.
You can remove or modify this section once you start working.

1.  Initialize the git repository.

    ```bash
    git init
    ```

1.  Make sure you have conda and GNU make installed.
1.  Setup your conda environment.

    ```bash
    make conda-create conda-setup
    ```

1.  Change the `conda-dependencies` command in `Makefile` if you have any conda-only packages to install.
    If a package is available with `pip`, we recommend managing it with poetry.

1.  Install all conda dependencies.

    ```bash
    make conda-dependencies
    ```

1.  Create the conda lock file.

    ```bash
    make conda-lock
    ```

1.  Install pre-commit hooks.

    ```bash
    make pre-commit-install
    ```

1.  (Optional) Activate the conda environment.

    ```bash
    conda activate {{ cookiecutter.project_name }}-dev
    ```

1.  (Optional) Install any `PyPI` packages with the `poetry add` command.

1.  Create the poetry lock file.

    ```bash
    make poetry-lock
    ```

1.  Install your package.

    ```bash
    make install
    ```

1.  Add a `DOCS_URL` variable to the `Makefile`.
    For example, if this is GitHub project, you could use:

    ```text
    DOCS_URL := https://{{ cookiecutter.user_name }}.github.io/{{ cookiecutter.project_name }}
    ```

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

This project is released under the {{ cookiecutter.license }} License as specified in `LICENSE.md`.
