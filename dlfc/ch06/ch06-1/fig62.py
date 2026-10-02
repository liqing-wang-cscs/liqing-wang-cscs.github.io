import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import matplotlib.patches as patches

# 设置中文字体（可选）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

# 1. 加载数据（仅使用 sepal length 和 sepal width）
iris = load_iris()
X = iris.data[:, [0, 1]]  # sepal length (col 0), sepal width (col 1)
y = iris.target           # 0: setosa, 1: versicolor, 2: virginica
species_names = iris.target_names

# 2. 定义网格划分：4×4 网格
# 根据图中分布，合理设置边界（观察图：x轴约 4.5~8.0，y轴约 2.0~4.5）
x_min, x_max = X[:, 0].min() - 0.2, X[:, 0].max() + 0.2
y_min, y_max = X[:, 1].min() - 0.2, X[:, 1].max() + 0.2

nx, ny = 4, 4  # 4×4 网格
x_bins = np.linspace(x_min, x_max, nx + 1)
y_bins = np.linspace(y_min, y_max, ny + 1)

# 3. 为每个网格单元分配“主导类别”（即该单元内样本最多的类别）
cell_labels = np.full((ny, nx), -1, dtype=int)  # shape: (4 rows, 4 cols)
cell_counts = np.zeros((ny, nx, 3), dtype=int)  # 计数：[row, col, class]

for i in range(len(X)):
    xi, yi = X[i]
    # 找到所属网格索引（注意：y 轴从下到上，所以 row = ny-1 - bin_y_idx）
    col_idx = np.digitize(xi, x_bins) - 1  # 0~3
    row_idx = np.digitize(yi, y_bins) - 1  # 0~3
    if 0 <= col_idx < nx and 0 <= row_idx < ny:
        cell_counts[row_idx, col_idx, y[i]] += 1

# 决定每个单元的标签：取最大计数的类别（若有平局，取最小类别号）
for r in range(ny):
    for c in range(nx):
        counts = cell_counts[r, c]
        if counts.sum() > 0:
            cell_labels[r, c] = np.argmax(counts)
        else:
            cell_labels[r, c] = -1  # 空单元

# 4. 定义颜色映射
color_map = {
    0: 'red',      # setosa
    1: 'green',    # versicolor
    2: 'blue',     # virginica
    -1: 'white'    # 空单元（但图中无空单元，我们用浅灰或白）
}

# 5. 绘图
fig, ax = plt.subplots(figsize=(7, 6))

# 绘制网格单元（背景色）
for r in range(ny):
    for c in range(nx):
        # 单元左下角坐标
        x0 = x_bins[c]
        y0 = y_bins[r]
        width = x_bins[c+1] - x0
        height = y_bins[r+1] - y0
        
        # 获取该单元标签
        label = cell_labels[r, c]
        color = color_map.get(label, 'lightgray')
        
        # 绘制矩形背景
        rect = patches.Rectangle((x0, y0), width, height,
                                 linewidth=0.8, edgecolor='black',
                                 facecolor=color, alpha=0.4)
        ax.add_patch(rect)

# 绘制数据点（按类别着色）
colors = ['red', 'green', 'blue']
markers = ['o', 's', '^']
for i, (color, marker) in enumerate(zip(colors, markers)):
    mask = y == i
    ax.scatter(X[mask, 0], X[mask, 1],
               c=color, marker=marker, s=30, edgecolors='k', linewidth=0.5,
               label=species_names[i])

# 绘制测试点（×）——位置参考图中：在红色与绿色交界处，约 (5.8, 3.0)
test_point = np.array([5.8, 3.0])
ax.scatter(test_point[0], test_point[1],
           c='black', marker='x', s=100, linewidths=2, zorder=5,
           label='测试点')

# 添加坐标轴标签
ax.set_xlabel('sepal length')
ax.set_ylabel('sepal width')
ax.set_title('Figure 6.2: 网格分类法示意图\n输入空间划分为 4×4 单元，按单元内多数类赋值')

# 设置坐标轴范围
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# 添加图例
ax.legend(loc='upper right')

# 网格线（可选，增强视觉效果）
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()

# 可选：打印每个单元的类别分布（用于验证）
print("4×4 网格单元类别（行：从下到上；列：从左到右）：")
print("行索引（y方向）：0=底部，3=顶部")
for r in range(ny-1, -1, -1):  # 从上到下打印（对应图中从上到下）
    row_str = ""
    for c in range(nx):
        lbl = cell_labels[r, c]
        row_str += f"{lbl:>2} "
    print(f"Row {r}: [{row_str}]")