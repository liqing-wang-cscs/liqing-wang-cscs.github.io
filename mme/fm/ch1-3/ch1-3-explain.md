**Python代码：**
```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1. 读取收盘价数据并计算对数收益率
# parse_dates解析日期，index_col将日期设为索引
df = pd.read_csv('closing.csv', parse_dates=['日期'], index_col='日期')
# 计算对数收益率: ln(P_t / P_{t-1})
log_returns = np.log(df / df.shift(1)).dropna()

# 2. 数据标准化 (均值为0，方差为1)
scaler = StandardScaler()
returns_scaled = scaler.fit_transform(log_returns)

# 3. 执行主成分分析 (假设根据前期分析确定 K=2)
# n_components=2 表示只保留前2个主成分
pca = PCA(n_components=2)
pca.fit(returns_scaled)

# 4. 提取因子得分 (Factor Scores)
# 将原始收益率投影到主成分上，得到每一天的 F1 和 F2
factor_scores = pca.transform(returns_scaled)
factor_df = pd.DataFrame(factor_scores, columns=['F1', 'F2'], index=log_returns.index)
print("提取的共同因子得分(前5行):\n", factor_df.head())

# 5. 分析因子载荷 (Factor Loadings)
# components_ 是因子在原始股票上的权重，转置后行代表股票，列代表因子
loadings = pd.DataFrame(pca.components_.T, columns=['F1', 'F2'], index=log_returns.columns)
print("\n因子载荷矩阵:\n", loadings)
```


- 从收盘价计算收益率：ch1-3-1.py

- 对历史收益率进行主成分分析：ch1-3-2.py

<img src="ch1-3-figure-scree-plot.png" alt="碎石图" width="900" height="500">

`pca.fit(returns_scaled)` 这一步在数学上的核心思想是**寻找数据中方差最大的投影方向**（即主成分方向）。由于在 `fit` 之前我们已经对数据进行了 Z-score 标准化（均值为 0，方差为 1），PCA 的求解过程可以完美地映射到**线性代数中的特征值分解（Eigendecomposition）**。

1. 目标：最大化投影方差

假设我们有 $n$ 个样本、$p$ 个特征的标准化数据矩阵 $X$（在你的代码中，$X$ 就是 `returns_scaled`，形状为 $n \times 7$）。
我们希望找到一个单位方向向量 $\mathbf{w}$（$\|\mathbf{w}\| = 1$），使得数据 $X$ 投影到 $\mathbf{w}$ 上的新变量 $z = X\mathbf{w}$ 的方差最大。

投影后的方差公式为：
$$ \text{Var}(z) = \frac{1}{n-1} (X\mathbf{w})^T (X\mathbf{w}) = \mathbf{w}^T \left( \frac{X^T X}{n-1} \right) \mathbf{w} $$

2. 核心矩阵：协方差矩阵
令 $S = \frac{X^T X}{n-1}$，这就是数据的**样本协方差矩阵**（形状为 $7 \times 7$）。
于是，我们的目标变成了：
$$ \max_{\mathbf{w}} \quad \mathbf{w}^T S \mathbf{w} $$
$$ \text{s.t.} \quad \mathbf{w}^T \mathbf{w} = 1 $$

3. 求解：拉格朗日乘数法与特征值分解
使用拉格朗日乘数法构造目标函数：
$$ L(\mathbf{w}, \lambda) = \mathbf{w}^T S \mathbf{w} - \lambda (\mathbf{w}^T \mathbf{w} - 1) $$

对 $\mathbf{w}$ 求导并令其为 0：
$$ S \mathbf{w} = \lambda \mathbf{w} $$

**这就是经典的特征值方程！**
*   $S$ 是协方差矩阵。
*   $\lambda$ 是特征值（对应方差的大小）。
*   $\mathbf{w}$ 是特征向量（对应主成分的方向）。

4. 结论：PCA 的本质
通过求解上述方程，我们得到了协方差矩阵 $S$ 的特征值 $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_p$ 和对应的特征向量 $\mathbf{w}_1, \mathbf{w}_2, \dots, \mathbf{w}_p$。

*   **第一主成分 (PC1)** 的方向 $\mathbf{w}_1$，就是协方差矩阵**最大特征值** $\lambda_1$ 对应的特征向量。它代表了数据中方差最大的方向。
*   **第二主成分 (PC2)** 的方向 $\mathbf{w}_2$，是第二大特征值 $\lambda_2$ 对应的特征向量，且必须与 $\mathbf{w}_1$ 正交（$\mathbf{w}_1^T \mathbf{w}_2 = 0$）。

5. 对应到你的 Python 代码

当你执行 `pca.fit(returns_scaled)` 时，`scikit-learn` 底层实际上做了以下事情：
1. 计算 `returns_scaled` 的协方差矩阵 $S$。
2. 对 $S$ 进行特征值分解（或者更常用、数值更稳定的 **SVD 奇异值分解**）。
3. 将得到的特征值存入 `pca.explained_variance_`（即你之前看到的 4.54, 1.09...）。
4. 将得到的特征向量（按特征值从大到小排列）存入 `pca.components_`（即因子载荷矩阵）。

**总结**：`fit` 这一步的数学思想，就是**对标准化后的股票收益率协方差矩阵进行特征值分解，找出方差最大的几个正交方向，作为驱动股票涨跌的“隐藏因子”**。


既然我们已经通过前面的分析确定了保留 $K=2$ 个主成分，接下来的核心任务就是利用这 2 个主成分来提取和解释共同因子。

在 Python 代码中，这分为两步：
1. **提取因子得分（Factor Scores）**：将原始的 7 只股票收益率降维，投影到这 2 个新因子上，得到每一天的因子收益率（即 $F_1, F_2$ 的时间序列）。
2. **分析因子载荷（Factor Loadings）**：查看每只股票在这 2 个因子上的权重，以此来解释这两个因子背后的经济含义（例如哪个代表市场整体，哪个代表半导体行业共性）。

代码解读与金融分析思路

运行上述代码后，你会得到两张关键的数据表。在数量金融中，我们通常这样解读：

1. **看 `factor_df` (因子得分)**：
   这就是我们提取出的 $F_1$ 和 $F_2$。你可以观察它们在时间序列上的波动。通常 $F_1$（解释方差最大的因子）代表“市场整体情绪”或“系统性风险”，当 $F_1$ 为负时，说明当天大盘整体承压。

2. **看 `loadings` (因子载荷矩阵)**：
   载荷代表了股票与因子的相关程度。
   * **如果某只股票在 F1 上的载荷绝对值很大**（比如大于 0.3 或小于 -0.3），说明这只股票受 F1 因子驱动明显。
   * **对比 F1 和 F2 的载荷差异**：
     * 假设 7 只股票在 F1 上的载荷都是正数且相近，那么 **F1 就是“市场整体因子”**。
     * 假设“中微公司”、“澜起科技”等半导体设备股在 F2 上的载荷显著为正，而“恒瑞医药”在 F2 上的载荷为负，那么 **F2 就是“半导体 vs 医药的行业轮动因子”**。

3. **热力图的作用**：
   代码最后生成的热力图能让人一目了然地看出哪些股票受哪个因子影响最深（颜色越深/越浅，代表相关性越强）。


