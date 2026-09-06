import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorenz(state, t, params):
    sigma, rho, beta = params
    x, y, z = state
    return [sigma*(y-x), rho*x-y-x*z, x*y-beta*z]

t = np.linspace(0, 30, 3000)
s0 = [0, 1, 0]

# 两组参数
params1 = (10, 28, 8/3)
params2 = (5, 20, 3)

sol1 = odeint(lorenz, s0, t, args=(params1,))
sol2 = odeint(lorenz, s0, t, args=(params2,))

fig = plt.figure(figsize=(14, 6))

# 混沌参数
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot(sol1[:, 0], sol1[:, 1], sol1[:, 2], 'r--', lw=0.8)
ax1.set_xlabel('$x$'); ax1.set_ylabel('$y$'); ax1.set_zlabel('$z$')
ax1.set_title('Chaotic ($\\sigma=10, \\rho=28, \\beta=8/3$)', fontsize=12)
ax1.view_init(elev=20, azim=45)

# 非混沌参数
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot(sol2[:, 0], sol2[:, 1], sol2[:, 2], 'b--', lw=0.8)
ax2.set_xlabel('$x$'); ax2.set_ylabel('$y$'); ax2.set_zlabel('$z$')
ax2.set_title('Regular ($\\sigma=5, \\rho=20, \\beta=3$)', fontsize=12)
ax2.view_init(elev=20, azim=45)

plt.tight_layout()
plt.savefig('lorenz_comparison.png', dpi=150)
plt.show()
