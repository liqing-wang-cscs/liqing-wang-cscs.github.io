import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicHermiteSpline

x = np.array([0, 1, 2])
y = np.array([0, 2, 1])
dydx = np.array([1, 0, 1])

spline = CubicHermiteSpline(x, y, dydx)
xs = np.linspace(0, 2, 200)

plt.scatter(x, y, color='red')
plt.plot(xs, spline(xs), label="Hermite Interpolation")
plt.legend()
plt.grid(True)
plt.show()
