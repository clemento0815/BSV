



import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 20, 0.1)
np.pi
freq = 0.5
omega = 2 * np.pi * freq
x = np.sin(omega*t)
plt.plot(t, x)
plt.plot(t, x*x**2)
A_mat = np.array([[1,2],[3,4]])
