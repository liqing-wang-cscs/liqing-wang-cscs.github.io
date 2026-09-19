import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

t = np.array([3, 6, 9, 12, 15, 18, 21, 24], dtype=float)
y = np.array([57.6, 41.9, 31.0, 22.7, 16.6, 12.2, 8.9, 6.5])

# (a) 对数线性化估初值
B, A = np.polyfit(t, np.log(y), 1)
m0, k0 = B, np.exp(A)
print(f"初值估计：k0 = {k0:.4f}, m0 = {m0:.6f}")

# (b) 非线性拟合
def model(t, k, m):
    return k * np.exp(m * t)

popt, pcov = curve_fit(model, t, y, p0=[k0, m0])
k, m = popt
print(f"非线性拟合：k = {k:.4f}, m = {m:.6f}")
print(f"t = 5.8 时，y 预测值 = {model(5.8, k, m):.4f}")

ts = np.linspace(2, 25, 200)
plt.scatter(t, y, color='red', label='观测值')
plt.plot(ts, model(ts, k, m), 'b-', label=f'y={k:.2f}e^({m:.4f}t)')
plt.axvline(5.8, color='gray', linestyle='--', alpha=0.6)
plt.xlabel('时间 t'); plt.ylabel('反应物量 y')
plt.title('单分子化学反应速度拟合')
plt.legend(); plt.grid(True)
plt.tight_layout(); plt.show()