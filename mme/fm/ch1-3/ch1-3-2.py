import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# ==========================================
# 1. 数据准备与标准化
# ==========================================
# 读取数据（请确保文件路径正确，这里假设文件在当前目录）
# 将 '日期' 设为索引，方便后续处理
df = pd.read_csv('return.csv', parse_dates=['日期'], index_col='日期')

# 提取股票收益率数据（去除日期索引）
returns_data = df.values

# PCA 对量纲敏感，必须先进行 Z-score 标准化（均值为0，方差为1）
scaler = StandardScaler()
returns_scaled = scaler.fit_transform(returns_data)

# ==========================================
# 2. 执行主成分分析 (PCA)
# ==========================================
# 不指定 n_components，默认提取与特征数（7只股票）相同数量的主成分
pca = PCA()
pca.fit(returns_scaled)

# 获取特征值和方差解释比例
eigenvalues = pca.explained_variance_           # 特征值
var_ratio = pca.explained_variance_ratio_       # 单个因子的方差贡献率
cum_var_ratio = np.cumsum(var_ratio)            # 累计方差贡献率

# ==========================================
# 3. 打印统计结果
# ==========================================
print("="*50)
print("【主成分分析 (PCA) 结果】")
print("="*50)

# 创建一个漂亮的表格来展示结果
result_df = pd.DataFrame({
    '主成分': [f'PC{i+1}' for i in range(len(eigenvalues))],
    '特征值': eigenvalues,
    '方差贡献率(%)': var_ratio * 100,
    '累计方差贡献率(%)': cum_var_ratio * 100
})
print(result_df.to_string(index=False))
print("="*50)

# 给出 Kaiser 准则的初步建议
kaiser_k = np.sum(eigenvalues > 1)
print(f"\n💡 Kaiser准则建议：特征值 > 1 的主成分共有 {kaiser_k} 个。")

# ==========================================
# 4. 绘制碎石图 (Scree Plot)
# ==========================================
# plt.figure(figsize=(10, 6))

# # 绘制特征值折线图和散点
# plt.plot(range(1, len(eigenvalues) + 1), eigenvalues, marker='o', linestyle='--', color='b', label='Eigenvalues')

# # 添加一条 y=1 的参考线（Kaiser准则临界值）
# plt.axhline(y=1, color='r', linestyle=':', label='Kaiser Threshold (y=1)')

# # 添加累计方差贡献率折线（使用右侧Y轴）
# plt.twinx()
# plt.plot(range(1, len(cum_var_ratio) + 1), cum_var_ratio * 100, marker='s', linestyle='-', color='orange', label='Cumulative Variance (%)')
# plt.ylabel('Cumulative Variance (%)', fontsize=12)
# plt.ylim(0, 105)

# # 设置图表标题和标签
# plt.title('Scree Plot & Cumulative Variance', fontsize=14)
# plt.xlabel('Principal Component Number', fontsize=12)
# plt.ylabel('Eigenvalue', fontsize=12)
# plt.xticks(range(1, len(eigenvalues) + 1))
# plt.grid(True, linestyle=':', alpha=0.6)

# # 合并图例
# lines_1, labels_1 = plt.gca().get_legend_handles_labels()
# lines_2, labels_2 = plt.twinx().get_legend_handles_labels()
# plt.legend(lines_1 + lines_2, labels_1 + labels_2, loc='best')

# plt.tight_layout()
# plt.show()

# ==========================================
# 5. 指定 K=2 重新拟合模型并提取因子得分
# ==========================================
# 重新实例化 PCA，明确指定保留 2 个主成分
pca_k2 = PCA(n_components=2)
pca_k2.fit(returns_scaled)

# 提取因子得分 (Factor Scores)
# 形状为 (样本数, 2)，代表每个交易日在这两个因子上的暴露度
factor_scores = pca_k2.transform(returns_scaled)

# 将因子得分转换为 DataFrame，方便查看
factor_df = pd.DataFrame(
    factor_scores, 
    columns=['共同因子 F1', '共同因子 F2'],
    index=df.index  # 保持与原始数据相同的日期索引
)

print("="*50)
print("【提取的共同因子得分 (前5行)】")
print("="*50)
print(factor_df.head())

# ==========================================
# 6. 提取因子载荷矩阵并分析
# ==========================================
# pca_k2.components_ 的形状为 (2, 7)，代表 2 个因子在 7 只股票上的权重
# 为了直观，我们将其转置，行代表股票，列代表因子
loadings = pd.DataFrame(
    pca_k2.components_.T,
    columns=['共同因子 F1', '共同因子 F2'],
    index=df.columns  # 股票名称
)

print("\n" + "="*50)
print("【因子载荷矩阵 (Factor Loadings)】")
print("="*50)
print(loadings)

# ==========================================
# 7. 可视化：因子载荷热力图
# ==========================================
import seaborn as sns

# 解决 Matplotlib 中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(8, 6))
sns.heatmap(loadings, annot=True, fmt=".3f", cmap="coolwarm", center=0)
plt.title('Factor Loadings Heatmap (K=2)', fontsize=14)
plt.ylabel('Assets', fontsize=12)
plt.xlabel('Principal Components', fontsize=12)
plt.tight_layout()
plt.show()

