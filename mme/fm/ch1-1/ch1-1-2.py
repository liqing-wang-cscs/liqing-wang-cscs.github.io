## 从本地csv文件读入数据，画出时间序列图。
#------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体（Windows系统使用SimHei，Mac系统可换成Arial Unicode MS）
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False    

# 1. 读取 CSV 文件
# 假设你的文件名为 stock_prices.csv，分隔符为制表符(\t)
# 如果文件是逗号分隔的，请将 sep='\t' 改为 sep=','
# df = pd.read_csv('tech_stocks_3.csv', sep='\t')
df = pd.read_csv('tech_stocks_7.csv', sep=',', encoding='gbk')

# 2. 数据预处理
# 将“日期”列转换为 Pandas 的日期时间格式，并设置为索引
df['日期'] = pd.to_datetime(df['日期'])
df.set_index('日期', inplace=True)

# 3. 绘制时序图
plt.figure(figsize=(12, 6))

# 遍历每一列（即每只股票），分别绘制折线图
for stock_name in df.columns:
    plt.plot(df.index, df[stock_name], marker='o', label=stock_name, linewidth=2)

# 4. 设置图表样式
plt.title('A股科技股近三月收盘价走势', fontsize=16)
plt.xlabel('交易日期', fontsize=12)
plt.ylabel('收盘价 (元)', fontsize=12)
plt.legend(fontsize=12)  # 显示图例
plt.grid(True, linestyle='--', alpha=0.6)  # 添加网格线
plt.tight_layout()  # 自动调整布局，防止标签被遮挡

# 5. 显示图表
plt.show()