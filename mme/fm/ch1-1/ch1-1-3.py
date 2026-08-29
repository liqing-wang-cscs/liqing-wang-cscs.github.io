## 从本地csv文件 tech_stocks_7.csv 读入数据，
## 计算对数收益率、协方差矩阵，
## 保存在 portfolio_data_7.pkl 这个文件里。
#------------------------------------------------

import pandas as pd
import numpy as np

# 1. 载入本地 CSV 数据
# 注意：你提供的数据是逗号分隔的，因此使用默认的 sep=','
# 如果文件包含中文且出现乱码，可以加上 encoding='utf-8-sig'
df = pd.read_csv('tech_stocks_7.csv', sep=',', encoding='gbk', parse_dates=['日期'])

# 2. 数据预处理：将“日期”设置为索引
df.set_index('日期', inplace=True)

# 3. 计算每日对数收益率
# 公式：ln(P_t / P_{t-1})
# dropna() 用于剔除第一行因为缺少前一日数据而产生的空值
log_returns = np.log(df / df.shift(1)).dropna()

print("--- 每日对数收益率 (前5行) ---")
print(log_returns.head())

# 4. 计算协方差矩阵
# 在金融量化中，协方差矩阵用于衡量各资产收益率之间的联动性和风险
cov_matrix = log_returns.cov()

print("\n--- 收益率协方差矩阵 ---")
print(cov_matrix)

#--------------------------------------------
import pickle

# 假设前面程序已经计算出了 log_returns 和 cov_matrix
data_to_save = {
    'log_returns': log_returns,
    'cov_matrix': cov_matrix
}

# 以二进制写入模式 ('wb') 保存
with open('portfolio_data_7.pkl', 'wb') as f:
    pickle.dump(data_to_save, f)
print("变量已成功保存！")
