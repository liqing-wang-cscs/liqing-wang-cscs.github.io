import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])

a, b = np.polyfit(x, y, 1)
y_hat = a * x + b
rss = np.sum((y - y_hat)**2)
print(f"残差：{y - y_hat}")
print(f"残差平方和 RSS = {rss:.4f}")
