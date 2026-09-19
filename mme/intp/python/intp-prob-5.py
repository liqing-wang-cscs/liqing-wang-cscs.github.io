import numpy as np
import matplotlib.pyplot as plt

x = np.array([-5, -3, -1, 0, 1, 3, 5])
y = 1 / (1 + x**2)

xs = np.linspace(-5, 5, 200)
ys = np.interp(xs, x, y)

plt.plot(xs, ys, label="Piecewise Linear")
plt.scatter(x, y, color='red')
plt.legend()
plt.grid(True)
plt.show()
