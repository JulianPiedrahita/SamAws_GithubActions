import random
import pytest


@pytest.mark.skip(reason="don't run this test")
def test_skipped():
    assert "pytest-emoji" != ""


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Sara", "Hello Sara!"),
        ("Mat", "Hello Mat!"),
        ("Annie", "Hello Annie!"),
    ],
)
def test_passed(name, expected):
    assert f"Hello {name}!" == expected


def test_error(number):
    assert number == number