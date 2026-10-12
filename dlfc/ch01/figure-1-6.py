import numpy as np
import matplotlib.pyplot as plt

# ============ 1. 设置中文字体（可选） ============
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False   # 正常显示负号

# ============ 2. 生成带噪声的正弦数据 ============
np.random.seed(42)          # 固定随机种子，保证结果可复现

# 取 10 个采样点，范围 [0, 1]
x_train = np.linspace(0, 1, 10)
# 真实函数 sin(2πx)，加上高斯噪声
t_train = np.sin(2 * np.pi * x_train) + np.random.normal(0, 0.2, size=x_train.shape)

# 用于画光滑曲线的密集点
x_plot = np.linspace(0, 1, 200)
y_true = np.sin(2 * np.pi * x_plot)

# ============ 3. 定义多项式拟合函数 ============
def poly_fit(x, t, M):
    """用 M 阶多项式拟合数据，返回预测函数"""
    # 构造范德蒙德矩阵（Vandermonde matrix）
    X = np.vander(x, M + 1, increasing=True)   # 每列是 x^0, x^1, ..., x^M
    # 最小二乘解：w = (X^T X)^{-1} X^T t
    w, *_ = np.linalg.lstsq(X, t, rcond=None)
    # 返回预测函数
    def predict(x_new):
        X_new = np.vander(x_new, M + 1, increasing=True)
        return X_new @ w
    return predict

# ============ 4. 绘制 2×2 四联图 ============
orders = [0, 1, 3, 9]
fig, axes = plt.subplots(2, 2, figsize=(10, 7))
axes = axes.flatten()

for ax, M in zip(axes, orders):
    # 拟合
    predict = poly_fit(x_train, t_train, M)
    y_pred = predict(x_plot)

    # 画真实函数（绿色）
    ax.plot(x_plot, y_true, 'g-', linewidth=2, label='真实函数 $\\sin(2\\pi x)$')
    # 画拟合曲线（红色）
    ax.plot(x_plot, y_pred, 'r-', linewidth=1.8, label=f'$M={M}$ 拟合')
    # 画训练数据点（蓝色）
    ax.plot(x_train, t_train, 'bo', markersize=6, label='训练数据')

    # 坐标轴设置
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel('$t$', fontsize=12)
    ax.set_title(f'$M = {M}$', fontsize=13)
    ax.grid(alpha=0.3)

# 只在第一个子图显示图例，避免重复
axes[0].legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('poly_fit_sin.png', dpi=150, bbox_inches='tight')
plt.show()