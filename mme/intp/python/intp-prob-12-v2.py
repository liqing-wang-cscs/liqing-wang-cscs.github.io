import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# ========== 中文字体配置 ==========
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取文件，按行拆分，每行再按 tab 拆分
with open('data-12.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

x_obs = np.array(lines[0].split('\t'), dtype=float)
y_obs = np.array(lines[1].split('\t'), dtype=float)
h_obs = np.array(lines[2].split('\t'), dtype=float)
h_obs = -h_obs

xmin=np.min(x_obs)
xmax=np.max(x_obs)
ymin=np.min(y_obs)
ymax=np.max(y_obs)
hmin=np.min(h_obs)
hmax=np.max(h_obs)

# 插值到规则网格
xi = np.linspace(xmin, xmax, 100)
yi = np.linspace(ymin, ymax, 100)
Xi, Yi = np.meshgrid(xi, yi)
Hi = griddata((x_obs, y_obs), h_obs, (Xi, Yi), method='cubic')
# Hi = np.where(Hi > 0, 0, Hi)  # 水平面以上截断为 0

# 画湖底地形图（水深越大颜色越深）
plt.figure(figsize=(8, 6))
cf = plt.contourf(Xi, Yi, Hi, levels=20, cmap='ocean')
plt.colorbar(cf, label='水深 (m)')
plt.contour(Xi, Yi, Hi, levels=10, colors='k', linewidths=0.4)
plt.scatter(x_obs, y_obs, c='r', s=8, label='测深点')
plt.xlabel('x (m)'); plt.ylabel('y (m)')
plt.title('海底等高线')
plt.legend()
plt.tight_layout()
plt.show()

# 计算蓄水量：矩形法积分
dx = xi[1] - xi[0]
dy = yi[1] - yi[0]
V = np.nansum(Hi) * dx * dy
print(f"湖泊总蓄水量 ≈ {V:.0f} m³")

#------------ 画出海底地形曲面图 ----------------

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(Xi, Yi, Hi, cmap='ocean', #cmap='terrain/ocean/Blues/Blues-r'
                       edgecolor='none', alpha=0.95,
                       rstride=1, cstride=1)
fig.colorbar(surf, ax=ax, shrink=0.6, label='水深 (m)')

# ---- 关键：按实际尺度设置坐标轴 ----
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

# 真实比例（长宽真实，深度有缩放）
ax.set_box_aspect((xmax-xmin, ymax-ymin, (hmax-hmin)*10))

ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('水深 (m)')
ax.set_title('海底地形曲面图')
ax.view_init(elev=25, azim=-60)

plt.tight_layout()
plt.show()
