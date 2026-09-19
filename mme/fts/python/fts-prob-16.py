import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 模拟某地区人口数据（万人）
year = np.array([2000, 2003, 2006, 2009, 2012, 2015, 2018, 2020], dtype=float)
pop = np.array([1250, 1330, 1415, 1500, 1585, 1660, 1710, 1730], dtype=float)
t = year - year[0]

def model(t, P0, r):
    return P0 * np.exp(r * t)

popt, pcov = curve_fit(model, t, pop, p0=[1250, 0.02])
P0, r = popt
print(f"拟合：P0 = {P0:.2f} 万人, 年增长率 r = {r:.4%}")

t_pred = 2025 - year[0]
print(f"2025 年预测人口 ≈ {model(t_pred, P0, r):.1f} 万人")

ts = np.linspace(0, 25, 200)
plt.scatter(year, pop, color='red', label='实际数据')
plt.plot(year[0] + ts, model(ts, P0, r), 'b-', label='指数拟合')
plt.axvline(2025, color='gray', linestyle='--', alpha=0.6)
plt.xlabel('年份'); plt.ylabel('人口 (万人)')
plt.title('人口指数增长拟合')
plt.legend(); plt.grid(True)
plt.tight_layout(); plt.show()