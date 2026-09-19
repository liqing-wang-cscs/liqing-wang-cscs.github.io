# 二维插值的一些例子

## 问11. 山地等高线与地面总面积

<details>
<summary>问题：</summary>
测得一块矩形山地的若干离散点海拔数据（单位：米），坐标范围 \(x\in[0,1000]\)、\(y\in[0,800]\)。要求：用二维插值方法生成该区域的海拔曲面，画出等高线图，并估算这块山地的地面总面积（即曲面面积，而非水平投影面积）。
</details>

<details>
<summary>解答：</summary>
这类问题属于散点数据的二维插值。思路是：先用 `scipy.interpolate.griddata` 把离散海拔点插值到规则网格上，得到高程函数 \(z=f(x,y)\)；再用 `matplotlib` 画等高线；最后用曲面面积公式估算地面总面积：
\[
S=\iint_D \sqrt{1+\left(\frac{\partial z}{\partial x}\right)^2+\left(\frac{\partial z}{\partial y}\right)^2}\,dx\,dy.
\]
数值上用网格上的差分近似偏导数，再对网格单元求和即可。

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

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
```
</details>

---

## 问12. 湖泊湖底地形与蓄水量

<details>
<summary>问题：</summary>
某湖泊水面高程为 0 m，测得湖区内若干点的水深（正值表示水深，单位：米），坐标范围 \(x\in[0,500]\)、\(y\in[0,400]\)。要求：用二维插值画出湖底地形图，并计算湖泊的总蓄水量。
</details>

<details>
<summary>解答：</summary>
蓄水量等于水深在湖面上的积分：
\[
V=\iint_D h(x,y)\,dx\,dy.
\]
做法与问1类似：先把离散水深点插值到规则网格，得到水深函数 \(h(x,y)\)；再用 `contourf` 画出湖底地形（水深越大颜色越深）；最后对网格用矩形法或梯形法求和得到体积。

```python
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
```

</details>

---

## 问题2-v2. 海底地形图

<details>
<summary>问题：</summary>
某海域测得水深数据如下，

| x_obs | 129 | 140 | 103.5 | 88 | 185.5 | 195 | 105 | 157.5 | 107.5 | 77 | 81 | 162 | 162 | 117.5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| y_obs | 7.5 | 141.5 | 23 | 147 | 22.5 | 137.5 | 85.5 | -6.5 | -81 | 3 | 56.5 | -66.5 | 84 | -33.5 |
| h_obs | 4 | 8 | 6 | 8 | 6 | 8 | 8 | 9 | 9 | 8 | 8 | 9 | 4 | 9 |

画出海底等高线图和地形图。
</details>

<details>
<summary>解答：</summary>

<img src='/mme/intp/python/intp-prob-12-v2-a.png'>

<img src='/mme/intp/python/intp-prob-12-v2-b.png'>

</details>

---

## 问13. 城市气温分布与“热岛”中心定位

<details>
<summary>问题：</summary>
某城市在若干气象站测得夏季某日 14:00 的气温（单位：℃），站点坐标覆盖 \(x\in[0,20]\) km、\(y\in[0,20]\) km。要求：用二维插值绘制城市气温分布图，找出气温最高点（热岛中心）的位置，并估算气温超过 35 ℃ 的区域面积。
</details>

<details>
<summary>解答：</summary>
这是一个有趣的二维插值应用：气温场往往是连续变化的，用插值可以得到比站点更精细的分布。做法是先用 `griddata` 插值到细网格，画等温线；再用 `np.argmax` 找到最高点坐标；最后统计温度大于 35 ℃ 的网格数乘以单元面积，得到高温区域面积。

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

np.random.seed(2)
n = 25
x_obs = np.random.uniform(0, 20, n)
y_obs = np.random.uniform(0, 20, n)
# 城市热岛：市中心 (10,10) 温度高，郊区低
T_obs = (38 - 0.15*np.sqrt((x_obs-10)**2 + (y_obs-10)**2)
         + np.random.normal(0, 0.3, n))

# 插值到细网格
xi = np.linspace(0, 20, 200)
yi = np.linspace(0, 20, 200)
Xi, Yi = np.meshgrid(xi, yi)
Ti = griddata((x_obs, y_obs), T_obs, (Xi, Yi), method='cubic')

# 画等温线图
plt.figure(figsize=(8, 6))
cf = plt.contourf(Xi, Yi, Ti, levels=20, cmap='hot_r')
plt.colorbar(cf, label='气温 (℃)')
plt.contour(Xi, Yi, Ti, levels=[30, 33, 35, 37], colors='k', linewidths=0.8)
plt.scatter(x_obs, y_obs, c='cyan', s=20, edgecolors='k', label='气象站')
plt.xlabel('x (km)'); plt.ylabel('y (km)')
plt.title('城市气温分布图')
plt.legend()
plt.tight_layout()
plt.show()

# 找热岛中心
idx = np.nanargmax(Ti)
print(f"热岛中心位置：({Xi.flat[idx]:.2f} km, {Yi.flat[idx]:.2f} km)，"
      f"最高气温 ≈ {Ti.flat[idx]:.2f} ℃")

# 估算气温超过 35 ℃ 的区域面积
dx = xi[1] - xi[0]
dy = yi[1] - yi[0]
hot_area = np.nansum(Ti > 35) * dx * dy
print(f"气温超过 35 ℃ 的区域面积 ≈ {hot_area:.2f} km²")
```
</details>

---

## 问14. 松江区地图

<details>
<summary>问题：</summary>
使用松江区 GeoJSON 文件，画出地图，计算面积，以及其它工作。

上海市区geojson地图文件： <https://gitcode.com/open-source-toolkit/fd5fe/blob/main/README.md>


</details>

<details>
<summary>解答：</summary>

```python
import geopandas as gpd
import matplotlib.pyplot as plt

# 中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 读取 GeoJSON
gdf = gpd.read_file('songjiangqu.json')
print("要素数：", len(gdf))
print("原始 CRS：", gdf.crs)  # GeoJSON 通常无 CRS，默认为 WGS84

# 2. 设定坐标系为 WGS84 经纬度
gdf = gdf.set_crs("EPSG:4326", allow_override=True)

# 3. 画图（经纬度下）
fig, ax = plt.subplots(figsize=(8, 6))
gdf.plot(ax=ax, facecolor='lightblue', edgecolor='black', linewidth=1.5)
ax.set_xlabel('经度'); ax.set_ylabel('纬度')
ax.set_title('区域边界')
ax.set_aspect('equal')   # 让形状不变形
plt.tight_layout()
plt.show()

# 4. 投影到 UTM 51N，计算面积
gdf_utm = gdf.to_crs("EPSG:32651")
area_m2 = gdf_utm.area.sum()
print(f"面积 ≈ {area_m2:.2f} 平方米")
print(f"面积 ≈ {area_m2/1e6:.4f} 平方公里")

# 可选：分别列出每个多边形的面积
for i, a in enumerate(gdf_utm.area):
    print(f"  多边形 {i}: {a:.2f} m²  ({a/1e6:.4f} km²)")

```

<img src='/mme/intp/python/intp-prob-14.png'>

</details>

---
