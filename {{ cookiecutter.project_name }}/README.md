<h1 align="center">{{ cookiecutter.project_name }}</h1>

<h4 align="center">{{ cookiecutter.project_description }}</h4>

Add information about {{ cookiecutter.project_name }} here.

## Installation

Clone the [repository](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}):

```bash
git clone git@{{ cookiecutter.git_host.lower() }}.com:{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}.git
```

Install `{{ cookiecutter.project_name }}` using `pip` after moving into the directory.

```sh
pip install .
```

This will install all dependencies and `{{ cookiecutter.project_name }}` into your current Python environment.

## Development

We use [pixi](https://pixi.sh/latest/) to manage Python environments and simplify the developer workflow.
Once you have [pixi](https://pixi.sh/latest/) installed, move into `{{ cookiecutter.project_name }}` directory (e.g., `cd {{ cookiecutter.project_name }}`) and install the environment using the command

```bash
pixi install
```

Now you can activate the new virtual environment using

```sh
pixi shell
```

## License

This project is released under the {{ cookiecutter.license }} License as specified in `LICENSE.md`.
