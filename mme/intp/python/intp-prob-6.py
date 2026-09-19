import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 0, 1, 0, 1])

cs = CubicSpline(x, y, bc_type='natural')
xs = np.linspace(0, 5, 200)

plt.scatter(x, y, color='red')
plt.plot(xs, cs(xs), label="Cubic Spline")
plt.legend()
plt.grid(True)
plt.show()
