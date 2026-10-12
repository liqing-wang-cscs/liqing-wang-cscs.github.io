import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from sklearn.mixture import GaussianMixture

# ============ 1. 设置随机种子，保证可复现 ============
np.random.seed(42)

# ============ 2. 生成模拟的 Old Faithful 数据 ============
# 真实数据集有两个簇，这里用两个高斯分布合成
# 簇 1：短喷发 + 短等待
n1 = 100
mean1 = [2.0, 55]
cov1 = [[0.05, 0.6], [0.6, 20]]
X1 = np.random.multivariate_normal(mean1, cov1, n1)

# 簇 2：长喷发 + 长等待
n2 = 172
mean2 = [4.3, 80]
cov2 = [[0.1, 1.0], [1.0, 20]]
X2 = np.random.multivariate_normal(mean2, cov2, n2)

# 合并成一个数据集
X = np.vstack([X1, X2])

# 限制在合理范围（模拟真实数据的截断）
X = X[(X[:, 0] > 1) & (X[:, 0] < 6)]
X = X[(X[:, 1] > 40) & (X[:, 1] < 100)]

# ============ 3. 定义画椭圆（等高线）的辅助函数 ============
def draw_ellipse(ax, mean, cov, n_std=2.0, **kwargs):
    """根据均值和协方差矩阵画椭圆"""
    # 计算协方差矩阵的特征值和特征向量
    vals, vecs = np.linalg.eigh(cov)
    # 特征值对应的半轴长度
    order = vals.argsort()[::-1]
    vals, vecs = vals[order], vecs[:, order]
    # 椭圆旋转角度
    angle = np.degrees(np.arctan2(vecs[1, 0], vecs[0, 0]))
    # 半轴长度（n_std 倍标准差）
    width, height = 2 * n_std * np.sqrt(vals)
    # 画椭圆
    ellip = Ellipse(xy=mean, width=width, height=height,
                    angle=angle, fill=False, **kwargs)
    ax.add_patch(ellip)
    return ellip

plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False   

# ============ 4. 创建画布 ============
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# ---------- (a) 单个高斯分布 ----------
ax = axes[0]
# 用 GMM 拟合 1 个高斯（等价于用样本均值和协方差）
gmm1 = GaussianMixture(n_components=1, covariance_type='full', random_state=42)
gmm1.fit(X)

# 画散点
ax.scatter(X[:, 0], X[:, 1], c='blue', s=15, alpha=0.8, edgecolors='none')

# 画多个不同置信水平的椭圆
mean1 = gmm1.means_[0]
cov1 = gmm1.covariances_[0]
for n_std in [1.0, 1.5, 2.0, 2.5]:
    draw_ellipse(ax, mean1, cov1, n_std=n_std,
                 edgecolor='red', linewidth=1.5, alpha=0.8)

ax.set_xlim(1, 6)
ax.set_ylim(40, 100)
ax.set_xlabel('$x_1$', fontsize=12)
ax.set_ylabel('$x_2$', fontsize=12)
ax.set_title('(a) 单个高斯分布', fontsize=13)
ax.grid(alpha=0.3)

# ---------- (b) 两个高斯的线性组合（GMM） ----------
ax = axes[1]
gmm2 = GaussianMixture(n_components=2, covariance_type='full', random_state=42)
gmm2.fit(X)

# 画散点，按聚类标签着色
labels = gmm2.predict(X)
ax.scatter(X[:, 0], X[:, 1], c='blue', s=15, alpha=0.8, edgecolors='none')

# 对每个高斯分量，画多个置信椭圆
for k in range(2):
    mean_k = gmm2.means_[k]
    cov_k = gmm2.covariances_[k]
    for n_std in [0.5, 1.0, 1.5, 2.0, 2.5]:
        draw_ellipse(ax, mean_k, cov_k, n_std=n_std,
                     edgecolor='red', linewidth=1.5, alpha=0.8)

ax.set_xlim(1, 6)
ax.set_ylim(40, 100)
ax.set_xlabel('$x_1$', fontsize=12)
ax.set_ylabel('$x_2$', fontsize=12)
ax.set_title('(b) 两个高斯的线性组合', fontsize=13)
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('old_faithful.png', dpi=150, bbox_inches='tight')
plt.show()