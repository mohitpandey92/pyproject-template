from {{ cookiecutter.project_name }}.main import *


def test_add():
    assert add_one(2) == 3
