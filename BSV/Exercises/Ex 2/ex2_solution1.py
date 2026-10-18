"""creating aLissajous-figure"""

# author: Clemens Loher
# date: 2026-10-09

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal

if __name__ == "__main__":
    # Assignment 2.1 Lissajous-figure

    t = np.linspace(0, 2 * np.pi, 1000)
    deltas = np.arange(0, 0.25, 0.01)
    for delta in deltas:
        x = np.sin(t) + delta
        y = np.sin(2 * t)
        plt.plot(x, y, lw=3, color=(0.3, 0, 1), alpha=(1 - 4 * delta) / 2)
    plt.axis("equal")
    plt.show()
