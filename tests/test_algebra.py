import math

import pytest

from calculator import add, subtract, multiply, divide, sin, cos, tan


def test_basic_operations():
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    assert multiply(4, 3) == 12
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_trigonometry():
    assert math.isclose(sin(math.pi / 2), 1.0, rel_tol=1e-9)
    assert math.isclose(cos(0), 1.0, rel_tol=1e-9)
    assert math.isclose(tan(0), 0.0, rel_tol=1e-9)
