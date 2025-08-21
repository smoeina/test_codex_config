"""Plotting utilities using matplotlib."""

from typing import Callable

def plot_function(func: Callable[[float], float], start: float, end: float, num_points: int = 100, filename: str | None = None):
    """Plot *func* over the interval [start, end].

    Args:
        func: Function to plot.
        start: Start of the interval.
        end: End of the interval.
        num_points: Number of points to sample.
        filename: If provided, the plot is saved to this file.
    Returns:
        The matplotlib figure object.

    Raises:
        ImportError: If ``matplotlib`` or ``numpy`` are not available.
    """
    if num_points <= 1:
        raise ValueError("num_points must be greater than 1")
    try:
        import numpy as np
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise ImportError("matplotlib and numpy are required for plotting") from exc

    x = np.linspace(start, end, num_points)
    y = [func(val) for val in x]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Function plot")
    if filename:
        fig.savefig(filename)
    return fig
