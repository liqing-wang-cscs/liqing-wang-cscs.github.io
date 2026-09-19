import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# ========== 中文字体配置 ==========
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False    

# 1. 模拟一些离散海拔观测点
np.random.seed(0)
n = 60
x_obs = np.random.uniform(0, 1000, n)
y_obs = np.random.uniform(0, 800, n)
# 造一个山地地形：两个山峰 + 一个缓坡
z_obs = (300*np.exp(-((x_obs-300)**2+(y_obs-300)**2)/200**2)
         + 450*np.exp(-((x_obs-750)**2+(y_obs-550)**2)/150**2)
         + 0.05*x_obs + 0.03*y_obs)

# 2. 插值到规则网格
xi = np.linspace(0, 1000, 100)
yi = np.linspace(0, 800, 80)
Xi, Yi = np.meshgrid(xi, yi)
Zi = griddata((x_obs, y_obs), z_obs, (Xi, Yi), method='cubic')

# 3. 画等高线
plt.figure(figsize=(8, 6))
cs = plt.contour(Xi, Yi, Zi, levels=15, cmap='terrain')
plt.clabel(cs, inline=True, fontsize=8)
plt.scatter(x_obs, y_obs, c='k', s=8, label='观测点')
plt.colorbar(cs, label='海拔 (m)')
plt.xlabel('x (m)'); plt.ylabel('y (m)')
plt.title('山地等高线图')
plt.legend()
plt.tight_layout()
plt.show()

# 4. 计算曲面面积
dx = xi[1] - xi[0]
dy = yi[1] - yi[0]
dzdx, dzdy = np.gradient(Zi, dy, dx)
dS = np.sqrt(1 + dzdx**2 + dzdy**2) * dx * dy
area = np.nansum(dS)
print(f"山地地面总面积 ≈ {area:.1f} m²")
print(f"水平投影面积 = {1000*800} m²")
