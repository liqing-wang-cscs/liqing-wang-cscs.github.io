import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# ============ 参数设置 ============
v = 1.0       # 兔子速度
k = 1.1       # 狐狸速度 = k * v（k > 1 才能追上）
kv = k * v    # 狐狸速度大小

# ============ 定义微分方程 ============
# 兔子位置: (10, v*t)
# 狐狸位置: (x, y)，始终对准兔子，速度大小为 kv
def fox_ode(t, state):
    x, y = state
    # 兔子当前位置
    rx, ry = 10.0, v * t
    # 狐狸到兔子的方向向量
    dx, dy = rx - x, ry - y
    dist = np.sqrt(dx**2 + dy**2)
    if dist < 1e-5:  # 已追上，停止运动
        return [0.0, 0.0]
    # 狐狸速度方向指向兔子，大小恒为 kv
    vx = kv * dx / dist
    vy = kv * dy / dist
    return [vx, vy]

# ============ 数值求解（用于动画数据） ============
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 200)

sol = solve_ivp(fox_ode, t_span, [0.0, 0.0], t_eval=t_eval, method='RK45',
                events=lambda t, s: np.sqrt((10 - s[0])**2 + (v*t - s[1])**2) - 1e-6)

# 如果提前追上，截断时间
if sol.t_events[0].size > 0:
    t_hit = sol.t_events[0][0]
    mask = sol.t <= t_hit
    t_data = sol.t[mask]
    x_data = sol.y[0, mask]
    y_data = sol.y[1, mask]
else:
    t_data = sol.t
    x_data = sol.y[0]
    y_data = sol.y[1]

# 兔子轨迹
rx_data = np.ones_like(t_data)*10
ry_data = v * t_data

# ============ 创建动画 ============
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-0.5, 12.5)
ax.set_ylim(-0.5, max(2.5, v * t_data[-1] + 0.5))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title(f'Fox (speed={kv}) chasing Rabbit (speed={v}), k={k}')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

# 轨迹线
fox_line, = ax.plot([], [], 'b-', lw=1.5, label='Fox path')
rabbit_line, = ax.plot([], [], 'r--', lw=1.5, label='Rabbit path')

# 动点
fox_dot, = ax.plot([], [], 'bo', markersize=10, label='Fox')
rabbit_dot, = ax.plot([], [], 'rs', markersize=10, label='Rabbit')

# 连线（狐狸始终对准兔子）
connect_line, = ax.plot([], [], 'g-', lw=0.8, alpha=0.5)

ax.legend(loc='upper left')

def init():
    fox_line.set_data([], [])
    rabbit_line.set_data([], [])
    fox_dot.set_data([], [])
    rabbit_dot.set_data([], [])
    connect_line.set_data([], [])
    return fox_line, rabbit_line, fox_dot, rabbit_dot, connect_line

def update(frame):
    i = frame
    # 更新狐狸
    fox_line.set_data(x_data[:i+1], y_data[:i+1])
    fox_dot.set_data([x_data[i]], [y_data[i]])
    # 更新兔子
    rabbit_line.set_data(rx_data[:i+1], ry_data[:i+1])
    rabbit_dot.set_data([rx_data[i]], [ry_data[i]])
    # 连线
    connect_line.set_data([x_data[i], rx_data[i]], [y_data[i], ry_data[i]])
    return fox_line, rabbit_line, fox_dot, rabbit_dot, connect_line

ani = FuncAnimation(fig, update, frames=len(t_data), init_func=init,
                    blit=True, interval=20, repeat=True)

plt.tight_layout()
plt.show()

# 如果需要保存为 GIF，取消下面注释：
# ani.save('fox_chases_rabbit.gif', writer='pillow', fps=30)