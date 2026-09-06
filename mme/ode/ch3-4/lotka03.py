import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False    

a, b, c, d = 0.2, 0.005, 0.5, 0.01

# 定义微分方程
def lotka_volterra(t, z):
    x, y = z
    dx = a*x - b*x*y
    dy = -c*y + d*x*y
    return [dx, dy]

X, Y = np.meshgrid(np.linspace(30, 80, 20), np.linspace(15, 65, 20))
u = a*X - b*X*Y
v = -c*Y + d*X*Y
norm = np.sqrt(u**2 + v**2)
u /= norm; v /= norm

plt.figure(figsize=(8,6))
plt.streamplot(X, Y, u, v, density=1.5, color='gray')
# 对几个初值画轨道
for x0, y0 in [(60,30), (70,40), (50,50), (65,25)]:
    sol = solve_ivp(lotka_volterra, [0, 30], [x0, y0], t_eval=np.linspace(0,30,500))
    plt.plot(sol.y[0], sol.y[1], linewidth=2)
plt.xlabel('兔子数量')
plt.ylabel('狐狸数量')
plt.title('相平面与方向场')
plt.grid(True)
plt.show()
