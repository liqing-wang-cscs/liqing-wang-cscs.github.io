import numpy as np

def binomial_option_pricing(S0, E, r, u, d, N):
    """
    CRR二叉树期权定价模型
    :param S0: 初始股价
    :param E: 施权价
    :param r: 无风险利率 (单期)
    :param u: 上涨因子
    :param d: 下跌因子
    :param N: 时间步数
    """
    
    # 1. 计算风险中性概率
    p_star = ((1 + r) - d) / (u - d)
    print(f"风险中性概率 p*: {p_star:.4f}")
    
    # 2. 构建股票价格树 (使用二维列表或数组)
    # stock_tree[i][j] 表示第 i 步，经历了 j 次上涨后的股价
    stock_tree = []
    for i in range(N + 1):
        level = []
        for j in range(i + 1):
            price = S0 * (u ** j) * (d ** (i - j))
            level.append(price)
        stock_tree.append(level)
        
    print("\n--- 股票价格二叉树 ---")
    for i, level in enumerate(stock_tree):
        print(f"t={i}: {[f'{p:.2f}' for p in level]}")

    # 3. 初始化期权价值树 (从最后一步开始)
    # option_tree[i][j] 对应 stock_tree[i][j] 处的期权价值
    option_tree = [[0.0] * (i + 1) for i in range(N + 1)]
    
    # 设置终端价值 (t=N)
    for j in range(N + 1):
        option_tree[N][j] = max(stock_tree[N][j] - E, 0)
        
    # 4. 向后倒推计算期权价值
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            # 期望值折现
            expected_val = p_star * option_tree[i+1][j+1] + (1 - p_star) * option_tree[i+1][j]
            option_tree[i][j] = expected_val / (1 + r)
            
    print("\n--- 期权价值二叉树 (倒推结果) ---")
    for i, level in enumerate(option_tree):
        print(f"t={i}: {[f'{v:.4f}' for v in level]}")
        
    return option_tree[0][0]

# --- 主程序执行 ---
if __name__ == "__main__":
    # 题目给定参数
    S0 = 100
    E = 105
    r = 0.05
    u = 1.1
    d = 0.9
    N = 3
    
    print(f"参数设定: S0={S0}, E={E}, r={r}, u={u}, d={d}, N={N}\n")
    
    final_price = binomial_option_pricing(S0, E, r, u, d, N)
    
    print(f"\n>>> 最终计算结果: 该欧式看涨期权的当前价值为 {final_price:.4f} <<<")
    