def american_put_binomial(S0, E, r, u, d, N):
    """
    美式看跌期权二叉树定价模型
    """
    # 1. 计算风险中性概率
    p_star = ((1 + r) - d) / (u - d)
    print(f"风险中性概率 p*: {p_star:.4f}")
    
    # 2. 构建股票价格树
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

    # 3. 初始化期权价值树
    option_tree = [[0.0] * (i + 1) for i in range(N + 1)]
    
    # 设置终端价值 (t=N)，此时必须行权或作废
    for j in range(N + 1):
        option_tree[N][j] = max(E - stock_tree[N][j], 0)
        
    # 4. 向后倒推计算期权价值 (核心修改点)
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            # 计算继续持有的期望折现价值
            expected_val = p_star * option_tree[i+1][j+1] + (1 - p_star) * option_tree[i+1][j]
            hold_value = expected_val / (1 + r)
            
            # 计算立即行权的内在价值
            exercise_value = max(E - stock_tree[i][j], 0)
            
            # 美式期权取两者的较大值
            option_tree[i][j] = max(hold_value, exercise_value)
            
    print("\n--- 美式看跌期权价值二叉树 (倒推结果) ---")
    for i, level in enumerate(option_tree):
        print(f"t={i}: {[f'{v:.4f}' for v in level]}")
        
    return option_tree[0][0]

# --- 主程序执行 ---
if __name__ == "__main__":
    # 题目给定参数
    S0 = 100
    E = 110
    r = 0.05
    u = 1.1
    d = 0.9
    N = 3
    
    print(f"参数设定: S0={S0}, E={E}, r={r}, u={u}, d={d}, N={N}\n")
    
    final_price = american_put_binomial(S0, E, r, u, d, N)
    
    print(f"\n>>> 最终计算结果: 该美式看跌期权的当前价值为 {final_price:.4f} <<<")
    