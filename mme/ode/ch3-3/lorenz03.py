import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

sigma = 10; rho = 28; beta = 8 / 3
def lorenz(state, t):
    x, y, z = state
    return [sigma*(y-x), rho*x-y-x*z, x*y-beta*z]

np.random.seed(2)
t = np.linspace(0, 50, 5000)

# 两个接近的初始值
s01 = np.random.rand(3)
s02 = s01 + 1e-6

sol1 = odeint(lorenz, s01, t)
sol2 = odeint(lorenz, s02, t)

# 绘制 x 分量的差值
plt.figure(figsize=(10, 4))
plt.plot(t, sol1[:, 0] - sol2[:, 0], '-')
plt.xlabel('$t$', fontsize=12)
plt.ylabel('$x_1(t) - x_2(t)$', fontsize=12)
plt.title('Butterfly Effect: Divergence of Nearby Trajectories', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('butterfly_effect.png', dpi=150)
plt.show()
