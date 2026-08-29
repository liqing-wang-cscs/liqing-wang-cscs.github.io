import numpy as np
import matplotlib.pyplot as plt

# 解决 Matplotlib 中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def capm_demo():
    # 1. 模拟数据：假设某股票和市场组合的日度收益率（共252个交易日）
    np.random.seed(42)
    # 市场组合日收益率（均值 0.05%，波动率 2%）
    market_returns = np.random.normal(0.0005, 0.02, 252)
    # 股票收益率（设定理论 β = 1.2，Alpha = 0.0002，特异风险标准差 = 0.015）
    stock_returns = 0.0002 + 1.2 * market_returns + np.random.normal(0, 0.015, 252)

    # 2. 计算 β 系数：β = 资产与市场的协方差 / 市场的方差
    covariance = np.cov(stock_returns, market_returns)[0, 1]
    market_variance = np.var(market_returns)
    beta = covariance / market_variance
    print(f"股票的 β 系数：{beta:.2f}（理论设定为 1.2）")

    # 3. 计算 CAPM 预期收益率
    risk_free_rate = 0.02  # 无风险利率（年化 2%）
    market_return_annual = np.mean(market_returns) * 252  # 市场组合年化收益率
    expected_return = risk_free_rate + beta * (market_return_annual - risk_free_rate)
    print(f"市场组合年化收益率：{market_return_annual:.2%}")
    print(f"CAPM 预期年化收益率：{expected_return:.2%}")

    # 4. 可视化：股票收益率 vs 市场收益率（β 为回归线斜率）
    plt.figure(figsize=(10, 6))
    plt.scatter(market_returns, stock_returns, alpha=0.6, label='每日收益率散点')
    
    # 绘制回归线（体现 β 的含义）
    z = np.polyfit(market_returns, stock_returns, 1)
    p = np.poly1d(z)
    plt.plot(market_returns, p(market_returns), "r--", linewidth=2, 
             label=f'特征线/回归线（β={z[0]:.2f}）')
    
    plt.xlabel('市场组合日收益率', fontsize=12)
    plt.ylabel('股票日收益率', fontsize=12)
    plt.title('CAPM 中 β 系数的几何含义（回归线斜率展示）', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(alpha=0.3)
    plt.show()

if __name__ == "__main__":
    capm_demo()
