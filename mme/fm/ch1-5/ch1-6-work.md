## 课堂练习六：扩散方程与布莱克-斯科尔斯期权定价公式

### 题目1. 验证函数是否为扩散方程的解

<details>
<summary>问题：</summary>

扩散方程（热传导方程）为：

$$
\frac{\partial u}{\partial \tau} = \frac{\partial^2 u}{\partial x^2}
$$

已知函数：

$$
u(x, \tau) = \frac{1}{2\sqrt{\pi\tau}} e^{-\frac{x^2}{4\tau}}, \quad -\infty < x < +\infty, \; \tau > 0
$$

1. 求 $\frac{\partial u}{\partial \tau}$；
2. 求 $\frac{\partial^2 u}{\partial x^2}$；
3. 验证 $u(x, \tau)$ 是否满足扩散方程。

</details>

<details>
<summary>解答：</summary>

**1. 求 $\frac{\partial u}{\partial \tau}$**

令：

$$
u = \frac{1}{2\sqrt{\pi}} \tau^{-1/2} e^{-\frac{x^2}{4\tau}}
$$

对 $\tau$ 求偏导：

$$
\frac{\partial u}{\partial \tau} = \frac{1}{2\sqrt{\pi}} \left[ -\frac{1}{2}\tau^{-3/2} e^{-\frac{x^2}{4\tau}} + \tau^{-1/2} e^{-\frac{x^2}{4\tau}} \cdot \frac{x^2}{4\tau^2} \right]
$$

$$
= \frac{1}{2\sqrt{\pi}} \tau^{-3/2} e^{-\frac{x^2}{4\tau}} \left( -\frac{1}{2} + \frac{x^2}{4\tau} \right)
$$

**2. 求 $\frac{\partial^2 u}{\partial x^2}$**

先求一阶偏导：

$$
\frac{\partial u}{\partial x} = \frac{1}{2\sqrt{\pi\tau}} e^{-\frac{x^2}{4\tau}} \cdot \left( -\frac{x}{2\tau} \right) = -\frac{x}{4\sqrt{\pi}\tau^{3/2}} e^{-\frac{x^2}{4\tau}}
$$

再求二阶偏导：

$$
\frac{\partial^2 u}{\partial x^2} = -\frac{1}{4\sqrt{\pi}\tau^{3/2}} e^{-\frac{x^2}{4\tau}} + \frac{x^2}{8\sqrt{\pi}\tau^{5/2}} e^{-\frac{x^2}{4\tau}}
$$

$$
= \frac{1}{2\sqrt{\pi}} \tau^{-3/2} e^{-\frac{x^2}{4\tau}} \left( -\frac{1}{2} + \frac{x^2}{4\tau} \right)
$$

**3. 验证**

比较 $\frac{\partial u}{\partial \tau}$ 与 $\frac{\partial^2 u}{\partial x^2}$：

$$
\frac{\partial u}{\partial \tau} = \frac{\partial^2 u}{\partial x^2}
$$

因此 $u(x, \tau)$ 满足扩散方程，是扩散方程的基本解。

</details>

---

### 题目2. 由相似解方法求解半无限区间扩散方程

<details>
<summary>问题：</summary>

考虑半无限区间上的扩散方程：

$$
\frac{\partial u}{\partial \tau} = \frac{\partial^2 u}{\partial x^2}, \quad x > 0, \tau > 0
$$

初始条件：

$$
u(x, 0) = 1
$$

边界条件：

$$
u(0, \tau) = 0, \quad u \to 0 \; (x \to +\infty)
$$

设解具有相似形式 $u(x, \tau) = U(\xi)$，其中 $\xi = \frac{x}{\sqrt{\tau}}$。

1. 利用链式法则求 $\frac{\partial u}{\partial \tau}$ 和 $\frac{\partial^2 u}{\partial x^2}$；
2. 将偏微分方程化为常微分方程；
3. 求解该常微分方程并写出 $u(x, \tau)$ 的表达式。

</details>

<details>
<summary>解答：</summary>

**1. 利用链式法则求偏导数**

因为 $\xi = \frac{x}{\sqrt{\tau}}$，所以：

$$
\frac{\partial \xi}{\partial \tau} = -\frac{x}{2\tau^{3/2}} = -\frac{\xi}{2\tau}
$$

$$
\frac{\partial \xi}{\partial x} = \frac{1}{\sqrt{\tau}}
$$

于是：

$$
\frac{\partial u}{\partial \tau} = U'(\xi) \cdot \frac{\partial \xi}{\partial \tau} = -\frac{\xi}{2\tau} U'(\xi)
$$

$$
\frac{\partial u}{\partial x} = U'(\xi) \cdot \frac{1}{\sqrt{\tau}}
$$

$$
\frac{\partial^2 u}{\partial x^2} = \frac{1}{\tau} U''(\xi)
$$

**2. 化为常微分方程**

代入扩散方程：

$$
-\frac{\xi}{2\tau} U' = \frac{1}{\tau} U''
$$

两边乘以 $\tau$：

$$
-\frac{\xi}{2} U' = U''
$$

即：

$$
U'' + \frac{1}{2}\xi U' = 0
$$

**3. 求解常微分方程**

令 $V = U'$，则：

$$
V' + \frac{1}{2}\xi V = 0
$$

分离变量：

$$
\frac{V'}{V} = -\frac{1}{2}\xi
$$

积分：

$$
\ln V = -\frac{\xi^2}{4} + C
$$

$$
V = C_1 e^{-\xi^2/4}
$$

所以：

$$
U'(\xi) = C_1 e^{-\xi^2/4}
$$

再积分：

$$
U(\xi) = C_1 \int_0^\xi e^{-s^2/4} ds + C_2
$$

由边界条件 $U(0) = 1$，得 $C_2 = 1$。

由 $U(+\infty) = 0$，得：

$$
C_1 \int_0^{+\infty} e^{-s^2/4} ds + 1 = 0
$$

计算：

$$
\int_0^{+\infty} e^{-s^2/4} ds = \sqrt{\pi}
$$

所以：

$$
C_1 \sqrt{\pi} + 1 = 0 \Rightarrow C_1 = -\frac{1}{\sqrt{\pi}}
$$

因此：

$$
U(\xi) = 1 - \frac{1}{\sqrt{\pi}} \int_0^\xi e^{-s^2/4} ds = \frac{1}{\sqrt{\pi}} \int_\xi^{+\infty} e^{-s^2/4} ds
$$

代回 $\xi = \frac{x}{\sqrt{\tau}}$：

$$
u(x, \tau) = \frac{1}{\sqrt{\pi}} \int_{x/\sqrt{\tau}}^{+\infty} e^{-s^2/4} ds
$$

</details>

---

### 题目3. 由 delta 函数初始条件推导扩散方程的基本解

<details>
<summary>问题：</summary>

设扩散方程：

$$
\frac{\partial u}{\partial \tau} = \frac{\partial^2 u}{\partial x^2}
$$

的初始条件为 delta 函数：

$$
u(x, 0) = \delta(x)
$$

设解具有相似形式 $u(x, \tau) = \tau^{-1/2} U(\xi)$，其中 $\xi = \frac{x}{\sqrt{\tau}}$。

1. 求 $\frac{\partial u}{\partial \tau}$ 和 $\frac{\partial^2 u}{\partial x^2}$；
2. 化为常微分方程并求解；
3. 利用归一化条件 $\int_{-\infty}^{+\infty} u(x, \tau) dx = 1$ 确定常数，写出基本解。

</details>

<details>
<summary>解答：</summary>

**1. 求偏导数**

设 $u = \tau^{-1/2} U(\xi)$，$\xi = \frac{x}{\sqrt{\tau}}$。

$$
\frac{\partial u}{\partial \tau} = -\frac{1}{2}\tau^{-3/2} U(\xi) + \tau^{-1/2} U'(\xi) \cdot \left( -\frac{\xi}{2\tau} \right)
$$

$$
= -\frac{1}{2}\tau^{-3/2} \left[ U(\xi) + \xi U'(\xi) \right]
$$

$$
\frac{\partial u}{\partial x} = \tau^{-1/2} U'(\xi) \cdot \frac{1}{\sqrt{\tau}} = \tau^{-1} U'(\xi)
$$

$$
\frac{\partial^2 u}{\partial x^2} = \tau^{-1} U''(\xi) \cdot \frac{1}{\sqrt{\tau}} = \tau^{-3/2} U''(\xi)
$$

**2. 化为常微分方程**

代入扩散方程：

$$
-\frac{1}{2}\tau^{-3/2} \left[ U + \xi U' \right] = \tau^{-3/2} U''
$$

化简：

$$
-\frac{1}{2}(U + \xi U') = U''
$$

即：

$$
U'' + \frac{1}{2}\xi U' + \frac{1}{2}U = 0
$$

可以写成：

$$
\left( U' + \frac{1}{2}\xi U \right)' = 0
$$

积分一次：

$$
U' + \frac{1}{2}\xi U = C_1
$$

取 $C_1 = 0$（由对称性），得：

$$
U' = -\frac{1}{2}\xi U
$$

分离变量：

$$
\frac{U'}{U} = -\frac{1}{2}\xi
$$

积分：

$$
\ln U = -\frac{\xi^2}{4} + C
$$

$$
U(\xi) = C e^{-\xi^2/4}
$$

**3. 确定常数**

归一化条件：

$$
\int_{-\infty}^{+\infty} u(x, \tau) dx = 1
$$

代换 $x = \sqrt{\tau}\xi$，$dx = \sqrt{\tau} d\xi$：

$$
\int_{-\infty}^{+\infty} \tau^{-1/2} C e^{-\xi^2/4} \sqrt{\tau} d\xi = C \int_{-\infty}^{+\infty} e^{-\xi^2/4} d\xi = 1
$$

计算积分：

$$
\int_{-\infty}^{+\infty} e^{-\xi^2/4} d\xi = 2\sqrt{\pi}
$$

所以：

$$
C \cdot 2\sqrt{\pi} = 1 \Rightarrow C = \frac{1}{2\sqrt{\pi}}
$$

因此基本解为：

$$
u(x, \tau) = \frac{1}{2\sqrt{\pi\tau}} e^{-x^2/4\tau}
$$

</details>

---

### 题目4. 计算 delta 函数与光滑函数的积分

<details>
<summary>问题：</summary>

已知 delta 函数的性质：

$$
\int_{-\infty}^{+\infty} \delta(x - x_0) \Phi(x) dx = \Phi(x_0)
$$

计算下列积分：

1. $\int_{-\infty}^{+\infty} \delta(x - 3) (x^2 + 2x) dx$；
2. $\int_{0}^{5} \delta(x - 2) e^{x} dx$；
3. $\int_{-\infty}^{+\infty} \delta(x) \cos(x) dx$。

</details>

<details>
<summary>解答：</summary>

**1. $\int_{-\infty}^{+\infty} \delta(x - 3)(x^2 + 2x) dx$**

由 delta 函数性质，取 $\Phi(x) = x^2 + 2x$，$x_0 = 3$：

$$
\Phi(3) = 3^2 + 2 \times 3 = 9 + 6 = 15
$$

所以：

$$
\int_{-\infty}^{+\infty} \delta(x - 3)(x^2 + 2x) dx = 15
$$

**2. $\int_0^5 \delta(x - 2) e^x dx$**

因为 $2 \in (0, 5)$，所以：

$$
\int_0^5 \delta(x - 2) e^x dx = e^2
$$

**3. $\int_{-\infty}^{+\infty} \delta(x) \cos(x) dx$**

取 $\Phi(x) = \cos(x)$，$x_0 = 0$：

$$
\Phi(0) = \cos(0) = 1
$$

所以：

$$
\int_{-\infty}^{+\infty} \delta(x) \cos(x) dx = 1
$$

</details>

---

### 题目5. 由 Delta 函数表示不连续函数的导数

<details>
<summary>问题：</summary>

某人的财富 $M(t)$ 满足：

$$
M(t) = \begin{cases} 0, & 0 < t < t_0 \\ D_0, & t \geqslant t_0 \end{cases}
$$

1. 写出 $M(t)$ 的导数 $\frac{dM}{dt}$，用 delta 函数表示；
2. 若 $D_0 = 1000$，$t_0 = 5$，计算 $\int_0^{10} \frac{dM}{dt} dt$。

</details>

<details>
<summary>解答：</summary>

**1. 用 delta 函数表示 $\frac{dM}{dt}$**

因为 $M(t)$ 在 $t = t_0$ 处有一个大小为 $D_0$ 的跳跃，所以：

$$
\frac{dM}{dt} = D_0 \delta(t - t_0)
$$

**2. 计算积分**

$$
\int_0^{10} \frac{dM}{dt} dt = \int_0^{10} 1000 \delta(t - 5) dt = 1000
$$

因为 $5 \in (0, 10)$，所以积分结果为 $D_0 = 1000$。

</details>

---

### 题目6. 构造无风险资产组合并推导 Black-Scholes 微分方程

<details>
<summary>问题：</summary>

设股票价格 $S$ 遵循几何布朗运动：

$$
dS = \mu S dt + \sigma S dz
$$

设期权价格为 $V(S, t)$，由 Itô 引理：

$$
dV = \left( \frac{\partial V}{\partial S} \mu S + \frac{\partial V}{\partial t} + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} \sigma^2 S^2 \right) dt + \frac{\partial V}{\partial S} \sigma S dz
$$

构造投资组合：

$$
\pi = V - \delta S
$$

1. 求 $d\pi = dV - \delta dS$；
2. 选择 $\delta = \frac{\partial V}{\partial S}$，消去 $dz$ 项；
3. 由无套利条件 $d\pi = r\pi dt$，推导 Black-Scholes 微分方程。

</details>

<details>
<summary>解答：</summary>

**1. 求 $d\pi$**

$$
d\pi = dV - \delta dS
$$

代入 $dV$ 和 $dS$：

$$
d\pi = \left( \frac{\partial V}{\partial S} \mu S + \frac{\partial V}{\partial t} + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} \sigma^2 S^2 \right) dt + \frac{\partial V}{\partial S} \sigma S dz - \delta(\mu S dt + \sigma S dz)
$$

整理：

$$
d\pi = \sigma S \left( \frac{\partial V}{\partial S} - \delta \right) dz + \left[ \mu S \left( \frac{\partial V}{\partial S} - \delta \right) + \frac{\partial V}{\partial t} + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} \sigma^2 S^2 \right] dt
$$

**2. 选择 $\delta = \frac{\partial V}{\partial S}$**

代入后 $dz$ 项系数为零：

$$
d\pi = \left( \frac{\partial V}{\partial t} + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} \sigma^2 S^2 \right) dt
$$

**3. 推导 Black-Scholes 微分方程**

由无套利条件：

$$
d\pi = r\pi dt
$$

而：

$$
\pi = V - \delta S = V - \frac{\partial V}{\partial S} S
$$

所以：

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} \sigma^2 S^2 = r \left( V - \frac{\partial V}{\partial S} S \right)
$$

整理：

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0
$$

这就是 Black-Scholes 期权微分方程。

</details>

---

### 题目7. 用 Black-Scholes 公式计算欧式看涨期权价格

<details>
<summary>问题：</summary>

当前股票价格 $S = 50$ 元，欧式看涨期权的执行价格 $E = 45$ 元，无风险年利率 $r = 6\%$，期权有效期 $T - t = 0.25$ 年，股票价格波动率 $\sigma = 0.2$。

已知 Black-Scholes 公式：

$$
C(S, t) = SN(d_1) - Ee^{-r(T-t)} N(d_2)
$$

$$
d_1 = \frac{\ln(S/E) + \left( r + \frac{1}{2}\sigma^2 \right)(T-t)}{\sigma \sqrt{T-t}}
$$

$$
d_2 = d_1 - \sigma \sqrt{T-t}
$$

1. 计算 $d_1$ 和 $d_2$；
2. 查表得 $N(d_1) \approx 0.7422$，$N(d_2) \approx 0.6651$，计算期权价格 $C$。

</details>

<details>
<summary>解答：</summary>

**1. 计算 $d_1$ 和 $d_2$**

$$
\ln(S/E) = \ln(50/45) = \ln(1.1111) \approx 0.1054
$$

$$
\left( r + \frac{1}{2}\sigma^2 \right)(T-t) = (0.06 + 0.02) \times 0.25 = 0.02
$$

$$
\sigma\sqrt{T-t} = 0.2 \times 0.5 = 0.1
$$

$$
d_1 = \frac{0.1054 + 0.02}{0.1} = 1.254
$$

$$
d_2 = 1.254 - 0.1 = 1.154
$$

**2. 计算期权价格**

$$
Ee^{-r(T-t)} = 45e^{-0.06 \times 0.25} = 45e^{-0.015} \approx 45 \times 0.9851 = 44.33
$$

$$
C = 50 \times 0.7422 - 44.33 \times 0.6651
$$

$$
C = 37.11 - 29.48 = 7.63
$$

期权价格约为 **7.63 元**。

</details>

---

### 题目8. 用 Black-Scholes 公式计算欧式看跌期权价格

<details>
<summary>问题：</summary>

沿用题目 7 的数据：$S = 50$ 元，$E = 45$ 元，$r = 6\%$，$T - t = 0.25$ 年，$\sigma = 0.2$。

由 Black-Scholes 公式，欧式看跌期权价格为：

$$
P(S, t) = Ee^{-r(T-t)} N(-d_2) - SN(-d_1)
$$

已知 $N(-d_1) = 1 - N(d_1)$，$N(-d_2) = 1 - N(d_2)$，且 $N(d_1) \approx 0.7422$，$N(d_2) \approx 0.6651$。

1. 计算 $N(-d_1)$ 和 $N(-d_2)$；
2. 计算看跌期权价格 $P$；
3. 用平价公式验证：$P = C - S + Ee^{-r(T-t)}$。

</details>

<details>
<summary>解答：</summary>

**1. 计算 $N(-d_1)$ 和 $N(-d_2)$**

$$
N(-d_1) = 1 - N(d_1) = 1 - 0.7422 = 0.2578
$$

$$
N(-d_2) = 1 - N(d_2) = 1 - 0.6651 = 0.3349
$$

**2. 计算看跌期权价格**

$$
Ee^{-r(T-t)} = 45 \times e^{-0.015} \approx 44.33
$$

$$
P = 44.33 \times 0.3349 - 50 \times 0.2578
$$

$$
P = 14.85 - 12.89 = 1.96
$$

看跌期权价格约为 **1.96 元**。

**3. 用平价公式验证**

由题目 7 知 $C \approx 7.63$：

$$
P = C - S + Ee^{-r(T-t)} = 7.63 - 50 + 44.33 = 1.96
$$

与上面计算结果一致，验证成立。

</details>

---

### 题目9. 求 Black-Scholes 公式中的 $d_1$ 和 $d_2$

<details>
<summary>问题：</summary>

已知某欧式看涨期权的参数如下：

- 股票价格 $S = 100$；
- 执行价格 $E = 95$；
- 无风险利率 $r = 10\%$；
- 到期时间 $T - t = 0.25$ 年；
- 波动率 $\sigma = 0.5$。

1. 计算 $\ln(S/E)$；
2. 计算 $d_1$；
3. 计算 $d_2$。

</details>

<details>
<summary>解答：</summary>

**1. 计算 $\ln(S/E)$**

$$
\ln(S/E) = \ln(100/95) = \ln(1.0526) \approx 0.0513
$$

**2. 计算 $d_1$**

$$
d_1 = \frac{\ln(S/E) + \left( r + \frac{1}{2}\sigma^2 \right)(T-t)}{\sigma\sqrt{T-t}}
$$

$$
\left( r + \frac{1}{2}\sigma^2 \right)(T-t) = (0.1 + 0.125) \times 0.25 = 0.05625
$$

$$
\sigma\sqrt{T-t} = 0.5 \times 0.5 = 0.25
$$

$$
d_1 = \frac{0.0513 + 0.05625}{0.25} = \frac{0.10755}{0.25} = 0.4302
$$

**3. 计算 $d_2$**

$$
d_2 = d_1 - \sigma\sqrt{T-t} = 0.4302 - 0.25 = 0.1802
$$

</details>

---

### 题目10. 分析波动率对期权价格的影响

<details>
<summary>问题：</summary>

某欧式看涨期权的参数如下：

- $S = 100$，$E = 95$，$r = 0.1$，$T - t = 0.25$。

已知当 $\sigma = 0.5$ 时，$d_1 \approx 0.4302$，$d_2 \approx 0.1802$，$N(d_1) \approx 0.6664$，$N(d_2) \approx 0.5714$。

当 $\sigma = 0.6$ 时，$d_1 \approx 0.4043$，$d_2 \approx 0.1043$，$N(d_1) \approx 0.6570$，$N(d_2) \approx 0.5415$。

1. 分别计算两种波动率下的看涨期权价格；
2. 说明波动率增大对看涨期权价格的影响。

</details>

<details>
<summary>解答：</summary>

**1. 计算期权价格**

当 $\sigma = 0.5$：

$$
Ee^{-r(T-t)} = 95e^{-0.025} \approx 95 \times 0.9753 = 92.65
$$

$$
C = 100 \times 0.6664 - 92.65 \times 0.5714 = 66.64 - 52.94 = 13.70
$$

当 $\sigma = 0.6$：

$$
C = 100 \times 0.6570 - 92.65 \times 0.5415 = 65.70 - 50.17 = 15.53
$$

**2. 波动率的影响**

当波动率从 $0.5$ 增大到 $0.6$ 时，看涨期权价格从 $13.70$ 元增大到 $15.53$ 元。

结论：**波动率越大，看涨期权价格越高**。这是因为波动率越大，股票价格未来上涨的可能性越大，看涨期权的潜在收益越高，因此期权价值越高。

</details>

---

### 题目11. 解释 Black-Scholes 微分方程的含义

<details>
<summary>问题：</summary>

回答下列概念问题：

1. 写出 Black-Scholes 期权微分方程；
2. 解释方程中各项的金融含义；
3. 为什么 Black-Scholes 微分方程中不包含股票的期望收益率 $\mu$？这一事实有什么重要含义？

</details>

<details>
<summary>解答：</summary>

**1. Black-Scholes 期权微分方程**

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0
$$

**2. 各项的金融含义**

- $\frac{\partial V}{\partial t}$：期权价值随时间的变化（时间衰减）；
- $\frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}$：由股票价格波动引起的期权价值变化（凸性项）；
- $rS \frac{\partial V}{\partial S}$：由无风险利率和 Delta 对冲引起的漂移项；
- $-rV$：期权价值的无风险收益率调整项。

**3. 为什么方程中不包含 $\mu$**

在构造无风险投资组合时，通过选择 $\delta = \frac{\partial V}{\partial S}$，消去了股票随机项 $dz$，同时也消去了漂移项中的 $\mu$。

重要含义：

- 期权价格与投资者的风险偏好无关；
- 期权价格只取决于可观测的参数 $S, E, r, \sigma, T - t$；
- 可以引入风险中性定价原理：在风险中性世界中，所有资产的期望收益率都等于无风险利率 $r$。

</details>

---

### 题目12. 利用风险中性定价原理计算期权价格

<details>
<summary>问题：</summary>

设某不支付红利股票当前价格 $S = 50$ 元，欧式看涨期权执行价格 $E = 50$ 元，无风险利率 $r = 10\%$，到期时间 $T - t = 0.5$ 年，波动率 $\sigma = 0.3$。

已知 Black-Scholes 公式：

$$
C = SN(d_1) - Ee^{-r(T-t)}N(d_2)
$$

计算得 $d_1 \approx 0.3005$，$d_2 \approx 0.0884$，$N(d_1) \approx 0.6181$，$N(d_2) \approx 0.5352$。

1. 计算该欧式看涨期权的价格；
2. 用平价公式计算相应的欧式看跌期权价格；
3. 解释风险中性定价原理的核心思想。

</details>

<details>
<summary>解答：</summary>

**1. 计算看涨期权价格**

$$
Ee^{-r(T-t)} = 50e^{-0.1 \times 0.5} = 50e^{-0.05} \approx 50 \times 0.9512 = 47.56
$$

$$
C = 50 \times 0.6181 - 47.56 \times 0.5352
$$

$$
C = 30.91 - 25.46 = 5.45
$$

看涨期权价格约为 **5.45 元**。

**2. 计算看跌期权价格**

由平价公式：

$$
P = C - S + Ee^{-r(T-t)}
$$

$$
P = 5.45 - 50 + 47.56 = 3.01
$$

看跌期权价格约为 **3.01 元**。

**3. 风险中性定价原理的核心思想**

风险中性定价原理的核心思想是：

- 在风险中性世界中，所有资产的期望收益率都等于无风险利率 $r$；
- 衍生证券的价格等于其在风险中性世界中的期望回报按无风险利率折现；
- 风险中性概率不是真实的概率，而是一种等价鞅测度；
- 期权价格与投资者的风险偏好无关，只与可观测参数有关。

</details>

---