import numpy as np
from sklearn.metrics import r2_score

x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])
a, b = np.polyfit(x, y, 1)
y_hat = a * x + b

print(f"R² = {r2_score(y, y_hat):.4f}")
