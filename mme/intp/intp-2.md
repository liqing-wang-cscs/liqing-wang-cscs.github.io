# 一维插值的概念与方法

---

## 问1. 拉格朗日插值的基本思想

<details>
<summary>问题：</summary>
已知三个点 \((0,1)\)、\((1,2)\)、\((2,5)\)，如何用一个二次多项式同时穿过这三个点？拉格朗日插值是怎么构造这个多项式的？
</details>

<details>
<summary>解答：</summary>
拉格朗日插值的基本思想是：对每个节点构造一个“基函数”，该基函数在自己节点处为 1，在其他节点处为 0，然后把所有基函数按函数值加权求和。

对于节点 \(x_0=0, x_1=1, x_2=2\)，三个基函数为：
\[
L_0(x)=\frac{(x-1)(x-2)}{(0-1)(0-2)}, \quad
L_1(x)=\frac{(x-0)(x-2)}{(1-0)(1-2)}, \quad 
L_2(x)=\frac{(x-0)(x-1)}{(2-0)(2-1)}. 
\]
插值多项式为
\[
P(x)=1·L_0(x)+2·L_1(x)+5·L_2(x)=x^2+1. 
\]

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x = np.array([0, 1, 2])
y = np.array([1, 2, 5])
poly = lagrange(x, y)
print(poly)  # 输出二次多项式系数

xs = np.linspace(-0.5, 2.5, 100)
plt.scatter(x, y, color='red')
plt.plot(xs, poly(xs))
plt.title("Lagrange Interpolation")
plt.grid(True)
plt.show()
```

<img src='/mme/intp/python/intp-prob-1.png'>

</details>

---

## 问2. 什么是差商、什么是差商表

<details>
<summary>问题：</summary>
牛顿插值中的差商 \(f[x_0,x_1]\)、\(f[x_0,x_1,x_2]\) 是怎么定义的？
以问1中的三个点 \((0,1)\)、\((1,2)\)、\((2,5)\) 为例，逐步计算差商表。
如何用代码计算差商表？
</details>

<details>
<summary>解答：</summary>
一阶差商定义为
\[
f[x_i,x_j]=\frac{f(x_j)-f(x_i)}{x_j-x_i},
\]
例如
\[
f[x_0,x_1]=\frac{f(x_1)-f(x_0)}{x_1-x_0},
\]

高阶差商递归定义，例如
\[
f[x_0,x_1,x_2]=\frac{f[x_1,x_2]-f[x_0,x_1]}{x_2-x_0}.
\]

以问1中的三个点 \((0,1)\)、\((1,2)\)、\((2,5)\) 为例，逐步计算差商表：

**第 0 列：自变量的值**
\[
x_0=0,\quad x_1=1,\quad x_2=2.
\]

**第 1 列：函数值**
\[
f[x_0]=1,\quad f[x_1]=2,\quad f[x_2]=5.
\]

**第 2 列：一阶差商**
\[
f[x_0,x_1]=\frac{2-1}{1-0}=1,
\]
\[
f[x_1,x_2]=\frac{5-2}{2-1}=3,
\]

**第 3 列：二阶差商**
\[
f[x_0,x_1,x_2]=\frac{f[x_1,x_2]-f[x_0,x_1]}{x_2-x_0}=\frac{3-1}{2-0}=1.
\]

整理成差商表：

| \(x_i\) | \(f[x_i]\) | 一阶差商 | 二阶差商 |
|---|---|---|---|
| 0 | 1 | 1 | 1 |
| 1 | 2 | 3 |   |
| 2 | 5 |   |   |

表中每个右上方的值都由其左下方的两个相邻值计算而来。例如 \(f[x_0,x_1,x_2]=1\) 位于第 0 行第 2 列，它由第 1 行第 1 列的 \(f[x_1,x_2]=3\) 与第 0 行第 1 列的 \(f[x_0,x_1]=1\) 作差再除以 \(x_2-x_0=2\) 得到。

```python
import numpy as np

def divided_diff_table(x, y):
    n = len(x)
    table = np.zeros((n, n))
    table[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i+1, j-1] - table[i, j-1]) / (x[i+j] - x[i])
    return table

x = np.array([0, 1, 2])
y = np.array([1, 2, 5])
table = divided_diff_table(x, y)
print("差商表：")
print(table)
```

运行结果：

```
差商表：
[[0. 1. 1. 1.]
 [1. 2. 3. 0.]
 [2. 5. 0. 0.]]
```

其中第0列是自变量取值，第1列是函数值，第2列是一阶差商，第3列是二阶差商。
牛顿插值多项式的系数就取差商表第一行（第0列除外）：
\[
P(x)=1+1\cdot(x-0)+1\cdot(x-0)(x-1)=x^2+1,
\]
与问1中的拉格朗日插值的结果一致。
</details>

---

## 问3. 牛顿插值为什么适合逐步增加节点

<details>
<summary>问题：</summary>
在问1中，已经用 \((0,1)\)、\((1,2)\)、\((2,5)\) 三个点做了插值多项式 \(P(x)=x^2+1\)。现在又新增一个点 \((3,12)\)，是否需要从头重新计算？牛顿插值的形式有什么优势？
</details>

<details>
<summary>解答：</summary>
不需要从头重新计算。牛顿插值把多项式写成“差商形式”：
\[
P(x)=f[x_0]+f[x_0,x_1](x-x_0)+f[x_0,x_1,x_2](x-x_0)(x-x_1)+\cdots
\]
当从 3 个点增加到 4 个点时，原来的低阶项 \(f[x_0]\)、\(f[x_0,x_1]\)、\(f[x_0,x_1,x_2]\) 都保持不变，只需要再计算一个新的三阶差商 \(f[x_0,x_1,x_2,x_3]\)，并添加一个高阶项 \(f[x_0,x_1,x_2,x_3](x-x_0)(x-x_1)(x-x_2)\) 即可。

对于 \((0,1)\)、\((1,2)\)、\((2,5)\)、\((3,12)\)，差商表为：

| \(x_i\) | \(f[x_i]\) | 一阶差商 | 二阶差商 | 三阶差商 |
|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 1/3 |
| 1 | 2 | 3 | 2 | |
| 2 | 5 | 7 |   | |
| 3 | 12 |  |   | |

其中三阶差商的计算为：
\[
f[x_0,x_1,x_2,x_3]=\frac{f[x_1,x_2,x_3]-f[x_0,x_1,x_2]}{x_3-x_0}=\frac{2-1}{3-0}=\frac{1}{3}.
\]

因此新增项为 \(\frac{1}{3}(x-0)(x-1)(x-2)\)，牛顿插值多项式变为：
\[
P(x)=1+1\cdot(x-0)+1\cdot(x-0)(x-1)+\frac{1}{3}(x-0)(x-1)(x-2).
\]
可以看到，原来的低阶项完全保留，只是增加了一个三阶修正项。这正是牛顿插值相对于拉格朗日插值的优势：新增节点时不必重算全部基函数，只需追加一个新的差商项。展开后为：
\[
P(x)=\frac{1}{3}x^3+\frac{2}{3}x+1.
\]

```python
import numpy as np

def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
    return coef

x = np.array([0, 1, 2, 3])
y = np.array([1, 2, 5, 12])
table = divided_diff(x, y)
print("差商表：")
print(table)

# 牛顿插值求值
def newton_eval(x, table, t):
    n = len(x)
    result = table[0, 0]
    term = 1.0
    for j in range(1, n):
        term *= (t - x[j-1])
        result += table[0, j] * term
    return result

print("P(1.5) =", newton_eval(x, table, 1.5))

# 与拉格朗日插值结果对比
from scipy.interpolate import lagrange
poly = lagrange(x, y)
print("拉格朗日插值 P(1.5) =", poly(1.5))
```
</details>

---

## 问4. 什么是龙格现象

<details>
<summary>问题：</summary>
为什么用高次多项式插值函数 \(f(x)=1/(1+25x^2)\) 时，在区间两端会出现严重振荡？
</details>

<details>
<summary>解答：</summary>
龙格现象是指：在等距节点上，用高次多项式插值某些光滑函数时，随着节点数增加，插值多项式在区间边缘会出现剧烈振荡，误差不降反增。典型例子就是 \(f(x)=1/(1+25x^2)\) 在 \([-1,1]\) 上的等距插值。

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

f = lambda x: 1 / (1 + 25 * x**2)

for n in [5, 10, 15]:
    x = np.linspace(-1, 1, n+1)
    y = f(x)
    poly = lagrange(x, y)
    xs = np.linspace(-1, 1, 400)
    plt.plot(xs, poly(xs), label=f"n={n}")

plt.plot(xs, f(xs), 'k--', label="f(x)")
plt.ylim(-1, 2)
plt.legend()
plt.title("Runge Phenomenon")
plt.grid(True)
plt.show()
```

<img src='/mme/intp/python/intp-prob-4.png'>


</details>

---

## 问5. 分段线性插值为什么能避免龙格现象

<details>
<summary>问题：</summary>
高次多项式插值在等距节点上可能出现剧烈振荡。分段线性插值是如何避免这种问题的？
</details>

<details>
<summary>解答：</summary>
分段线性插值不在整个区间上用一个高次多项式，而是在每两个相邻节点之间用一条直线连接。由于每段只是低次多项式，不会出现高次多项式那种全局振荡，因此可以避免龙格现象。

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([-5, -3, -1, 0, 1, 3, 5])
y = 1 / (1 + x**2)

xs = np.linspace(-5, 5, 200)
ys = np.interp(xs, x, y)

plt.plot(xs, ys, label="Piecewise Linear")
plt.scatter(x, y, color='red')
plt.legend()
plt.grid(True)
plt.show()
```

<img src='/mme/intp/python/intp-prob-5.png'>

</details>

---

## 问6. 三次样条插值为什么比分段线性更光滑

<details>
<summary>问题：</summary>
三次样条插值也使用分段思想，但它比分段线性插值光滑。它额外满足了什么条件？
</details>

<details>
<summary>解答：</summary>
三次样条在每个小区间上使用三次多项式，并要求在内部节点处函数值、一阶导数、二阶导数都连续。这样整条曲线不仅穿过所有节点，而且连接处没有明显折角，因此比分段线性插值更光滑。

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 0, 1, 0, 1])

cs = CubicSpline(x, y, bc_type='natural')
xs = np.linspace(0, 5, 200)

plt.scatter(x, y, color='red')
plt.plot(xs, cs(xs), label="Cubic Spline")
plt.legend()
plt.grid(True)
plt.show()
```

<img src='/mme/intp/python/intp-prob-6.png'>

</details>

---

## 问7. 插值节点起什么作用

<details>
<summary>问题：</summary>
在插值问题中，插值节点只是已知数据点的横坐标吗？它们对插值结果有什么影响？
</details>

<details>
<summary>解答：</summary>
插值节点是已知函数值所在的横坐标位置。插值多项式必须在这些节点处取到给定的函数值。节点的数量决定插值多项式的最高次数，节点的分布也会显著影响插值误差和稳定性，例如等距节点可能引发龙格现象，而切比雪夫节点通常更稳定。

```python
import numpy as np
import matplotlib.pyplot as plt

# 等距节点与切比雪夫节点对比
n = 10
x_uniform = np.linspace(-1, 1, n)
x_cheb = np.cos(np.pi * np.arange(n) / (n - 1))

print("等距节点：", x_uniform)
print("切比雪夫节点：", x_cheb)
```
</details>

---

## 问8. 插值多项式是否唯一

<details>
<summary>问题：</summary>
给定 \(n+1\) 个互不相同的节点和对应函数值，次数不超过 \(n\) 的插值多项式是否唯一？
</details>

<details>
<summary>解答：</summary>
唯一。这是插值理论的基本定理：若节点 \(x_0, x_1, \cdots, x_n\) 互不相同，则存在唯一一个次数不超过 \(n\) 的多项式 \(P(x)\)，使得 \(P(x_i)=y_i\)。一个证明使用范德蒙德行列式的计算。拉格朗日插值、牛顿插值只是同一个唯一多项式的不同表示形式。

```python
import numpy as np
from scipy.interpolate import lagrange

x = np.array([0, 1, 2])
y = np.array([1, 2, 5])
poly1 = lagrange(x, y)

# 用牛顿差商也可以得到同一个多项式
def newton_poly(x, y, t):
    coef = np.zeros([len(x), len(x)])
    coef[:, 0] = y
    for j in range(1, len(x)):
        for i in range(len(x) - j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
    result = coef[0, 0]
    term = 1
    for j in range(1, len(x)):
        term *= (t - x[j-1])
        result += coef[0, j] * term
    return result

print(poly1(0.5), newton_poly(x, y, 0.5))
```
</details>

---


## 问9. 埃尔米特插值与普通插值有何不同

<details>
<summary>问题：</summary>
如果不仅知道每个节点处的函数值，还知道导数值，应该用什么插值方法？
</details>

<details>
<summary>解答：</summary>
埃尔米特插值不仅要求插值多项式在节点处等于给定函数值，还要求其导数在节点处等于给定导数值。因此它能在数据点处同时匹配函数值和变化趋势，通常比只匹配函数值的插值更光滑、更贴近原函数。

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicHermiteSpline

x = np.array([0, 1, 2])
y = np.array([0, 2, 1])
dydx = np.array([1, 0, 1])

spline = CubicHermiteSpline(x, y, dydx)
xs = np.linspace(0, 2, 200)

plt.scatter(x, y, color='red')
plt.plot(xs, spline(xs), label="Hermite Interpolation")
plt.legend()
plt.grid(True)
plt.show()
```

<img src='/mme/intp/python/intp-prob-9.png'>

</details>

---

## 问10. 重心拉格朗日插值为什么更稳定

<details>
<summary>问题：</summary>
普通拉格朗日插值在节点很多时计算量大且数值不稳定。重心拉格朗日插值做了哪些改进？
</details>

<details>
<summary>解答：</summary>
重心拉格朗日插值把拉格朗日插值公式改写成重心形式，预先计算一组重心权重 \(w_i=1/\prod (x_i-x_j)\)，之后每次求值只需要计算 \(\sum (w_i/(x-x_i))y_i\) 与 \(\sum (w_i/(x-x_i))\) 的比值。这样既减少了重复计算，又提高了数值稳定性，特别适合节点较多或需要反复求值的情况。

```python
import numpy as np

def barycentric_weights(x):
    n = len(x)
    w = np.ones(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                w[i] /= (x[i] - x[j])
    return w

def barycentric_interp(x, y, w, t):
    numerator = 0.0
    denominator = 0.0
    for i in range(len(x)):
        if np.isclose(t, x[i]):
            return y[i]
        term = w[i] / (t - x[i])
        numerator += term * y[i]
        denominator += term
    return numerator / denominator

x = np.array([0, 1, 2, 3])
y = np.array([1, 2, 5, 10])
w = barycentric_weights(x)
print("重心权重：", w)
print("在 x=1.5 处的插值：", barycentric_interp(x, y, w, 1.5))
```
</details>

---
