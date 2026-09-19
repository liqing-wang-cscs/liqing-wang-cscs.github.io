import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

np.random.seed(0)
lam = np.linspace(400, 700, 60)
A_true = 0.8 * np.exp(-((lam - 520)**2) / (2 * 15**2)) + 0.1
A = A_true + np.random.normal(0, 0.02, lam.size)

def gauss(x, A0, mu, sigma, B):
    return A0 * np.exp(-((x - mu)**2) / (2 * sigma**2)) + B

popt, pcov = curve_fit(gauss, lam, A, p0=[0.8, 520, 15, 0.1])
A0, mu, sigma, B = popt
print(f"峰高 A0 = {A0:.4f}")
print(f"峰位 μ = {mu:.2f} nm")
print(f"峰宽 σ = {sigma:.2f} nm")
print(f"基线 B = {B:.4f}")

xs = np.linspace(400, 700, 400)
plt.scatter(lam, A, color='red', s=15, label='观测数据')
plt.plot(xs, gauss(xs, *popt), 'b-', label='高斯拟合')
plt.xlabel('波长 (nm)'); plt.ylabel('吸光度')
plt.title('光谱吸收峰高斯拟合')
plt.legend(); plt.grid(True)
plt.tight_layout(); plt.show()
