## 代数余子式的计算

### 问题：

设行列式
$$
D=\begin{vmatrix}
1&1&1&2 \\
1&1&-2&0 \\
1&2&0&-1 \\
2&-3&4&3 \\
\end{vmatrix}
$$
的代数余子式记为 $A_{ij}$. 

1. 计算 $A_{41}+A_{42}+A_{43}+2A_{44}$. 
2. 计算 $A_{41}+A_{42}+A_{43}+A_{44}$. 

### 解答：

首先输入一些行向量
```python
import numpy as np
A1=np.array([1,1,1,2])
A2=np.array([1,1,-2,0])
A3=np.array([1,2,0,-1])
A4=np.array([2,-3,4,3])
B1=np.array([1,1,1,2])
B2=np.array([1,1,1,1])
```

然后根据用代数余子式展开行列式的方法，可得所求的两个表达式的值为
```python
C=np.array([A1,A2,A3,B1])
print(np.linalg.det(C))

D=np.array([A1,A2,A3,B2])
print(np.linalg.det(D))
```

输出结果：

```
0.0
-3.0000000000000004
```

