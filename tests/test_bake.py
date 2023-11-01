import os
import shutil

import pytest
from cookiecutter.main import cookiecutter

REPO_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
TMP_DIR = "./tests/tmp/"
BAKE_DIR = os.path.join(TMP_DIR, "python_project")


@pytest.mark.order(0)
def test_template_gen():
    if os.path.exists(BAKE_DIR):
        shutil.rmtree(BAKE_DIR)
    cookiecutter(REPO_PATH, no_input=True, output_dir=TMP_DIR)
