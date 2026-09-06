import numpy as np

# 输入数据
weights = np.array([0.50, 0.30, 0.20])
returns = np.array([0.20, 0.15, 0.20])
std = np.array([0.20, 0.30, 0.40])

corr = np.array([
    [1.0, 0.5, 0.3],
    [0.5, 1.0, 0.1],
    [0.3, 0.1, 1.0]
])

# 计算期望回报率
Rp = np.dot(weights, returns)

# 构建协方差矩阵
cov = corr * np.outer(std, std)

# 计算方差和标准差
Vp = weights @ cov @ weights
Sp = np.sqrt(Vp)

# 输出结果
print(f"期望回报率: {Rp*100:.2f}%")
print(f"标准差: {Sp*100:.2f}%")