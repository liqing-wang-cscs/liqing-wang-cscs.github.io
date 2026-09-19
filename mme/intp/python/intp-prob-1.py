import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x = np.array([0, 1, 2])
y = np.array([1, 2, 5])
poly = lagrange(x, y)
print(poly)  # 输出二次多项式系数

xs = np.linspace(-0.5, 2.5, 100)
plt.scatter(x, y, color='red')
plt.plot(xs, poly(xs))
plt.title("Lagrange Interpolation")
plt.grid(True)
plt.show()
