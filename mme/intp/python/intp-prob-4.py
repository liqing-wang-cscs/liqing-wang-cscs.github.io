import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

f = lambda x: 1 / (1 + 25 * x**2)

for n in [5, 10, 15]:
    x = np.linspace(-1, 1, n+1)
    y = f(x)
    poly = lagrange(x, y)
    xs = np.linspace(-1, 1, 400)
    plt.plot(xs, poly(xs), label=f"n={n}")

plt.plot(xs, f(xs), 'k--', label="f(x)")
plt.ylim(-1, 2)
plt.legend()
plt.title("Runge Phenomenon")
plt.grid(True)
plt.show()
