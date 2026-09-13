## 资本资产定价模型（CAPM）

### 题目1. 与CAPM模型相关的概念解释

<details>
<summary>问题：</summary>

分别用1-2句话解释与CAPM模型相关的基本概念：均值—方差效用、风险厌恶、无风险资产、风险资产、投资组合、有效前沿、切点组合、资本市场线（CML）、市场投资组合、市场均衡、两基金分离定理、均衡条件 \(w_t=w_M\)、系统性风险、非系统性风险、\(\beta\) 系数、市场风险溢价、证券市场线（SML）、CAPM 定价公式、\(\alpha\)、回归形式 CAPM、夏普比率。

</details>

<details>
<summary>解答：</summary>

**均值—方差效用**：投资者只根据期望收益率和方差（或标准差）做决策，期望收益越高越好，风险越小越好。这是 CAPM 的微观基础。

**风险厌恶**：投资者在相同期望收益下偏好风险更小的组合，因此承担风险需要额外补偿。

**无风险资产**：收益率固定为 \(R_f\)、标准差为零的资产，投资者可按 \(R_f\) 自由借入或贷出。

**风险资产**：未来收益不确定、存在方差的资产，如股票、债券等。

**投资组合**：由多种资产按一定权重构成的集合，其收益和风险由各资产的收益、风险和相关性共同决定。

**有效前沿**：在均值—方差平面上，给定风险下期望收益最高、或给定期望收益下风险最低的风险资产组合集合。

**切点组合（最优风险资产组合）**：从无风险点 \((0,R_f)\) 向风险资产有效前沿作切线，切点对应的风险资产组合，其夏普比率最高。

**资本市场线（CML）**：从无风险点出发、与风险资产有效前沿相切的直线，表示加入无风险资产后所有有效组合的收益—风险关系。

**市场投资组合（市场组合）**：市场上所有资产按各自市值占总市值比例构成的组合，代表整个市场的资产配置。

**市场均衡**：每个投资者都选择最优组合，且所有资产供求相等、价格不再变动。

**两基金分离定理**：在 CAPM 假设下，所有投资者只需持有无风险资产和市场组合这两种“基金”，风险资产部分的选择完全相同。

**均衡条件 \(w_t=w_M\)**：市场均衡时，切点组合等于市场组合，即所有投资者共同持有的最优风险资产组合就是市场组合。

**系统性风险**：影响整个市场的风险，无法通过分散化消除，是 CAPM 中唯一被定价的风险。

**非系统性风险**：个别资产特有的风险，可以通过分散化消除，因此市场不给予额外回报。

**\(\beta\) 系数**：衡量资产收益率对市场组合收益率变动的敏感程度，定义为
\[
\beta_i=\frac{\operatorname{Cov}(R_i,R_M)}{\operatorname{Var}(R_M)}.
\]

**市场风险溢价**：市场组合期望收益率与无风险利率之差 \(E(R_M)-R_f\)，是风险补偿的核心来源。

**证券市场线（SML）**：CAPM 定价公式在 \(E(R)\)—\(\beta\) 平面上对应的直线：
\[
E(R_i)=R_f+\beta_i[E(R_M)-R_f].
\]

**CAPM 定价公式**：
\[
E(R_i)-R_f=\beta_i[E(R_M)-R_f],
\]
表示资产期望超额收益只由其系统性风险 \(\beta\) 决定。

**\(\alpha\)（Alpha）**：资产实际期望收益与 CAPM 预测收益之差：
\[
\alpha_i=E(R_i)-\{R_f+\beta_i[E(R_M)-R_f]\}.
\]
\(\alpha>0\) 表示被低估，\(\alpha<0\) 表示被高估。

**回归形式 CAPM**：
\[
R_i-R_f=\alpha_i+\beta_i(R_M-R_f)+\varepsilon_i,
\]
用历史数据估计 \(\beta\) 并检验 CAPM 是否成立。

**夏普比率**：
\[
S=\frac{E(R_p)-R_f}{\sigma_p},
\]
衡量单位风险所获得的超额收益，切点组合的夏普比率最高。

</details>

---

### 题目2. SML 与 CML 的区别

<details>
<summary>问题：</summary>

简述证券市场线 SML 与资本市场线 CML 的区别。

</details>

<details>
<summary>解答：</summary>

- **CML**：描述**有效组合**的期望收益与**总风险**（标准差）之间的关系。
- **SML**：描述**任意资产或组合**的期望收益与**系统性风险**（β）之间的关系。

| 维度 | CML（资本市场线） | SML（证券市场线） |
|---|---|---|
| 横轴 | 总风险 \(\sigma\)（标准差） | 系统性风险 \(\beta\) |
| 纵轴 | 期望收益率 \(E(R)\) | 期望收益率 \(E(R)\) |
| 斜率 | 夏普比率 \(\dfrac{E(R_M)-R_f}{\sigma_M}\) | 市场风险溢价 \(E(R_M)-R_f\) |
| 截距 | 无风险利率 \(R_f\) | 无风险利率 \(R_f\) |
| 适用对象 | 只有**有效组合** | **任意**资产或组合 |
| 风险度量 | 总风险，含系统性 + 非系统性 | 只含系统性风险 |
| 定价功能 | 描述有效组合的收益—风险关系 | 用于资产定价，判断高估/低估 |
| 公式 | \(E(R_p)=R_f+\dfrac{E(R_M)-R_f}{\sigma_M}\sigma_p\) | \(E(R_i)=R_f+\beta_i[E(R_M)-R_f]\) |

**联系**：两者都经过无风险点 \((R_f)\)；市场组合 \(M\) 同时位于 CML 和 SML 上；对有效组合而言，两者给出的期望收益一致。

</details>

---

### 题目3. CAPM 基本思想与核心公式

<details>
<summary>问题：</summary>

简述 CAPM（资本资产定价模型）的基本思想。写出 CAPM 的核心公式，并解释其中 \(E(R_i)\)、\(R_f\)、\(E(R_M)-R_f\)、\(\beta_i\) 的含义。进一步说明 \(\beta=1\)、\(\beta>1\)、\(0<\beta<1\)、\(\beta<0\) 分别代表什么。

</details>

<details>
<summary>解答：</summary>

CAPM 的基本思想是：一项资产承担多少系统性风险，就应获得多少预期收益。

核心公式：
\[
E(R_i)=R_f+\beta_i\big(E(R_M)-R_f\big)
\]

其中：
- \(E(R_i)\)：资产 \(i\) 的预期收益率
- \(R_f\)：无风险收益率
- \(E(R_M)-R_f\)：市场风险溢价
- \(\beta_i\)：资产对市场波动的敏感程度

\(\beta\) 的含义：
- \(\beta=1\)：风险与市场大致相同
- \(\beta>1\)：比市场波动更大，投资者要求更高回报
- \(0<\beta<1\)：比市场更稳健
- \(\beta<0\)：通常与市场反向波动

CAPM 的关键观点是：投资者只会因承担无法通过分散投资消除的“系统性风险”而获得补偿。

</details>

---

### 题目4. CAPM 预期收益率与 Alpha 计算

<details>
<summary>问题：</summary>

设无风险利率 \(R_f=3\%\)，市场组合预期收益率 \(E(R_M)=10\%\)。某股票的 \(\beta=1.4\)。
(a) 根据 CAPM 计算该股票的预期收益率。
(b) 若该股票的实际预期收益率为 \(13\%\)，计算 \(\alpha=E(R_i)-[R_f+\beta(E(R_M)-R_f)]\)，并判断该股票被高估还是低估。

</details>

<details>
<summary>解答：</summary>

**(a)** 根据 CAPM：
\[
E(R_i)=R_f+\beta[E(R_M)-R_f]=3\%+1.4\times(10\%-3\%)=3\%+9.8\%=12.8\%
\]

**(b)** 计算 \(\alpha\)：
\[
\alpha=E(R_i)-[R_f+\beta(E(R_M)-R_f)]=13\%-12.8\%=0.2\%
\]
由于 \(\alpha=0.2\%>0\)，说明该股票实际收益高于 CAPM 预测，**被低估**。

</details>

---

### 题目5. Beta 系数的计算

<details>
<summary>问题：</summary>

下表给出某资产和市场组合的 5 期超额收益率（单位：\%）：

| 期数 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 市场超额收益 \(X=R_M-R_f\) | 2 | \(-1\) | 3 | 0 | 1 |
| 资产超额收益 \(Y=R_i-R_f\) | 3 | \(-2\) | 5 | \(-1\) | 2 |

请计算 \(X\) 和 \(Y\) 的样本均值、样本协方差 \(\operatorname{Cov}(X,Y)\)、市场超额收益的样本方差 \(\operatorname{Var}(X)\)，并用
\[
\beta_i=\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)}
\]
计算该资产的 Beta 系数。

</details>

<details>
<summary>解答：</summary>

先计算均值：
\[
\bar X=\frac{2+(-1)+3+0+1}{5}=\frac{5}{5}=1
\]
\[
\bar Y=\frac{3+(-2)+5+(-1)+2}{5}=\frac{7}{5}=1.4
\]

计算离差：
\[
X-\bar X: 1,\ -2,\ 2,\ -1,\ 0
\]
\[
Y-\bar Y: 1.6,\ -3.4,\ 3.6,\ -2.4,\ 0.6
\]

样本协方差（分母用 \(n-1=4\)）：
\[
\operatorname{Cov}(X,Y)=\frac{1}{4}\sum (X_t-\bar X)(Y_t-\bar Y)
\]
\[
=\frac{1}{4}[1\times1.6+(-2)\times(-3.4)+2\times3.6+(-1)\times(-2.4)+0\times0.6]
\]
\[
=\frac{1}{4}[1.6+6.8+7.2+2.4+0]=\frac{18}{4}=4.5
\]

样本方差：
\[
\operatorname{Var}(X)=\frac{1}{4}\sum (X_t-\bar X)^2
=\frac{1}{4}[1^2+(-2)^2+2^2+(-1)^2+0^2]
=\frac{1+4+4+1+0}{4}=\frac{10}{4}=2.5
\]

因此：
\[
\beta_i=\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)}=\frac{4.5}{2.5}=1.8
\]

该资产的 Beta 系数为 **1.8**，说明其波动大于市场。

</details>

---

### 题目6. 线性回归角度推导 Beta

<details>
<summary>问题：</summary>

从线性回归角度理解 CAPM。设 \(Y=R_i-R_f,\, X=R_M-R_f\)，回归模型为 \(Y=\alpha+\beta X+\varepsilon\)。请用最小二乘法，通过最小化残差平方和
\[
S(\alpha,\beta)=\sum_{t=1}^n (Y_t-\alpha-\beta X_t)^2,
\]
推导回归斜率估计量
\[
\hat\beta=\frac{\sum_{t=1}^n (X_t-\bar X)(Y_t-\bar Y)}{\sum_{t=1}^n (X_t-\bar X)^2},
\]
并说明它为什么等于 \(\operatorname{Cov}(X,Y)/\operatorname{Var}(X)\)。最后说明 CAPM 对回归截距 \(\alpha\) 的预测是什么。

</details>

<details>
<summary>解答：</summary>

**1. 用最小二乘法估计**

对样本 \((X_t,Y_t)\)，令残差平方和为：
\[
S(\alpha,\beta)=\sum_{t=1}^{n}(Y_t-\alpha-\beta X_t)^2
\]

最小化 \(S\)，对 \(\alpha\) 求偏导可得：
\[
\hat{\alpha}=\bar Y-\hat{\beta}\bar X
\]

代回原式，并对 \(\beta\) 求偏导：
\[
\sum_{t=1}^{n}(X_t-\bar X)
\left[(Y_t-\bar Y)-\hat{\beta}(X_t-\bar X)\right]=0
\]

因此：
\[
\hat{\beta}
=
\frac{\sum_{t=1}^{n}(X_t-\bar X)(Y_t-\bar Y)}
{\sum_{t=1}^{n}(X_t-\bar X)^2}
\]

分子是 \(X\) 和 \(Y\) 的共同变动，分母是 \(X\) 自身的变动。由于样本协方差和方差中的分母相同（都是 \(n\) 或 \(n-1\)），所以：
\[
\hat{\beta}=\frac{\operatorname{Cov}(X,Y)}
{\operatorname{Var}(X)}
\]

**2. CAPM 对回归截距的预测**

回归模型说：
\[
E(R_i)-R_f=\alpha_i+\beta_i[E(R_M)-R_f]
\]

CAPM 说：
\[
E(R_i)-R_f=\beta_i[E(R_M)-R_f]
\]

两者比较，CAPM 预测：
\[
\alpha_i=0
\]

也就是说：如果 CAPM 成立，那么资产超额收益对市场超额收益回归的截距应该为零。

</details>

---

### 题目7. 残差正交、协方差与独立性

<details>
<summary>问题：</summary>

从欧氏空间和统计角度回答下列问题：

(a) 设 \(X\) 和 \(e\) 为 \(n\) 期观测向量，中心化后为 \(\tilde X\) 和 \(\tilde e\)。说明样本协方差 \(\operatorname{Cov}(X,e)=0\) 为什么等价于 \(\tilde X^T\tilde e=0\)，即两个中心化向量正交。

(b) 在带截距的线性回归中，为什么残差与解释变量正交会推出残差与解释变量的样本协方差为零？

(c) 举例说明：即使 \(e\) 与 \(1,X,X^2,X^3,\ldots\) 都不相关，也不能推出 \(e\) 与 \(X\) 独立。

</details>

<details>
<summary>解答：</summary>

**(a)** 在欧氏空间中，可以把 \(n\) 期观测值看成 \(n\) 维向量。定义中心化向量：
\[
\tilde{\mathbf X}=\mathbf X-\bar X\mathbf 1,\qquad
\tilde{\mathbf e}=\mathbf e-\bar e\mathbf 1
\]
样本协方差为：
\[
\operatorname{Cov}(X,e)
=\frac{1}{n}\sum_{t=1}^n (X_t-\bar X)(e_t-\bar e)
=\frac{1}{n}\tilde{\mathbf X}^{\mathsf T}\tilde{\mathbf e}
\]
因此：
\[
\operatorname{Cov}(X,e)=0
\quad\Longleftrightarrow\quad
\tilde{\mathbf X}^{\mathsf T}\tilde{\mathbf e}=0
\]
而两个向量内积为零，正是它们在欧氏空间中**正交**的含义。

**(b)** 带截距的回归是把因变量向量 \(\mathbf Y\) 投影到由 \(\mathbf 1,\ \mathbf X\) 张成的平面上。最小二乘法得到的残差 \(\mathbf e\) 是投影误差，因此必须垂直于整个投影空间：
\[
\mathbf e^{\mathsf T}\mathbf 1=0,\qquad
\mathbf e^{\mathsf T}\mathbf X=0
\]
第一式说明残差均值为零，即 \(\bar e=0\)。于是：
\[
\operatorname{Cov}(X,e)
=\frac{1}{n}\sum_{t=1}^n(X_t-\bar X)e_t
=\frac{1}{n}\mathbf X^{\mathsf T}\mathbf e
=0
\]
所以，回归中的“残差与解释变量正交”，在带截距时就等价于“残差与解释变量的样本协方差为零”。

**(c)** 不能。这里“与 \(1,X,X^2,\ldots\) 不相关”可理解为：
\[
E[eX^k]=0,\qquad k=0,1,2,\ldots
\]
但这通常不足以推出 \(e\) 与 \(X\) 独立。一个反例是：
\[
Y\sim N(0,1),\qquad X=e^Y,\qquad e=\sin(2\pi Y)
\]
则对任意非负整数 \(k\)：
\[
E[eX^k]
=E\left[e^{kY}\sin(2\pi Y)\right]
=C_k\sin(2\pi k)=0
\]
所以 \(e\) 与 \(X^k\) 都不相关。然而 \(e\) 是 \(X\) 的确定函数：
\[
e=\sin(2\pi\ln X)
\]
因此二者显然不独立。

</details>

---

### 题目8. 计算市场投资组合权重

<details>
<summary>问题：</summary>

假设市场上只有 3 种资产：

| 资产 | 价格 \(P_i\) | 市场上可交易数量 \(\bar N_i\) |
|---|---|---|
| 无风险资产 \(X_0\) | 1 元 | 2000 份 |
| 风险资产 \(X_1\) | 10 元 | 300 份 |
| 风险资产 \(X_2\) | 20 元 | 100 份 |

请根据
\[
\text{mkt}_i=\frac{\bar N_i P_i}{\sum_{i=0}^{2}\bar N_i P_i}
\]
计算市场投资组合中三类资产的权重 \(\text{mkt}_0,\text{mkt}_1,\text{mkt}_2\)，并解释市场投资组合的含义。

</details>

<details>
<summary>解答：</summary>

先计算各资产的市值：
\[
\text{无风险资产市值}=2000\times 1=2000
\]
\[
X_1\text{市值}=300\times 10=3000
\]
\[
X_2\text{市值}=100\times 20=2000
\]

市场总市值为：
\[
2000+3000+2000=7000
\]

因此各资产权重为：
\[
\text{mkt}_0=\frac{2000}{7000}\approx 0.2857
\]
\[
\text{mkt}_1=\frac{3000}{7000}\approx 0.4286
\]
\[
\text{mkt}_2=\frac{2000}{7000}\approx 0.2857
\]

所以市场投资组合为：
\[
\text{mkt}\approx(0.2857,\ 0.4286,\ 0.2857)^T
\]

**市场投资组合的含义**：市场投资组合是市场上所有资产按各自市值占总市值比例构成的组合，代表整个市场的资产配置。在均衡状态下，所有投资者持有的风险资产加总起来，必须等于市场上全部风险资产，因此市场组合就是“整个市场的缩影”。

</details>

---

### 题目9. 计算切点组合及其夏普比率

<details>
<summary>问题：</summary>

假设市场上只有两种风险资产。已知：
\[
E(R)=\begin{pmatrix}12\%\\18\%\end{pmatrix},\,
R_f=4\%,\,
\Sigma=\begin{pmatrix}0.04&0.01\\0.01&0.09\end{pmatrix}.
\]
请完成：

(a) 计算超额收益向量 \(E(R)-R_f I\)。

(b) 计算协方差矩阵的逆 \(\Sigma^{-1}\)。

(c) 利用切点组合公式 \(w_t\propto \Sigma^{-1}[E(R)-R_f I]\) 求切点组合方向，并将其归一化为权重 \(w_t\)。

(d) 计算该切点组合的期望收益率和夏普比率。

</details>

<details>
<summary>解答：</summary>

**(a)** 超额收益向量：
\[
E(R)-R_f I=
\begin{pmatrix}
12\%-4\%\\
18\%-4\%
\end{pmatrix}
=
\begin{pmatrix}
0.08\\
0.14
\end{pmatrix}
\]

**(b)** 协方差矩阵的逆：
\[
\Sigma^{-1}
=
\frac{1}{0.04\times 0.09-0.01^2}
\begin{pmatrix}
0.09 & -0.01\\
-0.01 & 0.04
\end{pmatrix}
=
\frac{1}{0.0035}
\begin{pmatrix}
0.09 & -0.01\\
-0.01 & 0.04
\end{pmatrix}
\]

**(c)** 计算：
\[
w_t \propto
\Sigma^{-1}[E(R)-R_f I]
=
\frac{1}{0.0035}
\begin{pmatrix}
0.09 & -0.01\\
-0.01 & 0.04
\end{pmatrix}
\begin{pmatrix}
0.08\\
0.14
\end{pmatrix}
=
\begin{pmatrix}
1.6571\\
1.3714
\end{pmatrix}
\]
归一化：
\[
1.6571+1.3714=3.0285
\]
\[
w_t=
\begin{pmatrix}
1.6571/3.0285\\
1.3714/3.0285
\end{pmatrix}
\approx
\begin{pmatrix}
0.5472\\
0.4528
\end{pmatrix}
\]

**(d)** 切点组合的期望收益率：
\[
E(R_{w_t})=w_t^T E(R)=0.5472\times 12\%+0.4528\times 18\%
\]
\[
=6.5664\%+8.1504\%=14.7168\%
\]
超额收益：
\[
E(R_{w_t})-R_f=14.7168\%-4\%=10.7168\%
\]

切点组合的方差：
\[
\sigma_t^2=w_t^T\Sigma w_t
\]
\[
=0.5472^2\times 0.04+2\times 0.5472\times 0.4528\times 0.01+0.4528^2\times 0.09
\]
\[
=0.01198+0.00496+0.01845\approx 0.03539
\]
\[
\sigma_t=\sqrt{0.03539}\approx 0.1881
\]

夏普比率：
\[
S(w_t)=\frac{E(R_{w_t})-R_f}{\sigma_t}
=\frac{10.7168\%}{18.81\%}\approx 0.570
\]

</details>

---

### 题目10. 证明切点组合的夏普比率最高

<details>
<summary>问题：</summary>

设风险资产期望收益向量为 \(\mu\)，协方差矩阵为 \(\Sigma\) 且正定，无风险利率为 \(R_f\)。任意风险资产组合权重为 \(w\)，满足 \(w^T I=1\)，其夏普比率为
\[
S(w)=\frac{w^T\mu-R_f}{\sqrt{w^T\Sigma w}}.
\]
请用柯西—施瓦茨不等式证明：
\[
S(w)\le \sqrt{(\mu-R_f I)^T\Sigma^{-1}(\mu-R_f I)},
\]
且等号成立当且仅当
\[
w\propto \Sigma^{-1}(\mu-R_f I).
\]
由此说明切点组合的夏普比率最高。

</details>

<details>
<summary>解答：</summary>

设风险资产期望收益向量为 \(\mu\)，协方差矩阵为 \(\Sigma\)，且 \(\Sigma\) 正定。无风险利率为 \(R_f\)。任意风险资产组合权重为 \(w\)，满足 \(w^T I=1\)。

夏普比率为：
\[
S(w)=\frac{w^T\mu-R_f}{\sqrt{w^T\Sigma w}}
\]

因为 \(w^T I=1\)，所以：
\[
w^T\mu-R_f=w^T\mu-R_f w^T I=w^T(\mu-R_f I)
\]

令超额收益向量：
\[
\mu_e=\mu-R_f I
\]

则：
\[
S(w)=\frac{w^T\mu_e}{\sqrt{w^T\Sigma w}}
\]

令：
\[
z=\Sigma^{1/2}w
\]

则：
\[
w^T\Sigma w=z^T z
\]

且：
\[
w^T\mu_e=(\Sigma^{-1/2}z)^T\mu_e=z^T\Sigma^{-1/2}\mu_e
\]

所以：
\[
S(w)=\frac{z^T\Sigma^{-1/2}\mu_e}{\sqrt{z^T z}}
\]

由柯西—施瓦茨不等式：
\[
z^T\Sigma^{-1/2}\mu_e
\le
\sqrt{z^T z}\sqrt{\mu_e^T\Sigma^{-1}\mu_e}
\]

因此：
\[
S(w)\le \sqrt{\mu_e^T\Sigma^{-1}\mu_e}
\]

等号成立当且仅当：
\[
z\propto \Sigma^{-1/2}\mu_e
\]

即：
\[
\Sigma^{1/2}w\propto \Sigma^{-1/2}\mu_e
\]

所以：
\[
w\propto \Sigma^{-1}\mu_e=\Sigma^{-1}(\mu-R_f I)
\]

这正是切点组合的方向。

因此，切点组合满足：
\[
w_t\propto \Sigma^{-1}(\mu-R_f I)
\]

并且对任意风险资产组合 \(w\)，都有：
\[
S(w)\le S(w_t)
\]

所以，切点组合的夏普比率最高。

</details>

---

### 题目11. 从夏普比率一阶条件证明 CAPM 公式

<details>
<summary>问题：</summary>

设切点组合为 \(w_t\)，其夏普比率最高。考虑在切点组合中加入少量资产 \(i\)，构造新组合
\[
w(\alpha)=(1-\alpha)w_t+\alpha e_i,
\]
其中 \(e_i\) 是第 \(i\) 个单位向量。利用 \(\alpha=0\) 时夏普比率取极值的一阶条件，证明：
\[
E(R_i)-R_f
=
\frac{\operatorname{Cov}(R_i,R_{w_t})}{w_t^T\Sigma w_t}
[E(R_{w_t})-R_f].
\]
写成向量形式：
\[
E(R)-R_f I
=
\frac{\Sigma w_t}{w_t^T\Sigma w_t}
[E(R_{w_t})-R_f].
\]
最后说明：当市场均衡 \(w_t=w_M\) 时，如何由此得到标准 CAPM 公式
\[
E(R_i)-R_f=\beta_i[E(R_M)-R_f].
\]
其中 \(\beta_i=\frac{\operatorname{Cov}(R_i,R_M)}{\operatorname{Var}(R_M)}.\)

</details>

<details>
<summary>解答：</summary>

设风险资产期望收益向量为 \(\mu\)，协方差矩阵为 \(\Sigma\)（正定），无风险利率为 \(R_f\)。切点组合为 \(w_t\)，满足 \(w_t^T I=1\)。

记切点组合的期望收益：
\[
\mu_t=w_t^T\mu
\]
切点组合的方差：
\[
\sigma_t^2=w_t^T\Sigma w_t
\]
其夏普比率：
\[
S(w_t)=\frac{\mu_t-R_f}{\sigma_t}
\]

**1. 构造含资产 \(i\) 的新组合**

在切点组合中加入少量资产 \(i\)：
\[
w(\alpha)=(1-\alpha)w_t+\alpha e_i
\]
其中 \(e_i\) 是第 \(i\) 个单位向量。

其期望收益为：
\[
\mu(\alpha)=w(\alpha)^T\mu
=(1-\alpha)\mu_t+\alpha\mu_i
\]
超额收益：
\[
\mu(\alpha)-R_f
=(1-\alpha)(\mu_t-R_f)+\alpha(\mu_i-R_f)
\]

其方差为：
\[
\sigma^2(\alpha)
=w(\alpha)^T\Sigma w(\alpha)
\]
展开：
\[
\sigma^2(\alpha)
=(1-\alpha)^2\sigma_t^2
+2\alpha(1-\alpha)\operatorname{Cov}(R_i,R_{w_t})
+\alpha^2\sigma_i^2
\]
其中 \(\operatorname{Cov}(R_i,R_{w_t})=e_i^T\Sigma w_t\)，\(\sigma_i^2=e_i^T\Sigma e_i\)。

**2. 夏普比率在 \(\alpha=0\) 处取极值**

新组合的夏普比率：
\[
S(\alpha)=\frac{\mu(\alpha)-R_f}{\sigma(\alpha)}
\]
因为 \(w_t\) 使夏普比率最高，所以在 \(\alpha=0\) 处 \(S(\alpha)\) 取极值，故：
\[
S'(0)=0
\]

对 \(S(\alpha)\) 求导：
\[
S'(\alpha)
=
\frac{(\mu(\alpha)-R_f)'\sigma(\alpha)
-(\mu(\alpha)-R_f)\sigma'(\alpha)}
{\sigma^2(\alpha)}
\]

在 \(\alpha=0\) 处：
\[
\sigma(0)=\sigma_t
\]
期望收益的导数：
\[
(\mu(\alpha)-R_f)'\big|_{\alpha=0}
=(\mu_i-R_f)-(\mu_t-R_f)
=\mu_i-\mu_t
\]
方差的导数：
\[
\frac{d}{d\alpha}\sigma^2(\alpha)\Big|_{\alpha=0}
=-2\sigma_t^2+2\operatorname{Cov}(R_i,R_{w_t})
\]
因此：
\[
\sigma'(\alpha)\big|_{\alpha=0}
=
\frac{\operatorname{Cov}(R_i,R_{w_t})-\sigma_t^2}{\sigma_t}
\]

**3. 代入一阶条件**

由 \(S'(0)=0\)：
\[
(\mu_i-\mu_t)\sigma_t
-(\mu_t-R_f)
\frac{\operatorname{Cov}(R_i,R_{w_t})-\sigma_t^2}{\sigma_t}
=0
\]
两边乘以 \(\sigma_t\)：
\[
(\mu_i-\mu_t)\sigma_t^2
-(\mu_t-R_f)
\left[\operatorname{Cov}(R_i,R_{w_t})-\sigma_t^2\right]
=0
\]
展开并整理：
\[
(\mu_i-\mu_t)\sigma_t^2
+(\mu_t-R_f)\sigma_t^2
=
(\mu_t-R_f)\operatorname{Cov}(R_i,R_{w_t})
\]
左边合并：
\[
(\mu_i-\mu_t+\mu_t-R_f)\sigma_t^2
=
(\mu_i-R_f)\sigma_t^2
\]
所以：
\[
(\mu_i-R_f)\sigma_t^2
=
(\mu_t-R_f)\operatorname{Cov}(R_i,R_{w_t})
\]
即：
\[
\mu_i-R_f
=
\frac{\operatorname{Cov}(R_i,R_{w_t})}{\sigma_t^2}
(\mu_t-R_f)
\]
由于 \(\sigma_t^2=w_t^T\Sigma w_t\)，\(\mu_i=E(R_i)\)，\(\mu_t=E(R_{w_t})\)，得到：
\[
E(R_i)-R_f
=
\frac{\operatorname{Cov}(R_i,R_{w_t})}{w_t^T\Sigma w_t}
[E(R_{w_t})-R_f]
\]

**4. 向量形式**

对任意资产 \(i\) 都成立，因此可以写成向量形式：
\[
E(R)-R_f I
=
\frac{\Sigma w_t}{w_t^T\Sigma w_t}
[E(R_{w_t})-R_f]
\]
其中 \(E(R)\) 是各资产期望收益向量，\(\Sigma w_t\) 的第 \(i\) 个分量正是 \(\operatorname{Cov}(R_i,R_{w_t})\)。

**5. 市场均衡时得到标准 CAPM**

市场均衡时，切点组合等于市场组合：
\[
w_t=w_M
\]
代入上式：
\[
E(R_i)-R_f
=
\frac{\operatorname{Cov}(R_i,R_M)}{\sigma_M^2}
[E(R_M)-R_f]
\]
其中 \(\sigma_M^2=w_M^T\Sigma w_M=\operatorname{Var}(R_M)\)。

因此标准 CAPM 公式为：
\[
E(R_i)-R_f=\beta_i[E(R_M)-R_f]
\]
其中
\[
\beta_i=\frac{\operatorname{Cov}(R_i,R_M)}{\operatorname{Var}(R_M)}
\]

</details>

---
