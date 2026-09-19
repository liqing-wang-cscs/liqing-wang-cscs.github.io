import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.array([5.764, 6.286, 6.759, 7.168, 7.408])
y = np.array([0.648, 1.202, 1.823, 2.526, 3.360])

# 构造设计矩阵 A，右端向量 b = -1
A = np.column_stack([x**2, x*y, y**2, x, y])
b = -np.ones_like(x)

# 最小二乘求解
coef, *_ = np.linalg.lstsq(A, b, rcond=None)
a1, a2, a3, a4, a5 = coef
print("椭圆系数：")
print(f"a1={a1:.6f}, a2={a2:.6f}, a3={a3:.6f}, a4={a4:.6f}, a5={a5:.6f}")

# 画轨道曲线
X, Y = np.meshgrid(np.linspace(5, 8, 400), np.linspace(0, 4, 400))
F = a1*X**2 + a2*X*Y + a3*Y**2 + a4*X + a5*Y + 1

plt.figure(figsize=(8, 5))
plt.contour(X, Y, F, levels=[0], colors='b')
plt.scatter(x, y, color='red', zorder=5, label='观测点')
plt.xlabel('x (天文单位)'); plt.ylabel('y (天文单位)')
plt.title('小行星轨道椭圆')
plt.legend(); plt.grid(True)
plt.tight_layout(); plt.show()
