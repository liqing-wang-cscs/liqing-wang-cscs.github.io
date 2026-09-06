import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False    

# 数据与拟合参数
t_data = np.array([0,1,2,3,4,5,6,8,10,12,14,16,18])
x_data = np.array([60,63,64,63,61,58,53,44,39,38,41,46,53])
y_data = np.array([30,34,38,44,50,55,58,56,47,38,30,27,26])
a, b, c, d = 0.1907, 0.0048, 0.4829, 0.0095

# 定义微分方程
def lotka_volterra(t, z):
    x, y = z
    dx = a*x - b*x*y
    dy = -c*y + d*x*y
    return [dx, dy]

# 数值求解
sol = solve_ivp(lotka_volterra, [0, 18], [60, 30], t_eval=np.linspace(0,18,100))

# 绘图
plt.figure(figsize=(10,5))
plt.plot(sol.t, sol.y[0], 'b-', label='兔子模拟')
plt.plot(sol.t, sol.y[1], 'r-', label='狐狸模拟')
plt.scatter(t_data, x_data, color='blue', marker='o', label='兔子观测')
plt.scatter(t_data, y_data, color='red', marker='s', label='狐狸观测')
plt.xlabel('时间 (月)')
plt.ylabel('种群数量')
plt.legend()
plt.grid(True)
plt.title('捕食者-被捕食者模型拟合与观测数据')
plt.show()
