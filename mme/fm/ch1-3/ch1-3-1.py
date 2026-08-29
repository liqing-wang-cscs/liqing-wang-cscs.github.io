import pandas as pd
import numpy as np

# 1. 读取数据
df = pd.read_csv('closing.csv', parse_dates=['日期'], index_col='日期')

# 2. 计算对数收益率
log_returns = np.log(df / df.shift(1))

# 3. 处理第一行数据
log_returns = log_returns.dropna()

# 4. 保留四位小数
log_returns = log_returns.round(4)

# 5. 保存为新的 CSV 文件
log_returns.to_csv('return.csv')

print("对数收益率已成功计算并保存到 return.csv")