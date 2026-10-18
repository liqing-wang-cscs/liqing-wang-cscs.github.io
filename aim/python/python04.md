## 逆序数的计算

### 问题：

编写 Python 程序，计算排列 134782695 的逆序数。

### 解答：

```python
def count_inversions(s):
    """计算数字字符串 s 的逆序数：前大后小的数对个数"""
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] > s[j]:
                count += 1
    return count

num = "134782695"
print(f"{num} 的逆序数为：{count_inversions(num)}")
```

### 学习要点：

- **Python 函数的格式**：用 `def 函数名(参数):` 定义函数，函数体另起一行并缩进，可用 `return` 返回结果。本例中 `count_inversions(s)` 接收一个字符串参数并返回整数逆序数。

- **Python 的循环语句 for 的格式**：基本格式为 `for 变量 in 可迭代对象:`，循环体缩进书写，每轮从可迭代对象中取一个值赋给变量。本例用两层 `for` 分别枚举下标 `i` 和 `j`，实现对所有数对的遍历。

- **Python 的判断语句 if 的格式**：格式为 `if 条件:`，条件为真时执行缩进的语句块，可配合 `elif`、`else` 分支。本例用 `if s[i] > s[j]:` 判断是否构成前大后小的逆序对。

- **range() 和 len() 的含义**：`len(s)` 返回字符串 `s` 的长度，`range(n)` 生成从 0 到 n-1 的整数序列。本例中 `range(len(s))` 用来依次取得字符串的每个下标。

- **Python 代码块缩进的规定**：Python 用缩进（通常 4 个空格）表示代码块，同一代码块的缩进必须一致，缩进错误会导致 `IndentationError`。本例中循环体和 `if` 体内的语句都靠缩进体现层级关系。

- **print(f'string') 的用法**：在字符串前加 `f` 构成 f-string，用 `{}` 嵌入变量或表达式，输出时会被替换为实际值。本例中 `f"{num} 的逆序数为：{count_inversions(num)}"` 把数字和计算结果直接拼进输出语句。
