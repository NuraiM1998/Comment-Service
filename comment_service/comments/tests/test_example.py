import pytest

def sum(a, b):
    return a + b


@pytest.mark.parametrize('input, expected', [
    ((1, 2), 3),
    ((1, 1), 2),
    ((1, 0), 1),
])
def test_sum(input, expected):
    assert sum(*input) == expected