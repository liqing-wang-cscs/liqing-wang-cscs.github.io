import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False    

t = np.linspace(0, 100, 101)
k = np.log(2) / 20
u = 20 + 80 * np.exp(-k * t)
u0 = np.zeros_like(t) + 20

plt.plot(t, u, 'b-', label='水温')
plt.plot(t, u0, 'b--', label='室温')
plt.plot([0, 20, 60], [100, 60, 30], 'ro', label='观测点')
plt.xlabel('t = time (min)')
plt.ylabel('u = temperature (°C)')
plt.legend()
plt.axis([0, 100, 0, 120])
plt.show()