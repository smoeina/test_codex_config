"""Calculator package containing modules for algebra, integration, and plotting."""

from .algebra import add, subtract, multiply, divide, sin, cos, tan
from .integration import integrate
from .plotting import plot_function

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "sin",
    "cos",
    "tan",
    "integrate",
    "plot_function",
]
