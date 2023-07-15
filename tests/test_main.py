import pytest

import librarytemplate
from librarytemplate.mod1 import adder


@pytest.fixture
def data():
    return 1


def test_dummy(data):
    assert data == 1


def test_adder():
    a, b = adder((0, 1), (0, 4))
    assert a == 0 and b == 5
