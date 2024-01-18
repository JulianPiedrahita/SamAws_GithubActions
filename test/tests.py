import random
import pytest





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

