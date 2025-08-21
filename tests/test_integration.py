import math

from calculator import integrate


def test_integrate_linear():
    result = integrate(lambda x: x, 0, 1, n=1000)
    assert math.isclose(result, 0.5, rel_tol=1e-3)


def test_integrate_sine():
    result = integrate(math.sin, 0, math.pi, n=1000)
    assert math.isclose(result, 2.0, rel_tol=1e-3)
