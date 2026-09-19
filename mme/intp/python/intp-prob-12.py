import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# ========== 中文字体配置 ==========
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

np.random.seed(1)
n = 50
x_obs = np.random.uniform(0, 500, n)
y_obs = np.random.uniform(0, 400, n)
# 造一个碗状湖底：中心深、边缘浅
h_obs = 20 * np.exp(-(((x_obs-250)**2)/150**2 + ((y_obs-200)**2)/120**2))
h_obs += np.random.normal(0, 0.3, n)  # 少量测量噪声

# 插值到规则网格
xi = np.linspace(0, 500, 120)
yi = np.linspace(0, 400, 100)
Xi, Yi = np.meshgrid(xi, yi)
Hi = griddata((x_obs, y_obs), h_obs, (Xi, Yi), method='cubic')
Hi = np.where(Hi < 0, 0, Hi)  # 负水深截断为 0

# 画湖底地形图（水深越大颜色越深）
plt.figure(figsize=(8, 6))
cf = plt.contourf(Xi, Yi, Hi, levels=20, cmap='Blues')
plt.colorbar(cf, label='水深 (m)')
plt.contour(Xi, Yi, Hi, levels=10, colors='k', linewidths=0.4)
plt.scatter(x_obs, y_obs, c='r', s=8, label='测深点')
plt.xlabel('x (m)'); plt.ylabel('y (m)')
plt.title('湖底地形图')
plt.legend()
plt.tight_layout()
plt.show()

# 计算蓄水量：矩形法积分
dx = xi[1] - xi[0]
dy = yi[1] - yi[0]
V = np.nansum(Hi) * dx * dy
print(f"湖泊总蓄水量 ≈ {V:.0f} m³")