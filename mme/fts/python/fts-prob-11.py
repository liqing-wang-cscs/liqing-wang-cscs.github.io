import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

t = np.array([0, 1, 2, 3, 4, 5, 6, 7], dtype=float)
y = np.array([27.0, 26.8, 26.5, 26.3, 26.1, 25.7, 25.3, 24.8])

# 最小二乘拟合 y = a t + b
a, b = np.polyfit(t, y, 1)
print(f"拟合结果：y = {a:.4f} t + {b:.4f}")

y_hat = a * t + b
rss = np.sum((y - y_hat)**2)
r2 = 1 - rss / np.sum((y - y.mean())**2)
print(f"残差平方和 RSS = {rss:.5f}, 决定系数 R² = {r2:.5f}")

plt.scatter(t, y, color='red', label='观测值')
plt.plot(t, y_hat, 'b-', label=f'拟合: y={a:.3f}t+{b:.3f}')
plt.xlabel('时间 t (h)'); plt.ylabel('刀具厚度 y')
plt.title('刀具磨损速度拟合')
plt.legend(); plt.grid(True)
plt.tight_layout(); plt.show()
