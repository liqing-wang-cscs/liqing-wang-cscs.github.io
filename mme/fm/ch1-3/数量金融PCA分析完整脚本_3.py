"""
数量金融实验 - 完整分析脚本
=============================================
包含三道题：
  问8. PCA因子提取方法
  问9. 套利机会检验算法
  问10. 因子载荷矩阵回归估计

数据要求：同目录下需要有一个 closing.csv 文件，
         格式为：日期,恒瑞医药,中微公司,澜起科技,兆易创新,海光信息,寒武纪,中芯国际
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# ============================================================
# 问8. PCA因子提取方法
# ============================================================
print("=" * 60)
print("问8. PCA因子提取方法")
print("=" * 60)

# --- 第1步：读取收盘价，计算对数收益率 ---
df = pd.read_csv('closing.csv', parse_dates=['日期'], index_col='日期')
# 对数收益率: ln(P_t / P_{t-1})，dropna()去掉第一行NaN
log_returns = np.log(df / df.shift(1)).dropna()
print(f"股票数量: {len(log_returns.columns)}")
print(f"交易日数: {len(log_returns)}")

# --- 第2步：Z-score标准化（均值为0，方差为1） ---
scaler = StandardScaler()
returns_scaled = scaler.fit_transform(log_returns)

# --- 第3步：全成分PCA，用于判断K取多少 ---
pca_full = PCA()
pca_full.fit(returns_scaled)

eigenvalues = pca_full.explained_variance_          # 特征值
var_ratio = pca_full.explained_variance_ratio_       # 方差贡献率
cum_var_ratio = np.cumsum(var_ratio)                 # 累计方差贡献率

# 打印各主成分的特征值和累计方差贡献率
result_df = pd.DataFrame({
    '主成分': [f'PC{i+1}' for i in range(len(eigenvalues))],
    '特征值': eigenvalues.round(4),
    '方差贡献率(%)': (var_ratio * 100).round(2),
    '累计方差贡献率(%)': (cum_var_ratio * 100).round(2)
})
print("\n【PCA 特征值与方差贡献率】")
print(result_df.to_string(index=False))

# Kaiser准则：特征值>1的主成分个数
kaiser_k = np.sum(eigenvalues > 1)
print(f"\nKaiser准则建议 K = {kaiser_k}")

# --- 第4步：指定K=2，提取因子得分和载荷矩阵 ---
K = 2
pca_k2 = PCA(n_components=K)
pca_k2.fit(returns_scaled)

# 因子得分：每个交易日在F1、F2上的值
factor_scores = pca_k2.transform(returns_scaled)
factor_df = pd.DataFrame(
    factor_scores,
    columns=['F1', 'F2'],
    index=log_returns.index
)
print(f"\n【共同因子得分 (前5行)】")
print(factor_df.head())

# 因子载荷矩阵：每只股票在F1、F2上的权重
loadings = pd.DataFrame(
    pca_k2.components_.T,
    columns=['F1', 'F2'],
    index=log_returns.columns
)
print(f"\n【因子载荷矩阵】")
print(loadings.round(4))

# --- 第5步：绘制碎石图 ---
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(range(1, len(eigenvalues)+1), eigenvalues, marker='o', linestyle='--', color='b', label='Eigenvalues')
plt.axhline(y=1, color='r', linestyle=':', label='Kaiser Threshold (y=1)')
plt.twinx()
plt.plot(range(1, len(cum_var_ratio)+1), cum_var_ratio*100, marker='s', linestyle='-', color='orange', label='Cumulative Variance (%)')
plt.ylabel('Cumulative Variance (%)')
plt.ylim(0, 105)
plt.title('Scree Plot & Cumulative Variance')
plt.xlabel('Principal Component Number')
plt.ylabel('Eigenvalue')
plt.xticks(range(1, len(eigenvalues)+1))
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.savefig('scree_plot.png', dpi=150, bbox_inches='tight')
plt.show()
print("碎石图已保存为 scree_plot.png")


# --- 第6步：绘制方差贡献率柱状图 ---
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False

fig, ax1 = plt.subplots(figsize=(10, 6))
x_labels = [f'PC{i+1}' for i in range(len(eigenvalues))]
bars = ax1.bar(x_labels, var_ratio * 100, color='#4E79A7', alpha=0.8, edgecolor='white')
ax1.set_xlabel('主成分', fontsize=12)
ax1.set_ylabel('方差贡献率 (%)', fontsize=12, color='#4E79A7')
ax1.tick_params(axis='y', labelcolor='#4E79A7')
ax1.set_title('各主成分方差贡献率与累计方差贡献率', fontsize=14)

# 在每个柱子顶部标注数值
for bar, val in zip(bars, var_ratio * 100):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{val:.1f}%', ha='center', va='bottom', fontsize=9)

# 右轴：累计方差贡献率折线
ax2 = ax1.twinx()
ax2.plot(x_labels, cum_var_ratio * 100, marker='s', linestyle='-', color='#E15759', linewidth=2, label='累计方差贡献率')
ax2.set_ylabel('累计方差贡献率 (%)', fontsize=12, color='#E15759')
ax2.tick_params(axis='y', labelcolor='#E15759')
ax2.set_ylim(0, 105)

# 在累计折线上标注数值
for i, val in enumerate(cum_var_ratio * 100):
    ax2.text(i, val + 1.5, f'{val:.1f}%', ha='center', va='bottom', fontsize=9, color='#E15759')

# 添加85%参考线
ax2.axhline(y=85, color='gray', linestyle=':', alpha=0.7)
ax2.text(len(eigenvalues)-0.5, 86, '85%参考线', fontsize=9, color='gray')

plt.grid(True, linestyle=':', alpha=0.4, axis='y')
plt.tight_layout()
plt.savefig('variance_contribution.png', dpi=150, bbox_inches='tight')
plt.show()
print("方差贡献率柱状图已保存为 variance_contribution.png")

# --- 第7步：绘制因子载荷热力图 ---
import matplotlib
# 使用 matplotlib 内置的颜色映射，不依赖 seaborn
fig, ax = plt.subplots(figsize=(8, 6))

# 将载荷矩阵转为 numpy 数组
loadings_arr = loadings.values
stocks = loadings.index.tolist()
factors = loadings.columns.tolist()

# 绘制热力图
im = ax.imshow(loadings_arr, cmap='RdYlBu_r', aspect='auto', vmin=-np.max(np.abs(loadings_arr)), vmax=np.max(np.abs(loadings_arr)))

# 设置坐标轴标签
ax.set_xticks(range(len(factors)))
ax.set_xticklabels(factors, fontsize=12)
ax.set_yticks(range(len(stocks)))
ax.set_yticklabels(stocks, fontsize=11)

# 在每个格子中标注数值
for i in range(len(stocks)):
    for j in range(len(factors)):
        val = loadings_arr[i, j]
        # 根据背景色深浅选择文字颜色
        text_color = 'white' if abs(val) > 0.5 * np.max(np.abs(loadings_arr)) else 'black'
        ax.text(j, i, f'{val:.3f}', ha='center', va='center', fontsize=11, color=text_color, fontweight='bold')

# 添加颜色条
cbar = fig.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('载荷值', fontsize=11)

ax.set_title('因子载荷热力图 (K=2)', fontsize=14, pad=15)
ax.set_xlabel('共同因子', fontsize=12)
ax.set_ylabel('股票', fontsize=12)

plt.tight_layout()
plt.savefig('factor_loadings_heatmap.png', dpi=150, bbox_inches='tight')
plt.show()
print("因子载荷热力图已保存为 factor_loadings_heatmap.png")

# --- 第8步：绘制因子载荷散点图（F1 vs F2 平面） ---
fig, ax = plt.subplots(figsize=(8, 7))

for i, stock in enumerate(loadings.index):
    f1_val = loadings.loc[stock, 'F1']
    f2_val = loadings.loc[stock, 'F2']
    ax.scatter(f1_val, f2_val, s=120, zorder=5)
    # 标注股票名称（稍微偏移避免遮挡点）
    ax.annotate(stock, (f1_val, f2_val), textcoords="offset points",
                xytext=(8, 5), fontsize=10)

# 添加坐标轴参考线
ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.5)

ax.set_xlabel('F1 载荷 (市场整体因子)', fontsize=12)
ax.set_ylabel('F2 载荷 (行业/风格因子)', fontsize=12)
ax.set_title('各股票在 F1-F2 因子平面上的位置', fontsize=14)
ax.grid(True, linestyle=':', alpha=0.4)

plt.tight_layout()
plt.savefig('factor_loadings_scatter.png', dpi=150, bbox_inches='tight')
plt.show()
print("因子载荷散点图已保存为 factor_loadings_scatter.png")

# --- 第9步：绘制因子得分时间序列图 ---
fig, axes = plt.subplots(2, 1, figsize=(12, 7), sharex=True)

# F1 时间序列
axes[0].plot(factor_df.index, factor_df['F1'], color='#4E79A7', linewidth=1.2)
axes[0].fill_between(factor_df.index, factor_df['F1'], alpha=0.3, color='#4E79A7')
axes[0].axhline(y=0, color='gray', linestyle='--', alpha=0.5)
axes[0].set_ylabel('F1 得分', fontsize=12)
axes[0].set_title('共同因子 F1 时间序列 (市场整体因子)', fontsize=13)
axes[0].grid(True, linestyle=':', alpha=0.4)

# F2 时间序列
axes[1].plot(factor_df.index, factor_df['F2'], color='#E15759', linewidth=1.2)
axes[1].fill_between(factor_df.index, factor_df['F2'], alpha=0.3, color='#E15759')
axes[1].axhline(y=0, color='gray', linestyle='--', alpha=0.5)
axes[1].set_ylabel('F2 得分', fontsize=12)
axes[1].set_xlabel('日期', fontsize=12)
axes[1].set_title('共同因子 F2 时间序列 (行业/风格因子)', fontsize=13)
axes[1].grid(True, linestyle=':', alpha=0.4)

# 自动旋转日期标签
fig.autofmt_xdate(rotation=30)
plt.tight_layout()
plt.savefig('factor_scores_timeseries.png', dpi=150, bbox_inches='tight')
plt.show()
print("因子得分时间序列图已保存为 factor_scores_timeseries.png")

# --- 第10步：绘制因子重构 vs 原始收益率对比图（选取前2只股票展示） ---
# 用 K=2 个因子重构原始收益率，展示还原效果
reconstructed = pca_k2.inverse_transform(factor_scores)  # 重构标准化后的数据

# 选取前3只股票做对比展示
show_stocks = log_returns.columns[:3].tolist()
fig, axes = plt.subplots(len(show_stocks), 1, figsize=(12, 3 * len(show_stocks)), sharex=True)

if len(show_stocks) == 1:
    axes = [axes]

for idx, stock in enumerate(show_stocks):
    col_idx = list(log_returns.columns).index(stock)
    original = returns_scaled[:, col_idx]     # 标准化后的原始收益率
    recon = reconstructed[:, col_idx]          # 重构后的收益率

    axes[idx].plot(log_returns.index, original, label='原始(标准化)', color='#4E79A7', alpha=0.7, linewidth=1)
    axes[idx].plot(log_returns.index, recon, label='K=2重构', color='#E15759', linestyle='--', linewidth=1.2)
    axes[idx].set_ylabel('收益率', fontsize=10)
    axes[idx].set_title(f'{stock} — 原始 vs 因子重构', fontsize=12)
    axes[idx].legend(fontsize=9)
    axes[idx].grid(True, linestyle=':', alpha=0.4)

axes[-1].set_xlabel('日期', fontsize=12)
fig.autofmt_xdate(rotation=30)
plt.tight_layout()
plt.savefig('factor_reconstruction.png', dpi=150, bbox_inches='tight')
plt.show()
print("因子重构对比图已保存为 factor_reconstruction.png")

# --- 计算重构精度（R²）---
print("\n【因子重构精度 (R²)】")
from sklearn.metrics import r2_score
for stock in log_returns.columns:
    col_idx = list(log_returns.columns).index(stock)
    r2 = r2_score(returns_scaled[:, col_idx], reconstructed[:, col_idx])
    print(f"  {stock}: R² = {r2:.4f}")




# --- 第11步：因子得分与原始股票收益率的相关性对比 ---
# 这一步帮助你直观感受：PCA 把 7 只股票"压缩"成 2 个因子后，
# 每个因子到底和哪些股票最相关？保留了多大比例的信息？

print("\n【因子得分与各股票收益率的相关系数】")

# 把因子得分和原始收益率拼在一起，方便算相关系数
combined = pd.concat([log_returns, factor_df], axis=1)

# 提取因子与各股票的相关系数矩阵
stocks_list = log_returns.columns.tolist()
corr_f1 = []  # F1 与每只股票的相关系数
corr_f2 = []  # F2 与每只股票的相关系数

for stock in stocks_list:
    corr_f1.append(combined[stock].corr(combined['F1']))
    corr_f2.append(combined[stock].corr(combined['F2']))

# 整理成 DataFrame
corr_df = pd.DataFrame({
    '股票': stocks_list,
    '与F1相关系数': np.round(corr_f1, 4),
    '与F2相关系数': np.round(corr_f2, 4),
    '综合相关度(sqrt(r1^2+r2^2))': np.round(np.sqrt(np.array(corr_f1)**2 + np.array(corr_f2)**2), 4)
})
print(corr_df.to_string(index=False))

# 信息保留比例说明
total_var_explained = cum_var_ratio[1] * 100  # K=2 的累计方差贡献率
print(f"\nK=2 个因子累计保留了原始数据 {total_var_explained:.1f}% 的方差信息")
print(f"这意味着，用 2 个因子就能解释 {len(stocks_list)} 只股票的大部分共同波动。")

# --- 第12步：绘制相关性热力图 ---
fig, ax = plt.subplots(figsize=(8, 6))

# 构建相关系数矩阵（只取因子部分）
corr_matrix = np.array([corr_f1, corr_f2])  # 形状 (2, 7)

im = ax.imshow(corr_matrix, cmap='RdYlBu_r', aspect='auto', vmin=-1, vmax=1)

ax.set_xticks(range(len(stocks_list)))
ax.set_xticklabels(stocks_list, fontsize=10, rotation=30, ha='right')
ax.set_yticks(range(2))
ax.set_yticklabels(['F1 (市场因子)', 'F2 (行业因子)'], fontsize=11)

# 标注数值
for i in range(2):
    for j in range(len(stocks_list)):
        val = corr_matrix[i, j]
        text_color = 'white' if abs(val) > 0.5 else 'black'
        ax.text(j, i, f'{val:.3f}', ha='center', va='center', fontsize=11,
                color=text_color, fontweight='bold')

cbar = fig.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('Pearson 相关系数', fontsize=11)
ax.set_title('因子得分 vs 原始股票收益率 相关性', fontsize=14, pad=15)

plt.tight_layout()
plt.savefig('factor_correlation_heatmap.png', dpi=150, bbox_inches='tight')
plt.show()
print("因子相关性热力图已保存为 factor_correlation_heatmap.png")

# --- 第13步：绘制每只股票的信息保留度柱状图 ---
fig, ax = plt.subplots(figsize=(10, 6))

# 综合相关度的平方近似于该股票被 K=2 因子解释的方差比例
info_retained = np.array(corr_f1)**2 + np.array(corr_f2)**2

bars = ax.bar(stocks_list, info_retained * 100, color='#4E79A7', alpha=0.8, edgecolor='white')
ax.set_ylabel('信息保留比例 (%)', fontsize=12)
ax.set_xlabel('股票', fontsize=12)
ax.set_title('每只股票被 K=2 因子解释的信息比例 (R² 近似)', fontsize=14)
ax.axhline(y=np.mean(info_retained) * 100, color='#E15759', linestyle='--',
           label=f'平均值: {np.mean(info_retained)*100:.1f}%')

# 在柱子上标注数值
for bar, val in zip(bars, info_retained * 100):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'{val:.1f}%', ha='center', va='bottom', fontsize=10)

ax.legend(fontsize=11)
ax.set_ylim(0, max(info_retained * 100) + 10)
ax.grid(True, linestyle=':', alpha=0.4, axis='y')

plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('info_retention_by_stock.png', dpi=150, bbox_inches='tight')
plt.show()
print("信息保留度柱状图已保存为 info_retention_by_stock.png")

# --- 第14步：总结性文字输出 ---
print("\n" + "=" * 50)
print("【PCA 信息压缩总结】")
print("=" * 50)
print(f"  原始维度: {len(stocks_list)} 只股票")
print(f"  压缩维度: K = {K} 个因子")
print(f"  累计方差解释率: {total_var_explained:.1f}%")
print(f"  信息保留最多的股票: {stocks_list[np.argmax(info_retained)]} ({max(info_retained)*100:.1f}%)")
print(f"  信息保留最少的股票: {stocks_list[np.argmin(info_retained)]} ({min(info_retained)*100:.1f}%)")
print(f"  平均信息保留率: {np.mean(info_retained)*100:.1f}%")
print("=" * 50)



# ============================================================
# 问9. 套利机会检验算法
# ============================================================
print("\n" + "=" * 60)
print("问9. 套利机会检验算法")
print("=" * 60)

# 假设给定3只资产的期望收益率和因子敏感系数
E_R = np.array([0.10, 0.12, 0.08])   # 期望收益率
b = np.array([1.0, 1.2, 0.8])         # 因子敏感系数

# --- 第1步：构建约束矩阵A ---
# 第一行：全1向量（零净投资约束 w1+w2+w3=0）
# 第二行：因子敏感系数（零因子风险约束 w1*b1+w2*b2+w3*b3=0）
A = np.vstack([np.ones(len(E_R)), b])

# --- 第2步：用SVD求零空间 ---
# 零空间中的向量满足：零投资 + 零因子风险
U, S, Vt = np.linalg.svd(A)
# 最小奇异值对应的右奇异向量就是零空间基向量
null_vec = Vt.T[:, -1]

# --- 第3步：检验套利机会 ---
portfolio_return = np.dot(E_R, null_vec)
if abs(portfolio_return) > 1e-6:
    # 如果收益为负，反转权重即可获利
    if portfolio_return < 0:
        null_vec = -null_vec
        portfolio_return = -portfolio_return
    print(f"存在套利机会！")
    print(f"套利组合权重 w = {null_vec.round(4)}")
    print(f"期望收益率 = {portfolio_return:.6f}")
else:
    print("市场无套利机会，所有资产定价符合单因子模型。")


# ============================================================
# 问10. 因子载荷矩阵回归估计
# ============================================================
print("\n" + "=" * 60)
print("问10. 因子载荷矩阵回归估计")
print("=" * 60)

import statsmodels.api as sm

# --- 第1步：准备自变量X（因子得分，添加常数项） ---
X = sm.add_constant(factor_df)  # factor_df 来自问8的结果

# --- 第2步：逐只股票进行多元线性回归 ---
loadings_matrix = pd.DataFrame(index=log_returns.columns, columns=['截距', 'b_F1', 'b_F2'])

for stock in log_returns.columns:
    Y = log_returns[stock]           # 因变量：某只股票的收益率
    model = sm.OLS(Y, X).fit()       # OLS回归
    loadings_matrix.loc[stock, '截距'] = model.params['const']
    loadings_matrix.loc[stock, 'b_F1'] = model.params['F1']
    loadings_matrix.loc[stock, 'b_F2'] = model.params['F2']

# --- 第3步：输出因子载荷矩阵B ---
print("【估计的因子载荷矩阵 B】")
print(loadings_matrix.round(4))

print("\n" + "=" * 60)
print("全部分析完成！")
print("=" * 60)
