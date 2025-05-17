import os
import tempfile

from cookiecutter.main import cookiecutter

REPO_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def test_template_gen():
    tmpdir = tempfile.TemporaryDirectory()
    cookiecutter(REPO_PATH, no_input=True, output_dir=tmpdir.name)
