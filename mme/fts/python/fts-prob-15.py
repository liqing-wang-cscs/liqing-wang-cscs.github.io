import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.array([6, 2, 6, 7, 4, 2, 5, 9], dtype=float)
y = np.array([4, 9, 5, 3, 8, 5, 8, 2], dtype=float)
z = np.array([5, 2, 1, 9, 7, 4, 3, 3], dtype=float)

def model(X, a, b, c):
    x, y = X
    return a * np.exp(b * x) + c * y**2

# 初值：a=1, b=0.1, c=0.1
popt, pcov = curve_fit(model, (x, y), z, p0=[1.0, 0.1, 0.1], maxfev=20000)
a, b, c = popt
print(f"拟合结果：a = {a:.4f}, b = {b:.4f}, c = {c:.4f}")

z_hat = model((x, y), *popt)
rss = np.sum((z - z_hat) ** 2)
print(f"残差平方和 RSS = {rss:.4f}")

# 可视化：三维散点与拟合曲面
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, color='red', s=40, label='观测值')

Xg, Yg = np.meshgrid(np.linspace(1, 10, 40), np.linspace(1, 10, 40))
Zg = model((Xg, Yg), *popt)
ax.plot_surface(Xg, Yg, Zg, cmap='viridis', alpha=0.6)
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.set_title('r$z = ae^{bx} + cy^2$ 拟合曲面')
plt.tight_layout(); plt.show()