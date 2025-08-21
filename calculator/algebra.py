"""Algebra and trigonometry operations."""

import math

def add(a: float, b: float) -> float:
    """Return the sum of *a* and *b*."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference of *a* and *b*."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of *a* and *b*."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return *a* divided by *b*.

    Raises:
        ValueError: If *b* is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is undefined")
    return a / b

def sin(x: float) -> float:
    """Return the sine of *x* (in radians)."""
    return math.sin(x)

def cos(x: float) -> float:
    """Return the cosine of *x* (in radians)."""
    return math.cos(x)

def tan(x: float) -> float:
    """Return the tangent of *x* (in radians)."""
    return math.tan(x)
