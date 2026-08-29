## 从文件 portfolio_data_7.pkl 读取对数收益率、协方差矩阵，
## 计算最小方差投资组合
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
from scipy.optimize import minimize
import numpy as np

# 1. 定义目标函数：计算投资组合的方差
# 数学公式为：W' * Cov * W
def portfolio_variance(weights, cov_matrix):
    return np.dot(weights.T, np.dot(cov_matrix, weights))

# 2. 设定约束条件
# 约束1：所有权重之和必须等于 1
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# 约束2：权重边界（A股不能卖空，假设每只股票至少分配 1% 的资金，防止权重为绝对的0）
bounds = tuple((0.01, 1.0) for _ in range(len(log_returns.columns)))

# 3. 设定初始权重猜测（平均分配）
init_weights = np.array([1.0 / len(log_returns.columns)] * len(log_returns.columns))

# 4. 运行优化算法 (SLSQP 是处理带约束非线性优化最经典的算法)
result = minimize(
    portfolio_variance, 
    init_weights, 
    args=(cov_matrix,), 
    method='SLSQP', 
    bounds=bounds, 
    constraints=constraints
)

# 5. 输出最优结果
print("\n--- 最小方差投资组合结果 ---")
print("最优权重分配:")
for asset, weight in zip(log_returns.columns, result.x):
    print(f"{asset}: {weight:.2%}")

# 计算并输出组合的最小波动率（年化）
min_variance = result.fun
annual_volatility = np.sqrt(min_variance * 252)
print(f"\n组合最小方差: {min_variance:.6f}")
print(f"组合年化波动率: {annual_volatility:.2%}")
