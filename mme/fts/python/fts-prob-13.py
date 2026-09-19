import numpy as np
from scipy.optimize import minimize

x = np.array([3, 5, 6, 7, 4, 8, 5, 9], dtype=float)
y = np.array([4, 9, 5, 3, 8, 5, 8, 5], dtype=float)

# 目标函数：残差平方和
def loss(p):
    a, b = p
    return np.sum((a*np.exp(x) + b*np.log(x) - y) ** 2)

# 约束
cons = [{'type': 'ineq', 'fun': lambda p: p[0]},      # a >= 0
        {'type': 'ineq', 'fun': lambda p: p[1]},      # b >= 0
        {'type': 'ineq', 'fun': lambda p: 1 - p[0] - p[1]}]  # a+b <= 1

res = minimize(loss, x0=[0.01, 0.01], constraints=cons, method='SLSQP')
a, b = res.x
print(f"拟合结果：a = {a:.6f}, b = {b:.6f}")
print(f"约束检查：a>=0: {a>=0}, b>=0: {b>=0}, a+b<=1: {a+b<=1}")
print(f"残差平方和 = {res.fun:.6f}")