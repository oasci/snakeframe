SHELL := /usr/bin/env bash
PYTHON_VERSION := {{ cookiecutter.dev_python_version }}
PYTHON_VERSION_CONDENSED := {{ cookiecutter.condensed_dev_python_version }}
PACKAGE_NAME := {{ cookiecutter.project_name }}
REPO_PATH := $(shell git rev-parse --show-toplevel)
PACKAGE_PATH := $(REPO_PATH)/$(PACKAGE_NAME)
TESTS_PATH := $(REPO_PATH)/tests
CONDA_NAME := $(PACKAGE_NAME)-dev
CONDA := conda run -n $(CONDA_NAME)
DOCS_URL := https://{{ cookiecutter.github_name }}.github.io/{{ cookiecutter.project_name }}



###   ENVIRONMENT   ###

.PHONY: conda-setup
conda-setup:
	- conda deactivate
	conda remove -y -n $(CONDA_NAME) --all
	conda create -y -n $(CONDA_NAME) python=$(PYTHON_VERSION)
	conda install -y conda-lock -n $(CONDA_NAME)
	conda install -y -c conda-forge poetry pre-commit tomli tomli-w -n $(CONDA_NAME)
	$(CONDA) pip install conda_poetry_liaison

.PHONY: write-conda-lock
write-conda-lock:
	- rm $(REPO_PATH)/conda-lock.yml
	$(CONDA) conda env export --from-history | grep -v "^prefix" > environment.yml
	$(CONDA) conda-lock -f environment.yml -p linux-64 -p osx-64 -p win-64
	$(CONDA) cpl-deps $(REPO_PATH)/pyproject.toml --env_name $(CONDA_NAME)
	$(CONDA) cpl-clean --env_name $(CONDA_NAME)

.PHONY: from-conda-lock
from-conda-lock:
	$(CONDA) conda-lock install -n $(CONDA_NAME) $(REPO_PATH)/conda-lock.yml
	$(CONDA) pip install conda_poetry_liaison
	$(CONDA) cpl-clean --env_name $(CONDA_NAME)

.PHONY: pre-commit-install
pre-commit-install:
	$(CONDA) pre-commit install

# Reads `pyproject.toml`, solves environment, then writes lock file.
.PHONY: poetry-lock
poetry-lock:
	$(CONDA) poetry lock --no-interaction
	$(CONDA) poetry export --without-hashes > requirements.txt

.PHONY: install
install:
	$(CONDA) poetry install --no-interaction
	- mkdir .mypy_cache
	- $(CONDA) poetry run mypy --install-types --non-interactive --explicit-package-bases $(PACKAGE_NAME)

.PHONY: refresh
refresh: conda-setup from-conda-lock pre-commit-install install



###   FORMATTING   ###

.PHONY: validate
validate:
	- $(CONDA) pre-commit run --all-files

.PHONY: formatting
formatting:
	- $(CONDA) isort --settings-path pyproject.toml ./
	- $(CONDA) black --config pyproject.toml ./




###   LINTING   ###


.PHONY: test
test:
	$(CONDA) pytest -c pyproject.toml --cov=$(PACKAGE_PATH) --cov-report=xml $(TESTS_PATH)

.PHONY: check-codestyle
check-codestyle:
	$(CONDA) isort --diff --check-only $(PACKAGE_PATH)
	$(CONDA) black --diff --check --config pyproject.toml $(PACKAGE_PATH)
	- $(CONDA) pylint --rcfile pyproject.toml $(PACKAGE_PATH)

.PHONY: mypy
mypy:
	-$(CONDA) mypy --config-file pyproject.toml $(PACKAGE_PATH)

.PHONY: lint
lint: check-codestyle mypy



###   CLEANING   ###

.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: dsstore-remove
dsstore-remove:
	find . | grep -E ".DS_Store" | xargs rm -rf

.PHONY: mypycache-remove
mypycache-remove:
	find . | grep -E ".mypy_cache" | xargs rm -rf

.PHONY: ipynbcheckpoints-remove
ipynbcheckpoints-remove:
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf

.PHONY: pytestcache-remove
pytestcache-remove:
	find . | grep -E ".pytest_cache" | xargs rm -rf

.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: cleanup
cleanup: pycache-remove dsstore-remove mypycache-remove ipynbcheckpoints-remove pytestcache-remove



###   BUILDING   ###

.PHONY: build
build:
	$(CONDA) poetry build


###   DOCS   ###

.PHONY: docs
docs:
	rm -rf ./docs/html/
	$(CONDA) sphinx-build -nT ./docs/source/ ./docs/html/
	touch ./docs/html/.nojekyll

.PHONY: docs-versioned
docs-versioned:
	rm -rf ./docs/html/
	$(CONDA) sphinx-multiversion -nT ./docs/source/ ./docs/html/
	touch ./docs/html/.nojekyll

	# Create html redirect to main
	echo "<head>" > ./docs/html/index.html
	echo "  <meta http-equiv='refresh' content='0; URL=$(DOCS_URL)/main/index.html'>" >> ./docs/html/index.html
	echo "</head>" >> ./docs/html/index.html

.PHONY: open-docs
open-docs:
	xdg-open ./docs/html/index.html 2>/dev/null