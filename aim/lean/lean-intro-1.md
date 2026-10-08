## Lean - 用计算机程序验证数学定理的一门编程语言

---

### 题目1. 用一个短语描述 Lean

<details>
<summary>问题：</summary>

请用一个短语或一句话描述 Lean 是什么。它和普通的编程语言（如 Python）或数学软件（如 MATLAB）有什么根本不同？

</details>

<details>
<summary>解答：</summary>

**Lean 是一个“可交互的机器验证证明器”**，同时它本身也是一门基于依值类型论的函数式编程语言。

与 Python 或 MATLAB 的根本不同在于：Python 运行代码得到数值结果，MATLAB 计算矩阵得到数值解，而 **Lean 的核心产物是“证明”本身**。在 Lean 中写下一段证明，Lean 的内核会逐行检查每一步推理是否符合逻辑规则。如果证明通过，你得到的不是一个“信任程序员”的数值结果，而是一个**被机器验证过的、从公理出发的严格数学证明**。

</details>

### 题目2. Lean 的核心机制是什么

<details>
<summary>问题：</summary>

Lean 能够“验证”证明的原理是什么？数学命题和它的证明在 Lean 眼中分别是什么东西？

</details>

<details>
<summary>解答：</summary>

Lean 建立在 **依值类型论（Dependent Type Theory）** 之上，核心思想是 **Curry-Howard 同构**：**命题即类型，证明即项**。

在 Lean 中：
- 一个**数学命题**（如 `2 + 2 = 4`）本身是一个 **`Prop` 类型的表达式**。
- 一个**证明**就是这个命题类型的一个**具体项（term）**。

例如，`2 + 2 = 4` 是一个 `Prop`，而 `rfl`（自反性）就是属于这个类型的一个证明项。如果你声称证明了某个命题，本质上就是在构造该命题类型的一个项。如果构造不出来，Lean 就不会接受这个“证明”。

</details>

### 题目3. 如何上手运行 Lean

<details>
<summary>问题：</summary>

我想在自己的电脑上开始用 Lean，最推荐的方式是什么？需要安装哪些东西？

</details>

<details>
<summary>解答：</summary>

最推荐的方式是：**安装 VS Code 编辑器 + Lean 官方扩展**。

具体步骤：
1. 下载安装 **VS Code**。
2. 在 VS Code 扩展商店中搜索并安装 **Lean (official)** 扩展。
3. 安装 **Git**（用于下载项目）。
4. 通过 Lean 扩展一键下载一个 **Lean 项目模板**（如 `LeanCourse24` 或 `Mathematics in Lean` 仓库）。

打开项目后，VS Code 会显示左右分屏：左侧是你写代码和证明的区域，右侧是 **Lean InfoView**，实时显示当前目标状态（Goal State）和假设（Hypotheses）。当所有目标清空，证明就完成了。

如果本地安装遇到困难，还可以使用 **GitHub Codespaces** 或 **Gitpod** 在浏览器中运行 Lean。

</details>

### 题目4. 什么是 Mathlib

<details>
<summary>问题：</summary>

搜索结果中经常提到 Mathlib。它是什么？对数学系学生来说意味着什么？

</details>

<details>
<summary>解答：</summary>

**Mathlib 是 Lean 社区维护的数学库**，是目前最大的 Lean 形式化数学集合。

它的重要性在于：**你不需要从皮亚诺公理开始重建一切**。Mathlib 已经形式化了大量本科和研究生级别的数学内容，包括代数、分析、拓扑、数论、测度论、范畴论等。当你需要证明某个定理时，可以直接调用 Mathlib 中已有的定义和引理。

例如，如果你想在 Lean 中使用“素数”这个概念，Mathlib 中已经有 `Nat.Prime` 的定义和大量相关定理。你的工作是在此基础上继续推进，而不是从零开始定义什么是素数。

</details>

### 题目5. 如何在 Lean 中做一次简单的计算

<details>
<summary>问题：</summary>

在 Lean 中，如何“计算”一个具体的表达式并看到结果？`#eval` 命令是做什么的？

</details>

<details>
<summary>解答：</summary>

Lean 提供了 **`#eval` 命令**来执行计算并查看结果。

例如，在 Lean 文件中输入：
```lean
#eval 2 + 2
```
VS Code 会在信息窗口中显示 `4`。

`#eval` 的本质是**调用 Lean 的求值器**，对表达式进行实际计算。它与“证明”不同：`#eval` 给出的是数值结果，而证明需要构造一个类型为命题的项。在初学阶段，`#eval` 可以帮助你快速验证你对 Lean 中定义的理解是否正确。

</details>

### 题目6. 什么是“策略”（Tactic）

<details>
<summary>问题：</summary>

Lean 中的“策略”（tactic）是什么？为什么数学证明中经常用 `by` 开头？它和直接写证明项有什么区别？

</details>

<details>
<summary>解答：</summary>

**策略是构建证明的交互式命令**，它告诉 Lean“下一步该做什么”。

例如：
```lean
theorem one_plus_one : 1 + 1 = 2 := by
  rfl
```
这里的 `by` 表示进入**策略模式**，后面的 `rfl` 是一个策略，含义是“使用自反性来关闭目标”。

与直接写证明项的区别：
- **证明项模式**：直接写出属于目标命题类型的项，如 `theorem easy : 2 + 2 = 4 := rfl`。
- **策略模式**：用一系列命令逐步将目标化简、拆解、关闭，Lean 在后台构建证明项。

对于复杂的数学证明，策略模式通常更直观、更易读，因为它模拟了人类“分步推理”的过程。

</details>

### 题目7. Lean 中的“证明状态”是什么

<details>
<summary>问题：</summary>

在 VS Code 中写 Lean 证明时，右侧的 Goal 窗口显示的内容是什么意思？如何使用它来引导证明？

</details>

<details>
<summary>解答：</summary>

**Goal 窗口显示的是“当前还需要证明什么”以及“手头有哪些已知条件”**。

典型格式：
```
1 goal
x y : ℕ
h : x = y
⊢ x + 1 = y + 1
```
- `x y : ℕ` 和 `h : x = y` 是**假设（Hypotheses）**，即你当前可以使用的变量和前提条件。
- `⊢ x + 1 = y + 1` 是**目标（Goal）**，即你需要证明的命题。

你的任务是：通过应用引理、改写、引入假设等策略，**让目标最终消失**。当窗口显示“All goals completed”时，证明就成功了。在交互式证明中，Goal 窗口是你最重要的向导。

</details>

### 题目8. 如何在 Lean 中使用已有的数学定理

<details>
<summary>问题：</summary>

如果 Mathlib 中已经有一个定理，我该如何在 Lean 中找到它并在证明中使用它？

</details>

<details>
<summary>解答：</summary>

有两种主要方式：

**第一种：知道定理的名字**，直接使用：
```lean
example (n : ℕ) : Nat.Prime n ↔ Prime n :=
  Nat.prime_iff.symm
```
这里 `Nat.prime_iff` 是 Mathlib 中的定理，`symm` 表示取等价关系的反向。

**第二种：不知道名字，用搜索工具**：
- **`exact?` 策略**：Lean 会尝试搜索能直接关闭当前目标的定理。
- **`apply?` 策略**：搜索可以用当前目标匹配的定理。
- **VS Code 中的 `#check` 和 `#print`**：查看某个定义或定理的类型和内容。
- **Loogle 或 LeanSearch**：在线搜索引擎，用自然语言或模式描述你想要的定理。

</details>

### 题目9. 为什么命题和证明的关系像“程序与类型”

<details>
<summary>问题：</summary>

Curry-Howard 同构是 Lean 的逻辑基础。请用一个具体的例子（比如“且”的证明）说明：为什么“证明一个命题”等价于“构造一个属于某类型的程序”？

</details>

<details>
<summary>解答：</summary>

以 **“且”（`∧`）** 为例。

在 Lean 中，`p ∧ q` 的定义与**笛卡尔积** `α × β` 高度相似：
- 要构造 `p ∧ q` 的证明，你需要同时提供一个 `p` 的证明和一个 `q` 的证明。这等价于构造一对元素 `(hp, hq)`，写为 `⟨hp, hq⟩`。
- 要从 `p ∧ q` 中提取 `p`，你使用 `h.left` 或 `And.left h`，这相当于从积中取第一个分量。

类似地：
- **蕴涵 `p → q`** 对应**函数类型** `p → q`：给定 `p` 的证明，返回 `q` 的证明，就是一个函数。
- **析取 `p ∨ q`** 对应**和类型**（`Sum`）：知道 `p ∨ q`，你只知道“要么有 `p`，要么有 `q`”，需要分情况讨论。

这种对应关系就是 Curry-Howard 同构：**逻辑推理规则 ↔ 编程构造规则**。

</details>

### 题目10. 作为本科生，学习 Lean 对数学学习有什么实际帮助

<details>
<summary>问题：</summary>

我将来不一定做形式化证明，为什么要花时间学 Lean？它对数学思维有什么帮助？

</details>

<details>
<summary>解答：</summary>

即使不做形式化研究，学习 Lean 对数学思维的帮助是实质性的：

**第一，强迫你精确**。在纸上写“显然成立”的地方，Lean 不允许你跳过。你必须回答：这个“显然”用了哪条公理？哪条引理？这能暴露出你自己都没意识到的理解漏洞。

**第二，提供即时反馈**。你写下一个证明步骤，Lean 立刻告诉你“这一步不成立，因为缺少某个条件”。这种即时验证循环能极大加速学习过程，类似于编程中的 REPL 环境。

**第三，理解数学的结构**。Lean 的依值类型论让你看到：数学命题不是孤立的陈述，而是处于一个复杂的类型网络中。你会开始用“这个命题属于什么类型”“需要什么构造子”来思考，这本身就是一种更高层次的数学理解。

**第四，这是未来的趋势**。AI 形式化数学已经在 IMO 级别的问题上取得突破，本科生阶段接触 Lean，是为未来的数学与 AI 交叉领域做准备。

</details>

### 题目11. Lean 学习文档

<details>
<summary>问题：</summary>

给几个介绍 Lean 的网页链接。

</details>

<details>
<summary>解答：</summary>

这里有几个适合数学专业本科生入门 Lean 的资源链接，按推荐优先级排列：

1. Mathematics in Lean（官方教材）
**推荐理由**：Lean 社区官方编写的教材，专为数学专业学生设计，涵盖从基础计算到拓扑、测度论的完整数学内容。

- 英文原版：[https://leanprover-community.github.io/mathematics_in_lean/](https://leanprover-community.github.io/mathematics_in_lean/)
- 中文翻译版：[http://www.leanprover.cn/math-in-lean-zh/](http://www.leanprover.cn/math-in-lean-zh/) 

2. Lean 快速入门（GlimpseOfLean）
**推荐理由**：适合“ impatient”的学习者，目标是在 2-3 小时内感受 Lean 证明的样子，有短路径（2小时）和长路径（半天到一天）可选。

- 英文原版：[https://reservoir.lean-lang.org/@PatrickMassot/glimpseOfLean](https://reservoir.lean-lang.org/@PatrickMassot/glimpseOfLean) 
- 中文版：[https://github.com/Lean-zh/GlimpseOfLean](https://github.com/Lean-zh/GlimpseOfLean) 

3. Lean 官方文档与社区
- **Lean 官网**：[https://lean-lang.org](https://lean-lang.org)
- **Lean 社区文档**：[https://leanprover-community.github.io/documentation.html](https://leanprover-community.github.io/documentation.html) 
- **中文社区**：[https://www.leanprover.cn/](https://www.leanprover.cn/) 

4. 在线练习（无需安装）
如果你想不安装任何东西先体验一下，可以用 Lean 官方的在线编辑器：[https://live.lean-lang.org/](https://live.lean-lang.org/) 

</details>
