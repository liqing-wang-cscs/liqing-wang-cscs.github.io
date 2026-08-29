## 从文件 portfolio_data_7.pkl 读取对数收益率、协方差矩阵，
## 随机生成投资组合，画出均值-方差散点图
#------------------------------------------------
import pickle

# 以二进制读取模式 ('rb') 加载
with open('portfolio_data_7.pkl', 'rb') as f:
    loaded_data = pickle.load(f)

# 还原变量
log_returns = loaded_data['log_returns']
cov_matrix = loaded_data['cov_matrix']
print("变量已成功导入！")

#-----------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ========== 【新增】中文字体配置 ==========
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False    
# ==========================================

# 1. 蒙特卡洛模拟：随机生成 1000 个投资组合
num_portfolios = 1000
# 创建空数组用于存储每个组合的：年化收益、年化波动率、夏普比率
results = np.zeros((3, num_portfolios)) 

for i in range(num_portfolios):
    # 随机生成权重并归一化（确保总和为 1）
    weights = np.random.random(len(log_returns.columns))
    weights /= np.sum(weights)
    
    # 计算年化预期收益（假设一年有 252 个交易日）
    portfolio_return = np.sum(log_returns.mean() * weights) * 252
    
    # 计算年化波动率（方差开根号，再乘以 252 开根号）
    portfolio_std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
    
    # 计算夏普比率（假设无风险利率为 1.0%，即 0.010）
    sharpe_ratio = (portfolio_return - 0.010) / portfolio_std 
    
    # 将结果存入数组
    results[0, i] = portfolio_return
    results[1, i] = portfolio_std
    results[2, i] = sharpe_ratio

# 2. 寻找关键的最优投资组合
# 最大夏普比率组合（性价比最高的组合）
max_sharpe_idx = np.argmax(results[2])
max_sharpe_ret, max_sharpe_std = results[0, max_sharpe_idx], results[1, max_sharpe_idx]

# 最小方差组合（风险最低的组合）
min_vol_idx = np.argmin(results[1])
min_vol_ret, min_vol_std = results[0, min_vol_idx], results[1, min_vol_idx]

# 3. 绘制有效边界图
plt.figure(figsize=(10, 7))
plt.xlim(left=0.25)  # 将横坐标（X轴）的左边界强制设置为 0.25
plt.xlim(right=1.25)  # 将横坐标（X轴）的右边界强制设置为 1.25

# 绘制所有随机生成的投资组合散点，颜色根据夏普比率变化
scatter = plt.scatter(results[1, :], results[0, :], c=results[2, :], 
                      cmap='viridis', marker='o', s=15, alpha=0.4)

# 标记最大夏普比率组合 (红色星号)
plt.scatter(max_sharpe_std, max_sharpe_ret, marker='*', color='red', s=300, label='最大夏普比率')

# 标记最小方差组合 (绿色星号)
plt.scatter(min_vol_std, min_vol_ret, marker='*', color='green', s=300, label='最小方差')

# 添加图形标签、颜色条和图例
plt.title('A股科技股有效边界 (Efficient Frontier)', fontsize=16)
plt.xlabel('年化波动率 / 风险', fontsize=12)
plt.ylabel('年化预期收益', fontsize=12)
plt.colorbar(label='夏普比率')
plt.legend(fontsize=12, loc='best')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()