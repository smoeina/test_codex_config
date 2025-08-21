import pytest

try:
    import matplotlib
    matplotlib.use("Agg")  # Use non-interactive backend for tests
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    plt = None

from calculator import plot_function


@pytest.mark.skipif(not MATPLOTLIB_AVAILABLE, reason="matplotlib not installed")
def test_plot_function_returns_figure():
    fig = plot_function(lambda x: x ** 2, 0, 1, num_points=10)
    assert fig.axes
    ax = fig.axes[0]
    line = ax.lines[0]
    x_data = line.get_xdata()
    y_data = line.get_ydata()
    assert x_data[0] == 0 and x_data[-1] == 1
    assert y_data[0] == 0 and y_data[-1] == 1
    plt.close(fig)
