import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 参数与求解（同上）
sigma = 10; rho = 28; beta = 8 / 3
def lorenz(state, t):
    x, y, z = state
    return [sigma*(y-x), rho*x-y-x*z, x*y-beta*z]

s0 = [1.0, 1.0, 1.0]
t = np.linspace(0, 50, 3000)
sol = odeint(lorenz, s0, t)

# 三维绘图
fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol[:, 0], sol[:, 1], sol[:, 2], 'b-', lw=0.5)
ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$y$', fontsize=12)
ax.set_zlabel('$z$', fontsize=12)
ax.set_title('Lorenz Attractor ($\\sigma=10, \\rho=28, \\beta=8/3$)', fontsize=14)
ax.view_init(elev=20, azim=45)
plt.tight_layout()
plt.savefig('lorenz_attractor.png', dpi=150)
plt.show()
