import numpy as np
from scipy.integrate import odeint

# 参数设置
sigma = 10
rho = 28
beta = 8 / 3

# 定义洛伦兹方程组的右端项
def lorenz(state, t):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = rho * x - y - x * z
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# 初始条件和积分区间
s0 = [1.0, 1.0, 1.0]
t = np.linspace(0, 10, 100)

# 数值求解
solution = odeint(lorenz, s0, t)
x = solution[:, 0]
y = solution[:, 1]
z = solution[:, 2]

print(f"求解完成，共 {len(t)} 个时间点")
print(f"最终状态: x={x[-1]:.4f}, y={y[-1]:.4f}, z={z[-1]:.4f}")
