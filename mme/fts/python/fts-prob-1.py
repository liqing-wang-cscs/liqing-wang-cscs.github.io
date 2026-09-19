import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 造一组带噪声的数据
np.random.seed(0)
x = np.linspace(0, 10, 20)
y = 2.5 * x + 1.0 + np.random.normal(0, 2, 20)

# 最小二乘拟合直线
a, b = np.polyfit(x, y, 1)
print(f"拟合直线：y = {a:.3f}x + {b:.3f}")

plt.scatter(x, y, label="数据点")
plt.plot(x, a*x + b, 'r', label="最小二乘拟合")
plt.legend(); plt.grid(True)
plt.title("最小二乘拟合直线")
plt.show()
