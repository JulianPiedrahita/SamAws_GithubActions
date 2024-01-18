import random
import pytest



@pytest.mark.xfail
def test_xfailed():
    assert random.random() == 1.0


@pytest.mark.xfail
def test_xpassed():
    assert 0.0 < random.random() < 1.0


@pytest.mark.skip(reason="don't run this test")
def test_skipped():
    assert "pytest-emoji" != ""


@pytest.fixture
def number():
    return 1234 / 0


def test_error(number):
    assert number == number