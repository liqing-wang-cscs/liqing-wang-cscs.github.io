import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

np.random.seed(0)
x = np.linspace(-3, 3, 15)
y = np.sin(x) + np.random.normal(0, 0.2, len(x))
xs = np.linspace(-3, 3, 200)

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='k', label='数据')
for deg in [1, 3, 9]:
    coef = np.polyfit(x, y, deg)
    plt.plot(xs, np.polyval(coef, xs), label=f"阶数={deg}")
plt.ylim(-2, 2); plt.legend(); plt.grid(True)
plt.title("不同阶数多项式拟合对比")
plt.show()
