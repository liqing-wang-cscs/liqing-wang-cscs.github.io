## 马科维茨投资组合理论：数学基础部分

### 题目1. 组合风险分解与比较

<details>
<summary>问题：</summary>

给定表1中两只股票在三种经济状态下的收益率：

| 状态 | 概率 | $R_A$ (%) | $R_B$ (%) |
|------|------|-----------|-----------|
| 衰退 ($\omega_1$) | 0.4 | -10 | 20 |
| 萧条 ($\omega_2$) | 0.2 | 0 | 20 |
| 繁荣 ($\omega_3$) | 0.4 | 20 | 10 |

(1) 计算每只股票的期望收益率与方差。

(2) 对以下两种投资组合，计算其期望收益率与方差，并与单只股票的风险进行比较：
  - (a) $w_A = 0.4,\; w_B = 0.6$；
  - (b) $w_A = -0.5,\; w_B = 1.5$。

(3) 解释权重为负值时的经济含义，并说明其对组合风险与收益的影响。
</details>

<details>
<summary>解答：</summary>

**(1) 单只股票的期望与方差**

股票A的期望收益：
$$E(R_A) = 0.4 \times (-10\%) + 0.2 \times 0\% + 0.4 \times 20\% = -4\% + 0\% + 8\% = 4\%$$

股票A的方差：
$$\text{Var}(R_A) = 0.4(-10\%-4\%)^2 + 0.2(0\%-4\%)^2 + 0.4(20\%-4\%)^2$$
$$= 0.4(0.0196) + 0.2(0.0016) + 0.4(0.0256) = 0.00784 + 0.00032 + 0.01024 = 0.0184$$
标准差 $\sigma_A = \sqrt{0.0184} \approx 13.56\%$

股票B的期望收益：
$$E(R_B) = 0.4 \times 20\% + 0.2 \times 20\% + 0.4 \times 10\% = 8\% + 4\% + 4\% = 16\%$$

股票B的方差：
$$\text{Var}(R_B) = 0.4(20\%-16\%)^2 + 0.2(20\%-16\%)^2 + 0.4(10\%-16\%)^2$$
$$= 0.4(0.0016) + 0.2(0.0016) + 0.4(0.0036) = 0.00064 + 0.00032 + 0.00144 = 0.0024$$
标准差 $\sigma_B = \sqrt{0.0024} \approx 4.90\%$

两只股票的协方差：
$$\text{Cov}(R_A,R_B) = 0.4(-10\%-4\%)(20\%-16\%) + 0.2(0\%-4\%)(20\%-16\%) + 0.4(20\%-4\%)(10\%-16\%)$$
$$= 0.4(-0.14)(0.04) + 0.2(-0.04)(0.04) + 0.4(0.16)(-0.06)$$
$$= -0.00224 - 0.00032 - 0.00384 = -0.0064$$

相关系数：
$$\rho_{AB} = \frac{-0.0064}{0.1356 \times 0.0490} \approx -0.9636$$

**(2) 组合(a)：$w_A = 0.4, w_B = 0.6$**

期望收益：
$$E(R_p) = 0.4 \times 4\% + 0.6 \times 16\% = 1.6\% + 9.6\% = 11.2\%$$

方差：
$$\sigma_p^2 = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_Aw_B\text{Cov}(R_A,R_B)$$
$$= 0.4^2(0.0184) + 0.6^2(0.0024) + 2(0.4)(0.6)(-0.0064)$$
$$= 0.002944 + 0.000864 - 0.003072 = 0.000736$$
标准差 $\sigma_p = \sqrt{0.000736} \approx 2.71\%$

组合风险(2.71%)远低于单只股票A(13.56%)和股票B(4.90%)，体现了分散化的强大效果。

**(2) 组合(b)：$w_A = -0.5, w_B = 1.5$**

期望收益：
$$E(R_p) = -0.5 \times 4\% + 1.5 \times 16\% = -2\% + 24\% = 22\%$$

方差：
$$\sigma_p^2 = (-0.5)^2(0.0184) + (1.5)^2(0.0024) + 2(-0.5)(1.5)(-0.0064)$$
$$= 0.0046 + 0.0054 + 0.0096 = 0.0196$$
标准差 $\sigma_p = \sqrt{0.0196} = 14\%$

组合风险(14%)高于任一单只股票，因为负权重放大了卖空带来的杠杆风险。

**(3) 负权重的经济含义**

负权重($w_A < 0$)代表**卖空**资产A：投资者借入资产A并卖出，获得现金后投资于资产B。这种策略在资产A表现不佳时获利，但同时也放大了组合的波动性，因为卖空头寸的亏损理论上是无限的。从公式可见，负权重使协方差项对组合方差的贡献方向发生改变，可能显著增加整体风险。
</details>

---

### 题目2. 相关系数与均值-方差前沿

<details>
<summary>问题：</summary>

设随机变量 $X$ 与 $Y$ 满足：
$$E(X)=0.10,\quad \text{Var}(X)=0.05^2,\qquad E(Y)=0.04,\quad \text{Var}(Y)=0.10^2.$$

考虑线性组合 $Z_w = wX + (1-w)Y$，其中 $w \in [-1,2]$。取离散权重 $w = -1, -0.5, 0, 0.5, 1, 1.5, 2$，针对以下三种相关系数情形，分别计算并绘制 $Z_w$ 的“标准差—均值”散点图：
(1) $\rho_{X,Y} = 0$；
(2) $\rho_{X,Y} = 1$；
(3) $\rho_{X,Y} = -1$。

讨论相关系数如何影响组合的风险—收益权衡关系。
</details>

<details>
<summary>解答：</summary>

**基本公式**

组合期望收益：$\mu_w = w\mu_X + (1-w)\mu_Y = 0.10w + 0.04(1-w) = 0.04 + 0.06w$

组合方差：$\sigma_w^2 = w^2(0.05)^2 + (1-w)^2(0.10)^2 + 2w(1-w)\rho(0.05)(0.10)$

标准差：$\sigma_w = \sqrt{\sigma_w^2}$

**情形(1)：$\rho = 0$**

| $w$ | $\mu_w$ | $\sigma_w^2$ | $\sigma_w$ |
|-----|---------|--------------|------------|
| -1.0 | -0.02 | 0.0025 + 0.04 = 0.0425 | 0.2062 |
| -0.5 | 0.01 | 0.000625 + 0.0225 = 0.023125 | 0.1521 |
| 0 | 0.04 | 0 + 0.01 = 0.01 | 0.1000 |
| 0.5 | 0.07 | 0.000625 + 0.0025 = 0.003125 | 0.0559 |
| 1.0 | 0.10 | 0.0025 + 0 = 0.0025 | 0.0500 |
| 1.5 | 0.13 | 0.005625 + 0.000625 = 0.00625 | 0.0791 |
| 2.0 | 0.16 | 0.01 + 0.0025 = 0.0125 | 0.1118 |

**情形(2)：$\rho = 1$（完全正相关）**

方差公式简化为：$\sigma_w = |w \cdot 0.05 + (1-w) \cdot 0.10| = |0.10 - 0.05w|$

| $w$ | $\mu_w$ | $\sigma_w$ |
|-----|---------|------------|
| -1.0 | -0.02 | 0.15 |
| -0.5 | 0.01 | 0.125 |
| 0 | 0.04 | 0.10 |
| 0.5 | 0.07 | 0.075 |
| 1.0 | 0.10 | 0.05 |
| 1.5 | 0.13 | 0.025 |
| 2.0 | 0.16 | 0.00 |

**情形(3)：$\rho = -1$（完全负相关）**

方差公式简化为：$\sigma_w = |w \cdot 0.05 - (1-w) \cdot 0.10| = |0.15w - 0.10|$

| $w$ | $\mu_w$ | $\sigma_w$ |
|-----|---------|------------|
| -1.0 | -0.02 | 0.25 |
| -0.5 | 0.01 | 0.175 |
| 0 | 0.04 | 0.10 |
| 0.5 | 0.07 | 0.025 |
| 1.0 | 0.10 | 0.05 |
| 1.5 | 0.13 | 0.125 |
| 2.0 | 0.16 | 0.20 |

**讨论**

- **$\rho = 1$**：所有点落在连接两个资产的直线上，风险与收益呈线性关系，**无分散化收益**。
- **$\rho = -1$**：存在一个权重使方差为零（此处$w = 2/3$），实现**无风险组合**，曲线形成V形，分散化效果最强。
- **$\rho = 0$**：介于两者之间，曲线向左弯曲，表明存在分散化收益，但无法完全消除风险。

相关系数越低，均值-标准差前沿向左弯曲的程度越大，代表分散化的潜在收益越高。
</details>

---

### 题目3. 两资产组合的均值-方差解析关系

<details>
<summary>问题：</summary>

设 $X,Y$ 为两个随机变量，$Z_w = wX + (1-w)Y$，权重 $w \in \mathbb{R}$。导出 $Z_w$ 的方差 $\text{Var}(Z_w)$ 与期望 $E(Z_w)$ 之间的函数关系式（即均值-方差前沿的解析表达式），并说明该曲线的几何形状。
</details>

<details>
<summary>解答：</summary>

设 $\mu_X = E(X), \mu_Y = E(Y), \sigma_X^2 = \text{Var}(X), \sigma_Y^2 = \text{Var}(Y), \rho = \text{Corr}(X,Y)$。

组合均值：$\mu = w\mu_X + (1-w)\mu_Y$

组合方差：
$$\sigma^2 = w^2\sigma_X^2 + (1-w)^2\sigma_Y^2 + 2w(1-w)\rho\sigma_X\sigma_Y$$

从 $\mu = w\mu_X + (1-w)\mu_Y$ 解出 $w$：
$$w = \frac{\mu - \mu_Y}{\mu_X - \mu_Y} \quad (\text{假设 } \mu_X \neq \mu_Y)$$

代入方差表达式，得到 $\sigma^2$ 作为 $\mu$ 的二次函数：
$$\sigma^2 = A\mu^2 + B\mu + C$$

其中：
$$A = \frac{\sigma_X^2 - 2\rho\sigma_X\sigma_Y + \sigma_Y^2}{(\mu_X - \mu_Y)^2} > 0$$
$$B = \frac{-2\mu_Y(\sigma_X^2 - \rho\sigma_X\sigma_Y) + 2\mu_X(\rho\sigma_X\sigma_Y - \sigma_Y^2)}{(\mu_X - \mu_Y)^2}$$
$$C = \frac{\mu_Y^2\sigma_X^2 - 2\mu_X\mu_Y\rho\sigma_X\sigma_Y + \mu_X^2\sigma_Y^2}{(\mu_X - \mu_Y)^2}$$

由于 $A > 0$（除非 $\rho = 1$ 且 $\sigma_X = \sigma_Y$），$\sigma^2$ 是 $\mu$ 的开口向上的抛物线。因此，在 $(\sigma, \mu)$ 平面上，有效前沿是**双曲线**的右支（开口朝右）。特别地：

- 当 $\rho = 1$ 时，$A = 0$，前沿退化为两条直线。
- 当 $\rho = -1$ 时，存在 $\mu$ 使得 $\sigma^2 = 0$，双曲线退化为两条相交直线。

几何上，该曲线在 $(\sigma, \mu)$ 平面中是一条**向右开口的双曲线**，其顶点对应全局最小方差组合。
</details>

---

### 题目4. 多资产组合的矩阵表示

<details>
<summary>问题：</summary>

设随机向量 $\mathbf{X} = (X_1, X_2, \dots, X_n)^T$，权重向量 $\mathbf{w} = (w_1, w_2, \dots, w_n)^T$，满足 $\sum_{i=1}^n w_i = 1$。定义组合收益 $Z_{\mathbf{w}} = \mathbf{w}^T \mathbf{X}$。

(1) 用矩阵形式表示 $E(Z_{\mathbf{w}})$。

(2) 用矩阵形式表示 $\text{Var}(Z_{\mathbf{w}})$。

(3) 说明协方差矩阵的正定性在组合方差分析中的意义。
</details>

<details>
<summary>解答：</summary>

设 $\boldsymbol{\mu} = (\mu_1, \mu_2, \dots, \mu_n)^T = E(\mathbf{X})$，$\Sigma = \text{Cov}(\mathbf{X}) = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T]$。

**(1) 组合期望收益**

$$E(Z_{\mathbf{w}}) = E(\mathbf{w}^T \mathbf{X}) = \mathbf{w}^T E(\mathbf{X}) = \mathbf{w}^T \boldsymbol{\mu} = \sum_{i=1}^n w_i \mu_i$$

**(2) 组合方差**

$$\text{Var}(Z_{\mathbf{w}}) = \text{Var}(\mathbf{w}^T \mathbf{X}) = \mathbf{w}^T \text{Cov}(\mathbf{X}) \mathbf{w} = \mathbf{w}^T \Sigma \mathbf{w} = \sum_{i=1}^n \sum_{j=1}^n w_i w_j \sigma_{ij}$$

其中 $\sigma_{ij} = \text{Cov}(X_i, X_j)$。

**(3) 协方差矩阵正定性的意义**

协方差矩阵 $\Sigma$ 是**半正定**矩阵（对于任何非零向量 $\mathbf{w}$，$\mathbf{w}^T \Sigma \mathbf{w} \geq 0$）。若 $\Sigma$ 是**正定**的（即 $\mathbf{w}^T \Sigma \mathbf{w} > 0$ 对所有非零 $\mathbf{w}$ 成立），则：

- **组合方差恒为正**：除非所有资产无风险且完全相关，否则任何非零权重组合都有正风险。
- **全局最小方差组合唯一存在**：正定性保证了目标函数 $\mathbf{w}^T \Sigma \mathbf{w}$ 是严格凸函数，拉格朗日乘数法的解是唯一的。
- **矩阵可逆**：正定矩阵 $\Sigma$ 可逆，使得 $\Sigma^{-1}$ 存在，从而可以解析求解有效前沿上的组合权重。

如果 $\Sigma$ 仅半正定（存在零特征值），则可能存在多个权重给出相同的组合方差，优化问题可能有多重解。
</details>

---

### 题目5. 总体与样本的协方差矩阵

<details>
<summary>问题：</summary>

设随机向量 $(X,Y,Z)^T$。

(1) 写出其总体均值向量 $\boldsymbol{\mu}$ 和总体协方差矩阵 $\Sigma$ 的定义式。

(2) 基于容量为 $n$ 的样本 $\{(x_i, y_i, z_i)\}_{i=1}^n$，写出样本均值向量 $\hat{\boldsymbol{\mu}}$ 和样本协方差矩阵 $\hat{\Sigma}$（无偏估计形式）的计算公式。
</details>

<details>
<summary>解答：</summary>

**(1) 总体参数**

总体均值向量：
$$\boldsymbol{\mu} = E\begin{pmatrix} X \\ Y \\ Z \end{pmatrix} = \begin{pmatrix} \mu_X \\ \mu_Y \\ \mu_Z \end{pmatrix} = \begin{pmatrix} E(X) \\ E(Y) \\ E(Z) \end{pmatrix}$$

总体协方差矩阵：
$$\Sigma = \text{Cov}\begin{pmatrix} X \\ Y \\ Z \end{pmatrix} = E\left[\begin{pmatrix} X-\mu_X \\ Y-\mu_Y \\ Z-\mu_Z \end{pmatrix} \begin{pmatrix} X-\mu_X & Y-\mu_Y & Z-\mu_Z \end{pmatrix}\right]$$
$$= \begin{pmatrix}
\sigma_X^2 & \sigma_{XY} & \sigma_{XZ} \\
\sigma_{XY} & \sigma_Y^2 & \sigma_{YZ} \\
\sigma_{XZ} & \sigma_{YZ} & \sigma_Z^2
\end{pmatrix}$$

其中 $\sigma_{XY} = \text{Cov}(X,Y)$，$\sigma_{XZ} = \text{Cov}(X,Z)$，$\sigma_{YZ} = \text{Cov}(Y,Z)$。

**(2) 样本估计（无偏估计）**

样本均值向量：
$$\hat{\boldsymbol{\mu}} = \begin{pmatrix} \bar{x} \\ \bar{y} \\ \bar{z} \end{pmatrix} = \frac{1}{n} \begin{pmatrix} \sum_{i=1}^n x_i \\ \sum_{i=1}^n y_i \\ \sum_{i=1}^n z_i \end{pmatrix}$$

样本协方差矩阵（无偏估计，分母为 $n-1$）：
$$\hat{\Sigma} = \begin{pmatrix}
s_X^2 & s_{XY} & s_{XZ} \\
s_{XY} & s_Y^2 & s_{YZ} \\
s_{XZ} & s_{YZ} & s_Z^2
\end{pmatrix}$$

其中：
$$s_X^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2, \quad s_{XY} = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})$$

用矩阵形式统一表示为：
$$\hat{\Sigma} = \frac{1}{n-1} \sum_{i=1}^n (\mathbf{d}_i - \bar{\mathbf{d}})(\mathbf{d}_i - \bar{\mathbf{d}})^T$$

其中 $\mathbf{d}_i = (x_i, y_i, z_i)^T$，$\bar{\mathbf{d}} = \hat{\boldsymbol{\mu}}$。
</details>

---

### 题目6. 二次曲线与投资组合可行集

<details>
<summary>问题：</summary>

(1) 在 $(x,y)$ 平面上绘制曲线 $x = 2(y-3)^2 + 4$。

(2) 在 $(x,y)$ 平面上绘制曲线 $x^2 = 2(y-3)^2 + 4$。

(3) 讨论上述两种曲线与马科维茨有效前沿的相似性及区别。
</details>

<details>
<summary>解答：</summary>

**(1) 曲线 $x = 2(y-3)^2 + 4$**

- 这是**开口向右的抛物线**，顶点在 $(4, 3)$。
- $x$ 作为 $y$ 的二次函数：$x \geq 4$ 恒成立。
- 形状：向右开口，对称轴为 $y = 3$（水平对称轴）。
- 与马科维茨前沿的相似性：在 $(\sigma, \mu)$ 空间中，有效前沿通常是向右开口的双曲线或抛物线，此曲线形状类似，但坐标系不同（此处 $x$ 对应 $\sigma$ 或 $\sigma^2$，$y$ 对应 $\mu$）。

**(2) 曲线 $x^2 = 2(y-3)^2 + 4$**

- 改写为标准形式：$\frac{x^2}{4} - \frac{(y-3)^2}{2} = 1$。
- 这是**双曲线**，中心在 $(0, 3)$，实轴沿 $x$ 轴方向。
- 顶点：$(\pm 2, 3)$，渐近线：$y - 3 = \pm \frac{1}{\sqrt{2}}x$。
- 与马科维茨前沿的区别：该双曲线关于 $y$ 轴对称，而马科维茨有效前沿只取右支（$\sigma \geq 0$），且 $\mu$ 轴通常对应收益，不对称。

**(3) 与马科维茨有效前沿的比较**

| 特征 | 曲线(1) $x = 2(y-3)^2 + 4$ | 曲线(2) $x^2 = 2(y-3)^2 + 4$ | 马科维茨有效前沿 |
|------|---------------------------|------------------------------|------------------|
| 几何形状 | 抛物线（右开口） | 双曲线（左右两支） | 双曲线右支 |
| 变量含义 | $x$ 类似 $\sigma$，$y$ 类似 $\mu$ | $x$ 类似 $\sigma$，$y$ 类似 $\mu$ | $\sigma$（风险）与 $\mu$（收益） |
| 对称性 | 关于 $y=3$ 对称 | 关于 $y=3$ 和 $x=0$ 对称 | 无对称性（只取右支） |
| 关键点 | 顶点 $(4,3)$ | 顶点 $(\pm 2, 3)$ | 全局最小方差点 |
| 凸性 | 凸（开口方向一致） | 凸（右支） | 凸（有效前沿） |

马科维茨有效前沿本质上对应 $\sigma^2$ 与 $\mu$ 的二次关系，在 $(\sigma, \mu)$ 平面呈现双曲线右支，与曲线(2)的右支更为接近。
</details>

---

### 题目7. 二次型与最小方差组合（拉格朗日方法）

<details>
<summary>问题：</summary>

设 $\mathbf{w} = (w_1, w_2, w_3)^T$，$\Sigma = (\sigma_{ij})$ 为 $3\times 3$ 正定矩阵。

(1) 证明 $\mathbf{w}^T \Sigma \mathbf{w}$ 是 $\mathbf{w}$ 的二次型。

(2) 在约束 $\mathbf{1}^T \mathbf{w} = 1$（其中 $\mathbf{1} = (1,1,1)^T$）下，利用拉格朗日乘数法求使 $\mathbf{w}^T \Sigma \mathbf{w}$ 最小的权重 $\mathbf{w}$。

(3) 讨论 $\Sigma$ 的正定性对该优化问题解的存在性与唯一性的影响。
</details>

<details>
<summary>解答：</summary>

**(1) 证明 $\mathbf{w}^T \Sigma \mathbf{w}$ 是二次型**

展开 $\mathbf{w}^T \Sigma \mathbf{w}$：
$$\mathbf{w}^T \Sigma \mathbf{w} = \sum_{i=1}^3 \sum_{j=1}^3 w_i w_j \sigma_{ij}$$

这是所有 $w_i w_j$ 的线性组合，每一项都是 $w_i$ 的二次项（当 $i=j$）或交叉项（当 $i \neq j$）。由于 $\Sigma$ 是对称矩阵（$\sigma_{ij} = \sigma_{ji}$），该表达式可整理为：
$$\mathbf{w}^T \Sigma \mathbf{w} = \sum_{i=1}^3 \sigma_{ii} w_i^2 + 2\sum_{i<j} \sigma_{ij} w_i w_j$$

这正是二次型的一般形式，其中二次项系数为 $\sigma_{ii}$，交叉项系数为 $2\sigma_{ij}$。

**(2) 拉格朗日乘数法**

定义拉格朗日函数：
$$\mathcal{L}(\mathbf{w}, \lambda) = \mathbf{w}^T \Sigma \mathbf{w} - \lambda(\mathbf{1}^T \mathbf{w} - 1)$$

（或 $+\lambda$ 形式，符号不影响最终结果）

一阶条件（对 $\mathbf{w}$ 求导并令为零）：
$$\frac{\partial \mathcal{L}}{\partial \mathbf{w}} = 2\Sigma \mathbf{w} - \lambda \mathbf{1} = \mathbf{0}$$

因此：
$$\Sigma \mathbf{w} = \frac{\lambda}{2} \mathbf{1}$$

由于 $\Sigma$ 正定，$\Sigma$ 可逆，解得：
$$\mathbf{w} = \frac{\lambda}{2} \Sigma^{-1} \mathbf{1}$$

利用约束 $\mathbf{1}^T \mathbf{w} = 1$：
$$1 = \mathbf{1}^T \left(\frac{\lambda}{2} \Sigma^{-1} \mathbf{1}\right) = \frac{\lambda}{2} (\mathbf{1}^T \Sigma^{-1} \mathbf{1})$$

因此：
$$\frac{\lambda}{2} = \frac{1}{\mathbf{1}^T \Sigma^{-1} \mathbf{1}}$$

最终：
$$\mathbf{w}^* = \frac{\Sigma^{-1} \mathbf{1}}{\mathbf{1}^T \Sigma^{-1} \mathbf{1}}$$

**(3) 正定性的影响**

- **存在性**：对于任意正定矩阵 $\Sigma$，$\mathbf{1}^T \Sigma^{-1} \mathbf{1} > 0$（因为 $\Sigma^{-1}$ 也正定），故解总是存在。
- **唯一性**：目标函数 $\mathbf{w}^T \Sigma \mathbf{w}$ 是严格凸函数（正定性保证 Hessian 矩阵 $\Sigma$ 正定），约束是线性的，因此优化问题是严格凸优化，解**唯一存在**。
- 如果 $\Sigma$ 仅半正定，则可能有多重解或无界解，组合方差可能在某些方向为零，无法唯一确定全局最小方差组合。
</details>

---

### 题目8. 两资产组合方差的凸性分析

<details>
<summary>问题：</summary>

考虑函数
$$f(w_A, w_B) = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \rho \sigma_A \sigma_B,$$
约束为 $w_A + w_B = 1$。

(1) 将 $f$ 化为关于 $w_A$ 的单变量函数 $g(w_A)$。

(2) 求 $g'(w_A)$ 与 $g''(w_A)$。

(3) 证明当 $-1 < \rho < 1$ 时，$g''(w_A) > 0$，说明 $g$ 是凸函数，从而其驻点为全局最小值点。
</details>

<details>
<summary>解答：</summary>

**(1) 化为单变量函数**

由约束 $w_B = 1 - w_A$，代入 $f$：

$$g(w_A) = w_A^2 \sigma_A^2 + (1-w_A)^2 \sigma_B^2 + 2w_A(1-w_A)\rho \sigma_A \sigma_B$$

展开：
$$g(w_A) = w_A^2 \sigma_A^2 + (1 - 2w_A + w_A^2)\sigma_B^2 + 2(w_A - w_A^2)\rho \sigma_A \sigma_B$$
$$= \sigma_B^2 + w_A^2(\sigma_A^2 + \sigma_B^2 - 2\rho \sigma_A \sigma_B) + w_A(-2\sigma_B^2 + 2\rho \sigma_A \sigma_B)$$

**(2) 求导**

一阶导数：
$$g'(w_A) = 2w_A(\sigma_A^2 + \sigma_B^2 - 2\rho \sigma_A \sigma_B) + (-2\sigma_B^2 + 2\rho \sigma_A \sigma_B)$$
$$= 2w_A(\sigma_A^2 + \sigma_B^2 - 2\rho \sigma_A \sigma_B) + 2\rho \sigma_A \sigma_B - 2\sigma_B^2$$

二阶导数：
$$g''(w_A) = 2(\sigma_A^2 + \sigma_B^2 - 2\rho \sigma_A \sigma_B)$$

**(3) 凸性证明**

当 $-1 < \rho < 1$ 时：
$$\sigma_A^2 + \sigma_B^2 - 2\rho \sigma_A \sigma_B > \sigma_A^2 + \sigma_B^2 - 2\sigma_A \sigma_B = (\sigma_A - \sigma_B)^2 \geq 0$$

严格不等式：当 $\rho < 1$ 且 $\rho > -1$ 时，恒有：
$$\sigma_A^2 + \sigma_B^2 - 2\rho \sigma_A \sigma_B > 0$$

因此 $g''(w_A) = 2(\sigma_A^2 + \sigma_B^2 - 2\rho \sigma_A \sigma_B) > 0$。

**结论**：$g''(w_A) > 0$ 意味着 $g$ 是严格凸函数。对于严格凸函数，$g'(w_A) = 0$ 给出的驻点不仅是局部最小值，而且是**全局唯一的最小值点**。这正是马科维茨投资组合理论中分散化投资降低风险的核心数学基础。
</details>

---

### 题目9. 协方差与相关系数计算

<details>
<summary>问题：</summary>

设随机变量 $X$ 与 $Y$ 的方差分别为 $\sigma_X^2 = 25$，$\sigma_Y^2 = 36$，协方差 $\text{Cov}(X,Y) = 15$。

(1) 计算相关系数 $\rho_{XY}$。

(2) 计算 $\text{Var}(2X - 3Y)$。

(3) 若 $Z = aX + bY$，求使 $\text{Var}(Z)$ 最小的比值 $a/b$（假设 $b \neq 0$）。
</details>

<details>
<summary>解答：</summary>

**(1) 相关系数**

$$\rho_{XY} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y} = \frac{15}{\sqrt{25} \cdot \sqrt{36}} = \frac{15}{5 \times 6} = \frac{15}{30} = 0.5$$

**(2) $\text{Var}(2X - 3Y)$**

$$\text{Var}(2X - 3Y) = 2^2 \text{Var}(X) + (-3)^2 \text{Var}(Y) + 2(2)(-3)\text{Cov}(X,Y)$$
$$= 4 \times 25 + 9 \times 36 - 12 \times 15$$
$$= 100 + 324 - 180 = 244$$

**(3) 最小化 $\text{Var}(Z)$**

$$\text{Var}(Z) = a^2 \sigma_X^2 + b^2 \sigma_Y^2 + 2ab \text{Cov}(X,Y) = 25a^2 + 36b^2 + 30ab$$

令 $t = a/b$（$b \neq 0$），则：
$$\text{Var}(Z) = b^2(25t^2 + 30t + 36)$$

由于 $b^2 > 0$，问题等价于最小化 $h(t) = 25t^2 + 30t + 36$。

求导：$h'(t) = 50t + 30 = 0$，解得 $t = -0.6$。

二阶导数 $h''(t) = 50 > 0$，确为最小值。

因此最优比值：
$$\frac{a}{b} = -0.6 = -\frac{3}{5}$$

即 $a:b = -3:5$ 时，组合 $Z = -3X + 5Y$（或等价地 $Z = -0.6X + Y$）的方差最小。
</details>

---

### 题目10. 样本统计量与置信区间

<details>
<summary>问题：</summary>

某资产的历史回报率样本为：$0.08, 0.12, 0.06, 0.10, 0.14$。

(1) 计算样本均值 $\bar{x}$ 和样本方差 $s^2$（无偏估计）。

(2) 计算样本标准差 $s$。

(3) 若该资产回报率服从正态分布，利用 $t$ 分布（$t_{0.025,4} = 2.776$）估计其总体均值的 $95\%$ 置信区间。
</details>

<details>
<summary>解答：</summary>

**(1) 样本均值与样本方差**

样本容量 $n = 5$。

样本均值：
$$\bar{x} = \frac{0.08 + 0.12 + 0.06 + 0.10 + 0.14}{5} = \frac{0.50}{5} = 0.10$$

样本方差（无偏估计，分母 $n-1=4$）：
$$s^2 = \frac{1}{4} \sum_{i=1}^5 (x_i - 0.10)^2$$
$$= \frac{1}{4}[(0.08-0.10)^2 + (0.12-0.10)^2 + (0.06-0.10)^2 + (0.10-0.10)^2 + (0.14-0.10)^2]$$
$$= \frac{1}{4}[(-0.02)^2 + (0.02)^2 + (-0.04)^2 + (0)^2 + (0.04)^2]$$
$$= \frac{1}{4}[0.0004 + 0.0004 + 0.0016 + 0 + 0.0016]$$
$$= \frac{1}{4}[0.0040] = 0.0010$$

**(2) 样本标准差**

$$s = \sqrt{s^2} = \sqrt{0.0010} \approx 0.03162$$

**(3) $95\%$ 置信区间**

总体均值 $\mu$ 的 $95\%$ 置信区间公式：
$$\bar{x} \pm t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}$$

代入数据：
$$\bar{x} \pm 2.776 \times \frac{0.03162}{\sqrt{5}} = 0.10 \pm 2.776 \times 0.01414$$
$$= 0.10 \pm 0.03925$$

置信区间：
$$[0.06075, 0.13925]$$

即 $[6.075\%, 13.925\%]$。我们有 $95\%$ 的置信度认为该资产的真实期望回报率落在这一区间内。
</details>

---

### 题目11. 矩阵求逆与全局最小方差组合

<details>
<summary>问题：</summary>

给定协方差矩阵
$$\Sigma = \begin{pmatrix} 0.04 & 0.006 \\ 0.006 & 0.09 \end{pmatrix}, \quad \mathbf{1} = (1,1)^T.$$

(1) 求 $\Sigma^{-1}$。

(2) 全局最小方差组合的权重为 $\mathbf{w}_{mv} = \dfrac{\Sigma^{-1} \mathbf{1}}{\mathbf{1}^T \Sigma^{-1} \mathbf{1}}$，计算该权重向量。

(3) 验证 $\mathbf{w}_{mv}^T \mathbf{1} = 1$。
</details>

<details>
<summary>解答：</summary>

**(1) 求 $\Sigma^{-1}$**

对于 $2\times 2$ 矩阵 $\Sigma = \begin{pmatrix} a & b \\ b & d \end{pmatrix}$，逆矩阵为：
$$\Sigma^{-1} = \frac{1}{ad - b^2} \begin{pmatrix} d & -b \\ -b & a \end{pmatrix}$$

这里 $a = 0.04,\; b = 0.006,\; d = 0.09$。

行列式：
$$\det(\Sigma) = 0.04 \times 0.09 - (0.006)^2 = 0.0036 - 0.000036 = 0.003564$$

因此：
$$\Sigma^{-1} = \frac{1}{0.003564} \begin{pmatrix} 0.09 & -0.006 \\ -0.006 & 0.04 \end{pmatrix}$$
$$= \begin{pmatrix} 25.2525 & -1.6835 \\ -1.6835 & 11.2234 \end{pmatrix}$$

**(2) 全局最小方差组合**

计算 $\Sigma^{-1} \mathbf{1}$：
$$\Sigma^{-1} \mathbf{1} = \begin{pmatrix} 25.2525 & -1.6835 \\ -1.6835 & 11.2234 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 23.5690 \\ 9.5399 \end{pmatrix}$$

计算分母 $\mathbf{1}^T \Sigma^{-1} \mathbf{1}$：
$$\mathbf{1}^T \Sigma^{-1} \mathbf{1} = 23.5690 + 9.5399 = 33.1089$$

因此：
$$\mathbf{w}_{mv} = \frac{1}{33.1089} \begin{pmatrix} 23.5690 \\ 9.5399 \end{pmatrix} = \begin{pmatrix} 0.7118 \\ 0.2882 \end{pmatrix}$$

**(3) 验证权重和为1**

$$\mathbf{w}_{mv}^T \mathbf{1} = 0.7118 + 0.2882 = 1.0000$$

验证成功。该组合将约 $71.18\%$ 的资金配置于资产1，$28.82\%$ 配置于资产2，以实现全局最小方差。

**组合风险**：
$$\sigma_{mv}^2 = \mathbf{w}_{mv}^T \Sigma \mathbf{w}_{mv} = \frac{1}{\mathbf{1}^T \Sigma^{-1} \mathbf{1}} = \frac{1}{33.1089} \approx 0.03020$$
$$\sigma_{mv} \approx 0.1738$$
</details>

---

### 题目12. 风险溢价与资产定价

<details>
<summary>问题：</summary>

设某风险资产的期末现金流为随机变量 $C$，其概率密度为
$$f(c) = \frac{1}{100000}, \quad c \in [50000, 150000],$$
即服从该区间上的均匀分布。

(1) 计算期望现金流 $E(C)$。

(2) 若投资者要求的风险溢价为 $r_p$，无风险利率为 $r_f$，定价公式为
$$P = \frac{E(C)}{1 + r_f + r_p}.$$
推导该定价公式并解释其经济含义。

(3) 若 $r_f = 0.03$，且风险溢价从 $5\%$ 上升到 $10\%$，计算价格变化的百分比。
</details>

<details>
<summary>解答：</summary>

**(1) 期望现金流**

均匀分布 $C \sim U[50000, 150000]$ 的期望：
$$E(C) = \frac{50000 + 150000}{2} = \frac{200000}{2} = 100000$$

**(2) 定价公式推导**

投资者要求对风险资产的风险进行调整。将期末现金流的期望值 $E(C)$ 以**风险调整后的折现率** $r_f + r_p$ 折现到当前：

**无风险资产**：投资 $P$ 元于无风险资产，期末获得 $P(1 + r_f)$。

**风险资产**：投资 $P$ 元于风险资产，期末的期望收益为 $E(C)$。投资者要求风险资产的期望收益等于无风险收益加上风险溢价补偿：
$$E(C) = P(1 + r_f + r_p)$$

解出当前价格：
$$P = \frac{E(C)}{1 + r_f + r_p}$$

**经济含义**：风险溢价 $r_p$ 是对承担不确定性的额外补偿。风险越高（现金流波动越大），$r_p$ 越高，当前价格 $P$ 越低，这正是风险资产定价的核心逻辑。

**(3) 价格变化百分比**

当 $r_f = 0.03$，$r_p = 0.05$ 时：
$$P_1 = \frac{100000}{1 + 0.03 + 0.05} = \frac{100000}{1.08} \approx 92592.59$$

当 $r_f = 0.03$，$r_p = 0.10$ 时：
$$P_2 = \frac{100000}{1 + 0.03 + 0.10} = \frac{100000}{1.13} \approx 88495.58$$

价格变化百分比：
$$\frac{P_2 - P_1}{P_1} \times 100\% = \frac{88495.58 - 92592.59}{92592.59} \times 100\%$$
$$= \frac{-4097.01}{92592.59} \times 100\% \approx -4.42\%$$

**结论**：当风险溢价从 $5\%$ 上升到 $10\%$ 时，资产价格下降约 $4.42\%$。这反映了市场风险厌恶程度上升会导致风险资产价格下跌的金融原理。
</details>

---

<details>
<summary>知识点总结：</summary>

| 题号 | 核心数学工具 | 对应投资学概念 |
|:---:|:---|:---|
| 1 | 概率论（期望、方差、协方差、相关系数） | 两资产组合的收益与风险计算、卖空对组合风险的影响 |
| 2 | 概率论（组合收益的均值与方差）、数值计算 | 相关系数与均值-方差前沿的形状、分散化效果 |
| 3 | 代数推导（参数消元、二次函数） | 两资产均值-方差前沿的解析表达式（抛物线/双曲线） |
| 4 | 线性代数（向量与矩阵运算） | 多资产组合收益与方差的矩阵表示 |
| 5 | 数理统计（总体参数与样本估计） | 均值向量与协方差矩阵的估计方法 |
| 6 | 解析几何（抛物线、双曲线） | 有效前沿的几何直观理解 |
| 7 | 线性代数（二次型、拉格朗日乘数法、矩阵求逆） | 全局最小方差组合的解析求解 |
| 8 | 微积分（一元函数求导、二阶导数、凸性判定） | 两资产组合方差的凸性与全局最优性 |
| 9 | 概率论（协方差、方差线性性质、相关系数） | 组合方差的计算与最小化 |
| 10 | 数理统计（样本均值、无偏方差、t分布置信区间） | 风险资产期望收益的统计推断 |
| 11 | 线性代数（2×2矩阵求逆、二次型优化） | 两资产全局最小方差组合的数值计算 |
| 12 | 微积分（均匀分布期望）、概率论（期望） | 风险溢价与资产定价、折现率变化对价格的影响 |

</details>

---
