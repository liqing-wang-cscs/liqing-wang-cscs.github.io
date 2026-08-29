import tushare as ts
import pandas as pd

# 1. 初始化接口（请替换为你自己的真实 Token）
ts.set_token('你的Tushare_Token')
pro = ts.pro_api()

# 2. 定义股票代码列表和时间范围
stock_codes = [
    '688041.SH', #海光信息
    '688981.SH', #中芯国际
    '688256.SH', #寒武纪
    '688012.SH', #中微公司
    '603986.SH', #兆易创新
    '600276.SH', #恒瑞医药
    '688008.SH' #澜起科技
    ]
start_date = '20260526'
end_date = '20260826'

# 3. 初始化一个空的 DataFrame 用于存放合并后的数据
df_all = pd.DataFrame()

# 4. 循环获取每只股票的收盘价数据
for code in stock_codes:
    print(f"正在获取 {code} 的数据...")
    df = pro.daily(
        ts_code=code,
        start_date=start_date,
        end_date=end_date,
        fields='ts_code,trade_date,close'  # 仅提取代码、日期和收盘价
    )
    
    # 将单只股票的数据追加到总表中
    df_all = pd.concat([df_all, df], ignore_index=True)

# 5. 数据清洗：按股票代码和交易日期进行升序排序
df_all = df_all.sort_values(['ts_code', 'trade_date'])

# 5. 【新增】将数据保存在当前目录下
df_all.to_csv('tech_stocks_4.csv', index=False, encoding='utf-8-sig')
print("\n数据已成功保存为 tech_stocks_4.csv！")

# 6. 打印查看最终结果
print("\n--- 数据获取完成 ---")
print(df_all)

## 注：后续用excel整理该数据文件，得到tech_stock_7.csv. 