import pytest

from func import my_sum

@pytest.fixture(scope="module")
def setUp():
    print("\t\tsetUp")
    return [my_sum(1, 2, 3, 4)]

def test_py_test(setUp):
    assert setUp[0] == -10