## 在 Windows 系统里安装 Python 

1. 打开浏览器，登录清华镜像官网：<https://mirrors.tuna.tsinghua.edu.cn/python/3.15.0/>

2. 找到并下载文件 `python-3.15.0-amd64.exe`, 文件大小约为 43.3M 。

3. 双击该文件，勾选 "Add Python to PATH"，然后开始安装。

4. 按 Win-R, 打开命令提示符终端，输入 cmd 打开命令提示符终端。（或者：左下角的开始 - Windows系统 - 命令提示符）

5. 安装 numpy 包：在命令提示符终端里运行
```bash
pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
```

6. 在命令提示符终端里运行python, 看到Python特有的提示符，三个向右的箭头：>>>

7. 载入 numpy 库
```python
import numpy as np
```

8. 使用 np.array 函数输入矩阵，注意参数是一个列表的列表
```python
A=np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
```

9. 访问矩阵元素，访问某些行和列
```python
A[0,0]
A[1,3]
A[1,:]
A[:,2]
```

10. 使用 np.delete 函数，删除第2行第3列（注意Python从0开始对行列计数）
```python
B=np.delete(A,1,axis=0)
C=np.delete(B,2,axis=1)
```

11. 使用 np.linalg.det 函数，计算代数余子式 $A_{23}$
```python
(-1)**(2+3)*np.linalg.det(C)
```
