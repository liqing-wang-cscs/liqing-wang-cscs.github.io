## 资本资产定价模型(CAPM)的书后习题

### 习题3.7. 计算各股票的贝塔系数

<details>
<summary>问题：</summary>

根据表 3.8 数据求每一种股票的 $\beta$ 系数。

| 股票 | 市场回报率为 -10% 的期望收益率 | 市场回报率为 +10% 的期望收益率 |
| :--- | :--- | :--- |
| A | 0 | +20 |
| B | -20 | +20 |
| C | -30 | 0 |
| D | +15 | +15 |
| E | +1 | -15 |

</details>

<details>
<summary>解答：</summary>

设市场回报率从 $-10\%$ 变到 $+10\%$，变化量为：

$$
\Delta R_m = 10\% - (-10\%) = 20\%
$$

由 CAPM 的单因子形式：

$$
R_i = R_f + \beta_i (R_m - R_f)
$$

当市场收益率变化时，股票期望收益率的变化为：

$$
\Delta R_i = \beta_i \Delta R_m
$$

所以：

$$
\beta_i = \frac{\Delta R_i}{\Delta R_m}
$$

逐个计算：

- 股票 A：

$$
\Delta R_A = 20\% - 0 = 20\%
$$

$$
\beta_A = \frac{20\%}{20\%} = 1
$$

- 股票 B：

$$
\Delta R_B = 20\% - (-20\%) = 40\%
$$

$$
\beta_B = \frac{40\%}{20\%} = 2
$$

- 股票 C：

$$
\Delta R_C = 0 - (-30\%) = 30\%
$$

$$
\beta_C = \frac{30\%}{20\%} = 1.5
$$

- 股票 D：

$$
\Delta R_D = 15\% - 15\% = 0
$$

$$
\beta_D = \frac{0}{20\%} = 0
$$

- 股票 E：

$$
\Delta R_E = -15\% - 1\% = -16\%
$$

$$
\beta_E = \frac{-16\%}{20\%} = -0.8
$$

因此：

$$
\boxed{\beta_A = 1,\quad \beta_B = 2,\quad \beta_C = 1.5,\quad \beta_D = 0,\quad \beta_E = -0.8}
$$

</details>

---

### 习题3.8. 求市场组合期望收益率、无风险利率及组合调整

<details>
<summary>问题：</summary>

设四种证券的有关数据如表 3.9 所示。投资者另有 50% 资产投资于无风险证券。

| 证券 $i$ | 期望收益率/% | $\beta_i$ | 投资比例/% |
| :--- | :--- | :--- | :--- |
| $i=1$ | 7.6 | 0.2 | 10 |
| $i=2$ | 12.4 | 0.8 | 10 |
| $i=3$ | 15.6 | 1.2 | 10 |
| $i=4$ | 18.8 | 1.6 | 20 |

(1) 求市场证券组合期望收益率 $R_M$ 和无风险利率 $R_f$。

(2) 求证券组合的 $\beta$ 系数。

(3) 若投资者可以卖所持有的无风险资产去买市场证券组合，当他希望期望收益率为 12% 时，证券组合如何？

</details>

<details>
<summary>解答：</summary>

#### (1) 求 $R_M$ 和 $R_f$

根据 CAPM：

$$
E(R_i) = R_f + \beta_i (R_M - R_f)
$$

由表中数据，任意取两组证券数据即可解出 $R_f$ 和 $R_M$。

取证券 1 和证券 2：

$$
7.6 = R_f + 0.2(R_M - R_f)
$$

$$
12.4 = R_f + 0.8(R_M - R_f)
$$

两式相减：

$$
12.4 - 7.6 = (0.8 - 0.2)(R_M - R_f)
$$

$$
4.8 = 0.6(R_M - R_f)
$$

$$
R_M - R_f = 8
$$

代入第一式：

$$
7.6 = R_f + 0.2 \times 8
$$

$$
7.6 = R_f + 1.6
$$

$$
R_f = 6
$$

因此：

$$
R_M = R_f + 8 = 14
$$

所以：

$$
\boxed{R_f = 6\%,\quad R_M = 14\%}
$$

#### (2) 求证券组合的 $\beta$ 系数

风险证券投资比例分别为：

$$
w_1 = 10\%,\quad w_2 = 10\%,\quad w_3 = 10\%,\quad w_4 = 20\%
$$

风险证券总权重为：

$$
w_{\text{risk}} = 10\% + 10\% + 10\% + 20\% = 50\%
$$

无风险证券权重为 $50\%$，其 $\beta = 0$。

因此组合的 $\beta$ 为：

$$
\beta_p = w_1\beta_1 + w_2\beta_2 + w_3\beta_3 + w_4\beta_4 + w_f \beta_f
$$

$$
\beta_p = 0.1 \times 0.2 + 0.1 \times 0.8 + 0.1 \times 1.2 + 0.2 \times 1.6 + 0.5 \times 0
$$

$$
\beta_p = 0.02 + 0.08 + 0.12 + 0.32 = 0.54
$$

所以：

$$
\boxed{\beta_p = 0.54}
$$

#### (3) 希望期望收益率为 12% 时，证券组合如何调整

原组合期望收益率为：

$$
E(R_p) = 0.1 \times 7.6 + 0.1 \times 12.4 + 0.1 \times 15.6 + 0.2 \times 18.8 + 0.5 \times 6
$$

$$
E(R_p) = 0.76 + 1.24 + 1.56 + 3.76 + 3 = 10.32\%
$$

现在投资者希望期望收益率为 $12\%$。设投资于市场证券组合的权重为 $w_M$，无风险资产权重为 $1 - w_M$。

市场证券组合期望收益率为 $R_M = 14\%$，无风险利率为 $R_f = 6\%$。

则：

$$
E(R_p) = w_M R_M + (1 - w_M) R_f
$$

$$
12\% = w_M \times 14\% + (1 - w_M) \times 6\%
$$

$$
12 = 14w_M + 6 - 6w_M
$$

$$
6 = 8w_M
$$

$$
w_M = 0.75
$$

即投资者应将 $75\%$ 的资产投资于市场证券组合，$25\%$ 投资于无风险资产。

由于原本无风险资产占 $50\%$，现在需要将无风险资产减少到 $25\%$，即卖出 $25\%$ 的无风险资产，买入市场证券组合。

调整后组合为：

$$
\boxed{w_M = 75\%,\quad w_f = 25\%}
$$

其中市场证券组合内部仍按原风险证券的相对比例配置。原风险证券总权重为 $50\%$，内部比例为：

$$
w_1 : w_2 : w_3 : w_4 = 10 : 10 : 10 : 20 = 1:1:1:2
$$

所以市场证券组合中：

$$
w_1^M = \frac{1}{5} = 20\%,\quad w_2^M = 20\%,\quad w_3^M = 20\%,\quad w_4^M = 40\%
$$

因此调整后各证券实际权重为：

$$
w_1 = 0.75 \times 20\% = 15\%
$$

$$
w_2 = 0.75 \times 20\% = 15\%
$$

$$
w_3 = 0.75 \times 20\% = 15\%
$$

$$
w_4 = 0.75 \times 40\% = 30\%
$$

$$
w_f = 25\%
$$

即：

$$
\boxed{w_1=15\%,\ w_2=15\%,\ w_3=15\%,\ w_4=30\%,\ w_f=25\%}
$$

</details>

---

### 习题3.9. 计算三证券组合的期望收益与标准差

<details>
<summary>问题：</summary>

设资产组合由 3 只证券组成，权重分别为 $w_1 = 40\%$, $w_2 = -20\%$, $w_3 = 80\%$，给定证券的期望收益 $\mu_1 = 8\%$, $\mu_2 = 10\%$, $\mu_3 = 6\%$，标准差 $\sigma_1 = 0.15$, $\sigma_2 = 0.05$, $\sigma_3 = 0.12$，相关系数 $\rho_{12} = 0.3$, $\rho_{23} = 0.0$, $\rho_{31} = -0.2$，求期望收益 $\mu_V$ 和标准差 $\sigma_V$。

</details>

<details>
<summary>解答：</summary>

#### 期望收益

$$
\mu_V = w_1\mu_1 + w_2\mu_2 + w_3\mu_3
$$

$$
\mu_V = 0.4 \times 8\% + (-0.2) \times 10\% + 0.8 \times 6\%
$$

$$
\mu_V = 3.2\% - 2\% + 4.8\% = 6\%
$$

所以：

$$
\boxed{\mu_V = 6\%}
$$

#### 标准差

组合方差为：

$$
\sigma_V^2 = \sum_{i=1}^3 \sum_{j=1}^3 w_i w_j \sigma_i \sigma_j \rho_{ij}
$$

其中 $\rho_{ii}=1$。

展开：

$$
\sigma_V^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + w_3^2\sigma_3^2 + 2w_1w_2\sigma_1\sigma_2\rho_{12} + 2w_2w_3\sigma_2\sigma_3\rho_{23} + 2w_1w_3\sigma_1\sigma_3\rho_{31}
$$

逐项计算：

$$
w_1^2\sigma_1^2 = 0.4^2 \times 0.15^2 = 0.16 \times 0.0225 = 0.0036
$$

$$
w_2^2\sigma_2^2 = (-0.2)^2 \times 0.05^2 = 0.04 \times 0.0025 = 0.0001
$$

$$
w_3^2\sigma_3^2 = 0.8^2 \times 0.12^2 = 0.64 \times 0.0144 = 0.009216
$$

交叉项：

$$
2w_1w_2\sigma_1\sigma_2\rho_{12} = 2 \times 0.4 \times (-0.2) \times 0.15 \times 0.05 \times 0.3
$$

$$
= 2 \times (-0.08) \times 0.0075 \times 0.3
$$

$$
= -0.00036
$$

$$
2w_2w_3\sigma_2\sigma_3\rho_{23} = 2 \times (-0.2) \times 0.8 \times 0.05 \times 0.12 \times 0 = 0
$$

$$
2w_1w_3\sigma_1\sigma_3\rho_{31} = 2 \times 0.4 \times 0.8 \times 0.15 \times 0.12 \times (-0.2)
$$

$$
= 2 \times 0.32 \times 0.018 \times (-0.2)
$$

$$
= -0.002304
$$

因此：

$$
\sigma_V^2 = 0.0036 + 0.0001 + 0.009216 - 0.00036 + 0 - 0.002304
$$

$$
\sigma_V^2 = 0.010252
$$

所以：

$$
\sigma_V = \sqrt{0.010252} \approx 0.10125
$$

即：

$$
\boxed{\sigma_V \approx 10.13\%}
$$

最终：

$$
\boxed{\mu_V = 6\%,\quad \sigma_V \approx 10.13\%}
$$

</details>

---

### 习题3.10. 证明组合贝塔的加权公式

<details>
<summary>问题：</summary>

证明权重为 $w_1, \cdots, w_n$ 的 $n$ 只证券构成的资产组合的贝塔因子为：

$$
\beta_p = w_1\beta_1 + \cdots + w_n\beta_n
$$

其中，$\beta_1, \cdots, \beta_n$ 是这些证券的贝塔因子。

</details>

<details>
<summary>解答：</summary>

设组合收益率为：

$$
R_p = \sum_{i=1}^n w_i R_i
$$

市场收益率为 $R_m$。根据贝塔定义：

$$
\beta_p = \frac{\mathrm{Cov}(R_p, R_m)}{\mathrm{Var}(R_m)}
$$

将 $R_p = \sum_{i=1}^n w_i R_i$ 代入：

$$
\beta_p = \frac{\mathrm{Cov}\left(\sum_{i=1}^n w_i R_i, R_m\right)}{\mathrm{Var}(R_m)}
$$

利用协方差的线性性质：

$$
\mathrm{Cov}\left(\sum_{i=1}^n w_i R_i, R_m\right)
= \sum_{i=1}^n w_i \mathrm{Cov}(R_i, R_m)
$$

因此：

$$
\beta_p = \frac{\sum_{i=1}^n w_i \mathrm{Cov}(R_i, R_m)}{\mathrm{Var}(R_m)}
$$

$$
\beta_p = \sum_{i=1}^n w_i \frac{\mathrm{Cov}(R_i, R_m)}{\mathrm{Var}(R_m)}
$$

而：

$$
\beta_i = \frac{\mathrm{Cov}(R_i, R_m)}{\mathrm{Var}(R_m)}
$$

所以：

$$
\beta_p = \sum_{i=1}^n w_i \beta_i
$$

即：

$$
\boxed{\beta_p = w_1\beta_1 + w_2\beta_2 + \cdots + w_n\beta_n}
$$

证毕。

</details>

---

### 习题3.11. 证明 CAPM 下的均衡价格公式

<details>
<summary>问题：</summary>

假定风险证券时期 1 时的随机收益为 $\tilde{y}$，而时期 0 的均衡价格为 $S_j$。假定 CAPM 成立，而证券的贝塔为 $\beta_{jm}$。证明：

$$
S_j = \frac{E[\tilde{y}]}{1+r_f+\beta_{jm}(E[\tilde{r}_m]-r_f)}
= \frac{E[\tilde{y}]-\varphi^* \cdot \rho_{jm}\sigma(\tilde{y})}{1+r_f},
$$

这里，

$$
\varphi^* = \frac{E[\tilde{y}]-r_f}{\sigma(\tilde{r}_m)}, \quad 
\rho_{jm} = \frac{\mathrm{Cov}(\tilde{y}, \tilde{r}_m)}{\sigma(\tilde{y})\sigma(\tilde{r}_m)}, \quad 
\beta_{jm} = \frac{\mathrm{Cov}(\tilde{r}_j, \tilde{r}_m)}{\sigma^2(\tilde{r}_m)}. 
$$

</details>

<details>
<summary>解答：</summary>

设证券在时期 1 的随机收益为 $\tilde{y}$，时期 0 的价格为 $S_j$，则证券的收益率为：

$$
\tilde{r}_j = \frac{\tilde{y} - S_j}{S_j}
$$

因此：

$$
E[\tilde{r}_j] = \frac{E[\tilde{y}] - S_j}{S_j}
$$

根据 CAPM：

$$
E[\tilde{r}_j] = r_f + \beta_{jm}(E[\tilde{r}_m] - r_f)
$$

于是：

$$
\frac{E[\tilde{y}] - S_j}{S_j} = r_f + \beta_{jm}(E[\tilde{r}_m] - r_f)
$$

由此可以解出：

$$
S_j = \frac{E[\tilde{y}]}{1+r_f+\beta_{jm}(E[\tilde{r}_m]-r_f)}
$$

这证明了第一等式。

接下来证明第二等式。该证券的收益率与市场收益率的协方差为：

$$
\mathrm{Cov}(\tilde{r}_j, \tilde{r}_m)
= \mathrm{Cov}\left(\frac{\tilde{y} - S_j}{S_j}, \tilde{r}_m\right)
= \frac{1}{S_j}\mathrm{Cov}(\tilde{y}, \tilde{r}_m)
$$

所以贝塔可以写为：

$$
\beta_{jm} = \frac{\mathrm{Cov}(\tilde{y}, \tilde{r}_m)}{S_j \sigma^2(\tilde{r}_m)}
$$

又因为该证券价格与市场收益率的相关系数为：

$$
\rho_{jm} = \frac{\mathrm{Cov}(\tilde{y}, \tilde{r}_m)}{\sigma(\tilde{y})\sigma(\tilde{r}_m)}
$$

所以贝塔又可以写为：

$$
\beta_{jm} = \frac{\rho_{jm}\sigma(\tilde{y})\sigma(\tilde{r}_m)}{S_j \sigma^2(\tilde{r}_m)}
= \frac{\rho_{jm}\sigma(\tilde{y})}{S_j \sigma(\tilde{r}_m)}
$$

将 $\beta_{jm}$ 代入第一等式，可得：

$$
S_j = \frac{E[\tilde{y}]}{1+r_f+\frac{\rho_{jm}\sigma(\tilde{y})}{S_j \sigma(\tilde{r}_m)}(E[\tilde{r}_m]-r_f)}
$$

将右边的分母乘到左边，可得：

$$
S_j(1+r_f) + \rho_{jm}\sigma(\tilde{y})\frac{E[\tilde{r}_m]-r_f}{\sigma(\tilde{r}_m)} = E[\tilde{y}]
$$

定义市场组合的夏普比率（Sharpe Ratio）为如下表达式：

$$
\varphi^* = \frac{E[\tilde{r}_m]-r_f}{\sigma(\tilde{r}_m)}
$$

表示每承担一单位市场风险，市场愿意支付的超额收益补偿。则：

$$
S_j(1+r_f) + \rho_{jm}\sigma(\tilde{y})\varphi^* = E[\tilde{y}]
$$

所以：

$$
S_j = \frac{E[\tilde{y}] - \varphi^* \rho_{jm}\sigma(\tilde{y})}{1+r_f}
$$

得证。这第二个表达式的含义是：资产的均衡价格等于其期望收益扣除市场风险补偿后的确定性等价，再按无风险利率贴现。

</details>

---

### 习题3.12. 求全局最小方差资产组合

<details>
<summary>问题：</summary>

假定市场上仅有两种资产，其收益率向量 $(X, Y)^T$ 和协方差矩阵 $V$ 的取值分别为

$$
V = \begin{bmatrix} 0.01 & 0 \\ 0 & 0.0064 \end{bmatrix}, \quad \begin{bmatrix} X \\ Y \end{bmatrix} = \begin{bmatrix} 0.2 \\ 0.1 \end{bmatrix}
$$

试求全局最小方差资产组合。

</details>

<details>
<summary>解答：</summary>

设组合中资产 $X$ 的权重为 $w$，资产 $Y$ 的权重为 $1-w$。

组合方差为：

$$
\sigma_p^2 = w^2 \sigma_X^2 + (1-w)^2 \sigma_Y^2 + 2w(1-w)\mathrm{Cov}(X,Y)
$$

由协方差矩阵：

$$
\sigma_X^2 = 0.01,\quad \sigma_Y^2 = 0.0064,\quad \mathrm{Cov}(X,Y)=0
$$

所以：

$$
\sigma_p^2 = 0.01w^2 + 0.0064(1-w)^2
$$

展开：

$$
\sigma_p^2 = 0.01w^2 + 0.0064(1 - 2w + w^2)
$$

$$
\sigma_p^2 = 0.01w^2 + 0.0064 - 0.0128w + 0.0064w^2
$$

$$
\sigma_p^2 = 0.0164w^2 - 0.0128w + 0.0064
$$

对 $w$ 求导并令其为零：

$$
\frac{d\sigma_p^2}{dw} = 2 \times 0.0164w - 0.0128 = 0
$$

$$
0.0328w = 0.0128
$$

$$
w = \frac{0.0128}{0.0328} = \frac{128}{328} = \frac{16}{41} \approx 0.39024
$$

因此：

$$
w_X = \frac{16}{41} \approx 39.02\%
$$

$$
w_Y = 1 - w_X = \frac{25}{41} \approx 60.98\%
$$

所以全局最小方差资产组合为：

$$
\boxed{w_X = \frac{16}{41} \approx 39.02\%,\quad w_Y = \frac{25}{41} \approx 60.98\%}
$$

此时最小方差为：

$$
\sigma_p^2 = 0.0164\left(\frac{16}{41}\right)^2 - 0.0128\left(\frac{16}{41}\right) + 0.0064
$$

计算得：

$$
\sigma_p^2 \approx 0.00390
$$

$$
\sigma_p \approx 0.06245
$$

即：

$$
\boxed{\sigma_p \approx 6.25\%}
$$

</details>

---
