## 均值方差模型的书后习题

### 习题3.1. 证明无卖空限制下的方差范围

<details>
<summary>习题：</summary>

3.1. 证明如果不允许卖空，投资组合收益率的方差 $\sigma^2(R_w)$ 不会超过 $\sigma^2(R_A)$ 和 $\sigma^2(R_B)$ 中的最大者。

</details>

<details>
<summary>解答：</summary>

投资组合收益率 $ R_w = w_A R_A + w_B R_B $，其中 $ w_A, w_B \ge 0 $ 且 $ w_A + w_B = 1 $。

其方差为：
$$
\sigma^2(R_w) = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_Aw_B\rho_{AB}\sigma_A\sigma_B
$$

因为 $ -1 \le \rho_{AB} \le 1 $，所以：
$$
\sigma^2(R_w) \le w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_Aw_B\sigma_A\sigma_B = (w_A\sigma_A + w_B\sigma_B)^2
$$

因此：
$$
\sigma(R_w) \le w_A\sigma_A + w_B\sigma_B \le \max(\sigma_A, \sigma_B)(w_A + w_B) = \max(\sigma_A, \sigma_B)
$$

所以 $ \sigma^2(R_w) \le [\max(\sigma_A, \sigma_B)]^2 $，即方差不会超过两者方差的最大者。

</details>

---

### 习题3.2. $ \rho_{AB} = 1 $ 时的零风险组合

<details>
<summary>习题：</summary>

2. 设 $\rho_{AB} = 1$，取 $w_A = \frac{-\sigma(R_B)}{\sigma(R_A) - \sigma(R_B)}$，$w_B = \frac{\sigma(R_A)}{\sigma(R_A) - \sigma(R_B)}$，证明 $\sigma(R_w) = 0$。

</details>

<details>
<summary>解答：</summary>

投资组合的方差为：
$$
\sigma^2(R_w) = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_Aw_B\rho_{AB}\sigma_A\sigma_B
$$

当 $ \rho_{AB} = 1 $ 时，
$$
\sigma^2(R_w) = (w_A\sigma_A + w_B\sigma_B)^2
$$

代入 $ w_A = \frac{-\sigma_B}{\sigma_A - \sigma_B} $，$ w_B = \frac{\sigma_A}{\sigma_A - \sigma_B} $, 可得
$$
w_A\sigma_A + w_B\sigma_B = -\frac{\sigma_A\sigma_B}{\sigma_A - \sigma_B} + \frac{\sigma_A\sigma_B}{\sigma_A - \sigma_B} = 0
$$

</details>

---

### 习题3.3. $ \rho_{AB} = -1 $ 时的零风险组合

<details>
<summary>习题：</summary>

3.3. 设 $\rho_{AB} = -1$，取 $w_A = \frac{\sigma(R_B)}{\sigma(R_A) + \sigma(R_B)}$，$w_B = \frac{\sigma(R_A)}{\sigma(R_A) + \sigma(R_B)}$，证明 $\sigma(R_w) = 0$。

</details>

<details>
<summary>解答：</summary>

当 $ \rho_{AB} = -1 $ 时，$ \sigma(R_w) = |w_A\sigma_A - w_B\sigma_B| $。

代入 $ w_A = \frac{\sigma_B}{\sigma_A + \sigma_B} $，$ w_B = \frac{\sigma_A}{\sigma_A + \sigma_B} $：

$$
w_A\sigma_A - w_B\sigma_B = \frac{\sigma_A\sigma_B}{\sigma_A + \sigma_B} - \frac{\sigma_A\sigma_B}{\sigma_A + \sigma_B} = 0
$$

因此 $ \sigma(R_w) = 0 $。

</details>

---

### 习题3.4. 最小方差组合的权重

<details>
<summary>习题：</summary>

3.4. 证明当 $-1 < \rho_{AB} < 1$ 时，方差最小的投资组合，在
$$
w_B = \frac{\sigma^2(R_A) - \rho_{AB}\sigma(R_A)\sigma(R_B)}{\sigma^2(R_A) + \sigma^2(R_B) - 2\rho_{AB}\sigma(R_A)\sigma(R_B)}
$$
处达到。

</details>

<details>
<summary>解答：</summary>

最小化 $ \sigma^2(R_w) = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_Aw_B\rho_{AB}\sigma_A\sigma_B $，约束 $ w_A + w_B = 1 $。

令 $ w_B = 1 - w_A $，对 $ w_A $ 求导并令其为零：

$$
\frac{d\sigma^2}{dw_A} = 2w_A\sigma_A^2 - 2(1-w_A)\sigma_B^2 + 2(1-2w_A)\rho_{AB}\sigma_A\sigma_B = 0
$$

解得：
$$
w_A = \frac{\sigma_B^2 - \rho_{AB}\sigma_A\sigma_B}{\sigma_A^2 + \sigma_B^2 - 2\rho_{AB}\sigma_A\sigma_B}
$$

因此：
$$
w_B = 1 - w_A = \frac{\sigma_A^2 - \rho_{AB}\sigma_A\sigma_B}{\sigma_A^2 + \sigma_B^2 - 2\rho_{AB}\sigma_A\sigma_B}
$$

这与题目中的公式一致。

</details>

---

### 习题3.5. 风险溢价与定价

<details>
<summary>习题：</summary>

3.5. 考虑一个风险资产组合，该组合的现金流可能为 70 000 或者 200 000，概率相等，均为 0.5。
    (1) 如果投资者要求 8% 的风险溢价，问：投资者愿意支付多少钱去购买该资产组合？该组合的期望收益率是多少？
    (2) 如果投资者要求 12% 的风险溢价，则投资者愿意支付的价格是多少？
    (3) 比较 (1) 和 (2) 的答案，分析风险溢价和价格之间的关系。

</details>

<details>
<summary>解答：</summary>

设现金流为 $ C_1 = 70000 $ 和 $ C_2 = 200000 $，概率各为0.5。

期望现金流：$ E(C) = 0.5 \times 70000 + 0.5 \times 200000 = 135000 $

(1) 风险溢价8%：投资者要求的回报率 = 无风险利率（设为0）+ 8% = 8%
$$
P = \frac{E(C)}{1.08} = \frac{135000}{1.08} = 125000
$$
期望收益率 = $ \frac{135000 - 125000}{125000} = 8\\% $

(2) 风险溢价12%：回报率 = 12%
$$
P = \frac{135000}{1.12} \approx 120535.71
$$
期望收益率 = 12%

(3) **关系**：风险溢价越高，投资者愿意支付的价格越低。两者呈**反向关系**。

</details>

---

### 习题3.6. 三股票组合的期望回报率和标准差

<details>
<summary>习题：</summary>

3.6. 计算表 3.7 所示投资组合的期望回报率和标准差。

**表 3.7 题6表**

| 股票 | 投资组合 /% | 期望回报率 /% | 标准差 | 股票间的相关系数 | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | **股票 1** | **股票 2** | **股票 3** |
| 股票 1 | 50 | 20 | 20 | 1.0 | 0.5 | 0.3 |
| 股票 2 | 30 | 15 | 30 | 0.5 | 1.0 | 0.1 |
| 股票 3 | 20 | 20 | 40 | 0.3 | 0.1 | 1.0 |

</details>

<details>
<summary>解答：</summary>

**期望回报率**：
$$
E(R_p) = 0.5 \times 20\% + 0.3 \times 15\% + 0.2 \times 20\% = 10\% + 4.5\% + 4\% = 18.5\%
$$

**方差计算**：
$$
\sigma_p^2 = \sum_{i=1}^3 \sum_{j=1}^3 w_i w_j \rho_{ij}\sigma_i\sigma_j
=\begin{pmatrix}w_1 & w_2 & w_3\end{pmatrix}
\begin{pmatrix}
\sigma_1^2 & \sigma_1\sigma_2\rho_{12} & \sigma_1\sigma_3\rho_{13} \\
\sigma_1\sigma_2\rho_{12} & \sigma_2^2 & \sigma_2\sigma_3\rho_{23} \\
\sigma_1\sigma_3\rho_{13} & \sigma_2\sigma_3\rho_{23} & \sigma_3^2 
\end{pmatrix}
\begin{pmatrix}w_1 \\ w_2 \\ w_3\end{pmatrix}
= 397.4
$$

$$
\sigma_p = \sqrt{397.4} \approx 19.93\%
$$

```python
import numpy as np

# 输入数据
weights = np.array([0.50, 0.30, 0.20])
returns = np.array([0.20, 0.15, 0.20])
std = np.array([0.20, 0.30, 0.40])

corr = np.array([
    [1.0, 0.5, 0.3],
    [0.5, 1.0, 0.1],
    [0.3, 0.1, 1.0]
])

# 计算期望回报率
Rp = np.dot(weights, returns)

# 构建协方差矩阵
cov = corr * np.outer(std, std)

# 计算方差和标准差
Vp = weights @ cov @ weights
Sp = np.sqrt(Vp)

# 输出结果
print(f"期望回报率: {Rp*100:.2f}%")
print(f"标准差: {Sp*100:.2f}%")
```

```txt
期望回报率: 18.50%
标准差: 19.93%
```

</details>

---
