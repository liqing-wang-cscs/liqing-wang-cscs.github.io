## 课堂练习五：市场有效性与伊藤引理

### 题目1. 判断有效市场的三种形式

<details>
<summary>问题：</summary>

根据哈里·罗伯茨对有效市场假设的分类，回答以下问题：

1. 弱有效市场、半强有效市场、强有效市场分别使用哪些信息？
2. 如果某投资者仅通过分析股票过去的历史价格和收益率，就能持续获得超额收益，这说明市场至少不满足哪一种有效性？
3. 如果某投资者利用公司尚未公开的内部信息进行交易并获得超额收益，这说明市场不满足哪一种有效性？

</details>

<details>
<summary>解答：</summary>

**1. 三种有效市场使用的信息**

- **弱有效市场**：只包含市场过去的历史价格和收益信息；
- **半强有效市场**：包含市场所有参与者都知道的信息，即所有公开信息；
- **强有效市场**：包含市场所有参与者都知道的信息，包括私有信息。

**2. 仅通过历史价格和收益获得超额收益**

如果投资者仅通过分析历史价格和收益率就能持续获得超额收益，说明历史价格信息尚未完全反映在当前价格中，因此市场至少不满足**弱有效市场**。

**3. 利用内部信息获得超额收益**

如果投资者利用尚未公开的内部信息进行交易并获得超额收益，说明私有信息尚未完全反映在当前价格中，因此市场不满足**强有效市场**。

</details>

---

### 题目2. 计算基本维纳过程的均值、方差与标准差

<details>
<summary>问题：</summary>

设 $Z = Z(t)$ 为基本维纳过程，即满足：

$$
\Delta z_t = \varepsilon \sqrt{\Delta t}
$$

其中 $\varepsilon \sim N(0,1)$，且不同时间间隔的 $\Delta z_t$ 相互独立。

1. 求 $\Delta z_t$ 的期望值、方差和标准差；
2. 设时间间隔 $T = 4$ 年，求 $Z(T) - Z(0)$ 的期望值、方差和标准差；
3. 若 $T = 9$ 年，重新计算 $Z(T) - Z(0)$ 的标准差，并说明标准差与时间长度之间的关系。

</details>

<details>
<summary>解答：</summary>

**1. $\Delta z_t$ 的期望值、方差和标准差**

由性质：

$$
\Delta z_t = \varepsilon \sqrt{\Delta t}
$$

因为 $\varepsilon \sim N(0,1)$，所以：

$$
E(\Delta z_t) = E(\varepsilon \sqrt{\Delta t}) = \sqrt{\Delta t} E(\varepsilon) = 0
$$

$$
\text{Var}(\Delta z_t) = \text{Var}(\varepsilon \sqrt{\Delta t}) = \Delta t \cdot \text{Var}(\varepsilon) = \Delta t \cdot 1 = \Delta t
$$

$$
\sigma(\Delta z_t) = \sqrt{\text{Var}(\Delta z_t)} = \sqrt{\Delta t}
$$

**2. 当 $T = 4$ 年时**

由基本维纳过程性质：

$$
E[Z(T) - Z(0)] = 0
$$

$$
\text{Var}[Z(T) - Z(0)] = T = 4
$$

$$
\sigma[Z(T) - Z(0)] = \sqrt{T} = \sqrt{4} = 2
$$

**3. 当 $T = 9$ 年时**

$$
E[Z(T) - Z(0)] = 0
$$

$$
\text{Var}[Z(T) - Z(0)] = 9
$$

$$
\sigma[Z(T) - Z(0)] = \sqrt{9} = 3
$$

比较可知：

- 当 $T = 4$ 时，标准差为 $2$；
- 当 $T = 9$ 时，标准差为 $3$。

标准差与时间长度 $T$ 的平方根成正比，即：

$$
\sigma[Z(T) - Z(0)] = \sqrt{T}
$$

</details>

---

### 题目3. 计算一般维纳过程的均值、方差与标准差

<details>
<summary>问题：</summary>

设变量 $x$ 遵循一般维纳过程：

$$
dx = a \, dt + b \, dz
$$

其中 $a = 3$，$b = 2$，$dz$ 为基本维纳过程。

1. 写出 $\Delta x$ 的表达式；
2. 求 $\Delta x$ 的期望值、方差和标准差；
3. 设时间间隔 $T = 5$，求 $x(T) - x(0)$ 的期望值、方差和标准差。

</details>

<details>
<summary>解答：</summary>

**1. $\Delta x$ 的表达式**

由一般维纳过程定义：

$$
dx = a \, dt + b \, dz
$$

经过一个时间增量 $\Delta t$ 后：

$$
\Delta x = a \Delta t + b \varepsilon \sqrt{\Delta t}
$$

其中 $\varepsilon \sim N(0,1)$。代入 $a = 3$，$b = 2$：

$$
\Delta x = 3 \Delta t + 2 \varepsilon \sqrt{\Delta t}
$$

**2. $\Delta x$ 的期望值、方差和标准差**

$$
E(\Delta x) = a \Delta t = 3 \Delta t
$$

$$
\text{Var}(\Delta x) = b^2 \Delta t = 2^2 \Delta t = 4 \Delta t
$$

$$
\sigma(\Delta x) = b \sqrt{\Delta t} = 2 \sqrt{\Delta t}
$$

**3. 当 $T = 5$ 时**

$$
E[x(T) - x(0)] = aT = 3 \times 5 = 15
$$

$$
\text{Var}[x(T) - x(0)] = b^2 T = 4 \times 5 = 20
$$

$$
\sigma[x(T) - x(0)] = b \sqrt{T} = 2 \sqrt{5} \approx 4.472
$$

</details>

---

### 题目4. 运用 Itô 引理求函数 $G = \ln S$ 的随机过程

<details>
<summary>问题：</summary>

设股票价格 $S$ 遵循如下 Itô 过程：

$$
dS = \mu S \, dt + \sigma S \, dz
$$

其中 $\mu$ 为股票期望收益率，$\sigma$ 为股票价格波动率，$dz$ 为基本维纳过程。

令 $G = \ln S$。请利用 Itô 引理：

$$
dG = \left( \frac{\partial G}{\partial S} \mu S + \frac{\partial G}{\partial t} + \frac{1}{2} \frac{\partial^2 G}{\partial S^2} \sigma^2 S^2 \right) dt + \frac{\partial G}{\partial S} \sigma S \, dz
$$

1. 计算 $\frac{\partial G}{\partial S}$、$\frac{\partial^2 G}{\partial S^2}$ 和 $\frac{\partial G}{\partial t}$；
2. 求出 $dG$ 的表达式；
3. 说明 $G = \ln S$ 服从什么过程，并写出其漂移率和方差率。

</details>

<details>
<summary>解答：</summary>

**1. 计算偏导数**

已知：

$$
G = \ln S
$$

$$
\frac{\partial G}{\partial S} = \frac{1}{S}
$$

$$
\frac{\partial^2 G}{\partial S^2} = -\frac{1}{S^2}
$$

$$
\frac{\partial G}{\partial t} = 0
$$

**2. 求 $dG$**

将偏导数代入 Itô 引理：

$$
dG = \left( \frac{1}{S} \mu S + 0 + \frac{1}{2} \left( -\frac{1}{S^2} \right) \sigma^2 S^2 \right) dt + \frac{1}{S} \sigma S \, dz
$$

化简：

$$
dG = \left( \mu - \frac{\sigma^2}{2} \right) dt + \sigma \, dz
$$

**3. $G = \ln S$ 服从的过程**

由上式可知，$G = \ln S$ 服从**一般维纳过程**，其：

- 漂移率为：

$$
\mu - \frac{\sigma^2}{2}
$$

- 方差率为：

$$
\sigma^2
$$

</details>

---

### 题目5. 计算股票价格对数变化的期望与方差

<details>
<summary>问题：</summary>

设某不支付红利的股票价格 $S$ 遵循几何布朗运动：

$$
dS = \mu S \, dt + \sigma S \, dz
$$

已知当前股票价格 $S = 50$ 元，期望收益率 $\mu = 0.12$，波动率 $\sigma = 0.20$，时间间隔 $T - t = 1$ 年。

1. 求 $\ln S_T - \ln S$ 的期望值和标准差；
2. 求 $S_T$ 的期望值 $E(S_T)$；
3. 求 $S_T$ 的方差 $\text{Var}(S_T)$。

</details>

<details>
<summary>解答：</summary>

已知：

- $S = 50$；
- $\mu = 0.12$；
- $\sigma = 0.20$；
- $T - t = 1$。

**1. $\ln S_T - \ln S$ 的期望值和标准差**

由公式：

$$
\ln S_T - \ln S \sim \phi \left[ \left( \mu - \frac{\sigma^2}{2} \right)(T-t), \; \sigma \sqrt{T-t} \right]
$$

期望值：

$$
E(\ln S_T - \ln S) = \left( \mu - \frac{\sigma^2}{2} \right)(T-t)
$$

$$
= \left( 0.12 - \frac{0.20^2}{2} \right) \times 1
$$

$$
= 0.12 - 0.02 = 0.10
$$

标准差：

$$
\sigma(\ln S_T - \ln S) = \sigma \sqrt{T-t} = 0.20 \times \sqrt{1} = 0.20
$$

**2. 求 $E(S_T)$**

由公式：

$$
E(S_T) = S e^{\mu(T-t)}
$$

$$
E(S_T) = 50 \times e^{0.12 \times 1}
$$

$$
E(S_T) = 50 \times e^{0.12} \approx 50 \times 1.1275 = 56.375
$$

**3. 求 $\text{Var}(S_T)$**

由公式：

$$
\text{Var}(S_T) = S^2 e^{2\mu(T-t)} \left[ e^{\sigma^2(T-t)} - 1 \right]
$$

$$
\text{Var}(S_T) = 50^2 \times e^{2 \times 0.12 \times 1} \times \left[ e^{0.20^2 \times 1} - 1 \right]
$$

$$
= 2500 \times e^{0.24} \times \left[ e^{0.04} - 1 \right]
$$

$$
\approx 2500 \times 1.2712 \times (1.0408 - 1)
$$

$$
\approx 2500 \times 1.2712 \times 0.0408
$$

$$
\approx 129.66
$$

因此：

$$
\text{Var}(S_T) \approx 129.66
$$

</details>

---

### 题目6. 计算连续复利年收益的分布参数

<details>
<summary>问题：</summary>

设某股票价格 $S$ 遵循几何布朗运动：

$$
dS = \mu S \, dt + \sigma S \, dz
$$

已知 $\mu = 0.15$，$\sigma = 0.25$，时间间隔 $T - t = 4$ 年。

设 $\eta$ 为 $t$ 与 $T$ 之间的连续复利年收益：

$$
\eta = \frac{1}{T-t} \ln \frac{S_T}{S}
$$

1. 写出 $\eta$ 服从的正态分布的均值；
2. 写出 $\eta$ 服从的正态分布的标准差；
3. 若 $\sigma = 0.40$，时间间隔 $T - t = 1$ 年，重新计算 $\eta$ 的均值和标准差。

</details>

<details>
<summary>解答：</summary>

由公式：

$$
\eta \sim \phi \left( \mu - \frac{\sigma^2}{2}, \; \frac{\sigma}{\sqrt{T-t}} \right)
$$

**1. $\eta$ 的均值**

$$
E(\eta) = \mu - \frac{\sigma^2}{2}
$$

代入 $\mu = 0.15$，$\sigma = 0.25$：

$$
E(\eta) = 0.15 - \frac{0.25^2}{2}
$$

$$
= 0.15 - \frac{0.0625}{2} = 0.15 - 0.03125 = 0.11875
$$

**2. $\eta$ 的标准差**

$$
\sigma(\eta) = \frac{\sigma}{\sqrt{T-t}}
$$

代入 $\sigma = 0.25$，$T - t = 4$：

$$
\sigma(\eta) = \frac{0.25}{\sqrt{4}} = \frac{0.25}{2} = 0.125
$$

**3. 当 $\sigma = 0.40$，$T - t = 1$ 时**

均值：

$$
E(\eta) = 0.15 - \frac{0.40^2}{2}
$$

$$
= 0.15 - \frac{0.16}{2} = 0.15 - 0.08 = 0.07
$$

标准差：

$$
\sigma(\eta) = \frac{0.40}{\sqrt{1}} = 0.40
$$

</details>

---

### 题目7. 判断随机过程类型

<details>
<summary>问题：</summary>

判断下列随机过程分别属于哪一类，并简要说明理由：

1. $dZ = \varepsilon \sqrt{dt}$，其中 $\varepsilon \sim N(0,1)$；
2. $dx = 5 \, dt + 3 \, dz$；
3. $dx = a(x,t) \, dt + b(x,t) \, dz$；
4. $dS = \mu S \, dt + \sigma S \, dz$。

备选项：基本维纳过程、一般维纳过程、Itô 过程、几何布朗运动。

</details>

<details>
<summary>解答：</summary>

**1. $dZ = \varepsilon \sqrt{dt}$**

这是**基本维纳过程**。

理由：其增量满足 $\Delta z_t = \varepsilon \sqrt{\Delta t}$，且不同时间间隔的增量相互独立，漂移率为零，方差率为 1。

**2. $dx = 5 \, dt + 3 \, dz$**

这是**一般维纳过程**。

理由：其形式为 $dx = a \, dt + b \, dz$，其中 $a = 5$，$b = 3$ 均为常数。

**3. $dx = a(x,t) \, dt + b(x,t) \, dz$**

这是 **Itô 过程**。

理由：其漂移率 $a(x,t)$ 和方差率 $b(x,t)$ 是 $x$ 和 $t$ 的函数，而不是常数。

**4. $dS = \mu S \, dt + \sigma S \, dz$**

这是**几何布朗运动**，也是一种特殊的 Itô 过程。

理由：其漂移率为 $\mu S$，方差率为 $\sigma^2 S^2$，均为 $S$ 的函数，常用于描述股票价格变动。

</details>

---

### 题目8. 利用 Itô 引理推导期权价格遵循的随机过程

<details>
<summary>问题：</summary>

设股票价格 $S$ 遵循几何布朗运动：

$$
dS = \mu S \, dt + \sigma S \, dz
$$

设某衍生证券的价格为 $V(S,t)$，且 $V$ 二次连续可微。

1. 写出 Itô 引理的一般形式；
2. 将 $dx = \mu S \, dt + \sigma S \, dz$ 代入 Itô 引理，推导 $dV$ 的表达式；
3. 指出 $dV$ 的漂移率和方差率。

</details>

<details>
<summary>解答：</summary>

**1. Itô 引理的一般形式**

设 $x$ 遵循 Itô 过程：

$$
dx = a(x,t) \, dt + b(x,t) \, dz
$$

设 $G = G(x,t)$ 二次连续可微，则：

$$
dG = \left( \frac{\partial G}{\partial x} a + \frac{\partial G}{\partial t} + \frac{1}{2} \frac{\partial^2 G}{\partial x^2} b^2 \right) dt + \frac{\partial G}{\partial x} b \, dz
$$

**2. 推导 $dV$**

令 $x = S$，$G = V$，且：

$$
a(S,t) = \mu S, \quad b(S,t) = \sigma S
$$

代入 Itô 引理：

$$
dV = \left( \frac{\partial V}{\partial S} \mu S + \frac{\partial V}{\partial t} + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} \sigma^2 S^2 \right) dt + \frac{\partial V}{\partial S} \sigma S \, dz
$$

**3. $dV$ 的漂移率和方差率**

漂移率：

$$
\frac{\partial V}{\partial S} \mu S + \frac{\partial V}{\partial t} + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} \sigma^2 S^2
$$

方差率：

$$
\left( \frac{\partial V}{\partial S} \right)^2 \sigma^2 S^2
$$

</details>

---

### 题目9. 计算股票价格超过某一水平的概率（对数正态分布应用）

<details>
<summary>问题：</summary>

设某股票当前价格 $S = 100$ 元，期望收益率 $\mu = 0.10$，波动率 $\sigma = 0.30$，时间间隔 $T - t = 1$ 年。

已知：

$$
\ln S_T \sim \phi \left[ \ln S + \left( \mu - \frac{\sigma^2}{2} \right)(T-t), \; \sigma \sqrt{T-t} \right]
$$

1. 求 $\ln S_T$ 的均值和标准差；
2. 求 $S_T > 110$ 的概率（用标准正态分布表示即可，不必查表）。

</details>

<details>
<summary>解答：</summary>

已知：

- $S = 100$；
- $\mu = 0.10$；
- $\sigma = 0.30$；
- $T - t = 1$。

**1. $\ln S_T$ 的均值和标准差**

均值：

$$
E(\ln S_T) = \ln S + \left( \mu - \frac{\sigma^2}{2} \right)(T-t)
$$

$$
= \ln 100 + \left( 0.10 - \frac{0.30^2}{2} \right) \times 1
$$

$$
= \ln 100 + (0.10 - 0.045)
$$

$$
= \ln 100 + 0.055
$$

$$
\approx 4.6052 + 0.055 = 4.6602
$$

标准差：

$$
\sigma(\ln S_T) = \sigma \sqrt{T-t} = 0.30 \times \sqrt{1} = 0.30
$$

**2. 求 $S_T > 110$ 的概率**

$$
P(S_T > 110) = P(\ln S_T > \ln 110)
$$

将 $\ln S_T$ 标准化：

$$
Z = \frac{\ln S_T - E(\ln S_T)}{\sigma(\ln S_T)}
$$

则：

$$
P(S_T > 110) = P\left( Z > \frac{\ln 110 - 4.6602}{0.30} \right)
$$

计算：

$$
\ln 110 \approx 4.7005
$$

$$
\frac{4.7005 - 4.6602}{0.30} = \frac{0.0403}{0.30} \approx 0.1343
$$

因此：

$$
P(S_T > 110) = P(Z > 0.1343) = 1 - \Phi(0.1343)
$$

其中 $\Phi(\cdot)$ 为标准正态分布的累积分布函数。

</details>

---

### 题目10. 市场有效性与马尔可夫性质的关系

<details>
<summary>问题：</summary>

回答以下概念题：

1. 什么是马尔可夫过程？它与股票价格变动的马尔可夫性质有什么关系？
2. 股票价格变动的马尔可夫性质与弱有效市场假设之间有什么联系？
3. 为什么人们通常假设股票价格遵循马尔可夫过程？
4. 维纳过程与马尔可夫过程之间是什么关系？

</details>

<details>
<summary>解答：</summary>


#### 1. 什么是马尔可夫过程？它与股票价格变动的马尔可夫性质有什么关系？

**马尔可夫过程**是一类随机过程，其核心特征是**马尔可夫性**：在已知过程当前值的条件下，过程的未来取值与它的过去取值、以及它从过去演变到现在的具体路径无关。

用条件分布严格表述：设 $\{X_t\}$ 为一随机过程，若对任意 $t$ 和任意 $s > 0$，

$$P(X_{t+s} \le x \mid X_t,\ X_u,\ u < t) = P(X_{t+s} \le x \mid X_t)$$

则称 $\{X_t\}$ 为马尔可夫过程。注意前提是"**已知当前值**"，而不是无条件地"未来与过去无关"——这是常见的表述误区。

**股票价格变动的马尔可夫性质**，是马尔可夫性在股价上的具体体现：股价的当前值已经包含了所有历史信息，**在已知当前价格的条件下**，未来价格的变动只与当前价格有关，而与过去的价格路径无关。也就是说，历史价格和价格演变的具体方式，在已知当前价格之后，不再提供任何额外的预测信息。

所以两者的关系是：股票价格的马尔可夫性质是马尔可夫过程这一般概念在股价模型中的特例；说"股价遵循马尔可夫过程"，就等价于说"股价变动具有马尔可夫性质"。

---

#### 2. 股票价格变动的马尔可夫性质与弱有效市场假设之间有什么联系？

**弱有效市场假设**（weak form of the efficient market hypothesis）认为：当前股票价格已经充分反映了**所有历史价格和交易量信息**，因此投资者无法通过分析历史价格数据获得超额收益。

这与股价的马尔可夫性质**高度一致，但侧重不同**：

- **马尔可夫性质**是一个**概率结构**上的陈述：它说的是，在已知当前价格后，历史路径对未来的条件分布没有影响。这是一种关于"信息如何进入未来预测"的刻画。
- **弱有效市场假设**是一个**经济学/市场效率**上的陈述：它说的是，历史信息已被价格吸收，所以基于历史信息的交易策略无法持续获利。

两者的联系在于：如果股价具有马尔可夫性质，那么当前价格就浓缩了历史中所有对预测未来有用的信息，历史数据不再有额外价值——这正是弱有效市场所描述的状态。因此，**股价的马尔可夫性质可以看作弱有效市场假设在随机过程层面的一种数学表达**。

但要注意方向：马尔可夫性质**不必然推出**弱有效市场（因为弱有效还涉及"无法获利"这一经济判断），弱有效市场也**不严格等价于**马尔可夫性。更准确的说法是：两者在"当前价格已包含历史信息"这一点上相互支持，弱有效市场为假设股价具有马尔可夫性提供了经济学依据。

---

#### 3. 为什么人们通常假设股票价格遵循马尔可夫过程？

主要有三个层面的理由：

**第一，与市场有效性一致。** 在一个信息传递迅速、竞争充分的市场里，历史信息会很快被价格吸收。如果过去的价格路径还能预测未来，就说明市场尚未出清，存在套利机会。竞争会迅速消除这种机会，从而让价格表现出马尔可夫性。

**第二，简化建模，且符合直觉。** 如果未来预测需要依赖整条历史路径，模型会变得极其复杂、难以处理。假设马尔可夫性后，只需知道当前价格就能刻画未来，模型从"路径依赖"降为"状态依赖"，数学上大为简化。同时，这一假设与人们观察到的市场现象——价格随机游走、难以用历史预测——大致吻合。

**第三，便于构造可处理的连续时间模型。** 在连续时间金融中，马尔可夫性是构造扩散过程（如伊藤过程）的基础。有了它，才能写出只依赖当前状态 $S_t$ 和 $t$ 的随机微分方程 $dS_t = \mu(S_t,t)\,dt + \sigma(S_t,t)\,dW_t$，进而用偏微分方程（如 Black-Scholes 方程）为衍生品定价。

需要说明的是，这只是一个**假设**，现实中股价可能有动量、反转等路径依赖现象，马尔可夫性并非严格成立。但它作为一阶近似，在理论和实务中被广泛采用。

---

#### 4. 维纳过程与马尔可夫过程之间是什么关系？

**维纳过程是马尔可夫过程的一个特例。**

- **维纳过程**（Wiener process，即布朗运动）$\{W_t\}$ 满足：$W_0 = 0$；增量独立且正态，$W_t - W_s \sim N(0, t-s)$（$s < t$）；样本路径连续。
- 由于它的**增量独立**，给定当前值 $W_t$ 后，未来增量 $W_{t+s} - W_t$ 与过去的增量无关，因此未来值 $W_{t+s}$ 只依赖 $W_t$。这就满足了马尔可夫性。

所以：**每一个维纳过程都是马尔可夫过程，但马尔可夫过程不一定是维纳过程。**

反例很多：泊松过程是马尔可夫过程，但不是维纳过程（增量服从泊松分布而非正态，路径不连续）；带漂移的布朗运动、几何布朗运动也都是马尔可夫过程，但不等于标准维纳过程。

在金融里，这个关系的意义是：股价模型常用维纳过程作为"随机源"来构造，而维纳过程本身的马尔可夫性，正好把"股价具有马尔可夫性质"这一假设落到了具体的数学对象上。

</details>
