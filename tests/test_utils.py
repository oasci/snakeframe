import pytest

from hooks.pre_gen_project import validate_line_length


def test_validate_line_length():
    with pytest.raises(ValueError):
        validate_line_length(1_000)

    with pytest.raises(ValueError):
        validate_line_length(-10)
