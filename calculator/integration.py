"""Numerical integration utilities."""

from typing import Callable


def integrate(func: Callable[[float], float], a: float, b: float, n: int = 1000) -> float:
    """Approximate the definite integral of *func* from *a* to *b* using the trapezoidal rule.

    Args:
        func: Function to integrate.
        a: Lower bound.
        b: Upper bound.
        n: Number of subdivisions. More subdivisions yield a more accurate result.
    """
    if n <= 0:
        raise ValueError("n must be positive")

    h = (b - a) / n
    total = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        x = a + i * h
        total += func(x)
    return total * h
