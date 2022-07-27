import pytest
from calc import add


@pytest.mark.parametrize("input_a,input_b,expected", [(3, 5, 8), (2, 4, 6), (6, 9, 15)])
def test_add(input_a, input_b, expected):
    assert add(input_a, input_b) == expected
