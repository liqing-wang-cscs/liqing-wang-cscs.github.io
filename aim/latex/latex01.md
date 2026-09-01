## 安装与使用 Tex Live 的简单问答

### 问1. 什么是镜像站？

<details>
<summary>问题：</summary>

用一两句话描述镜像站的作用。

</details>

<details>
<summary>解答：</summary>

镜像站是原始服务器数据的完整复制品。使用国内镜像站（如清华源）下载 TeX Live，可以避开跨国网络延迟，获得接近本地局域网的满速下载体验。

</details>

---

### 问2. 如何下载 TeX Live 安装镜像？

<details>
<summary>问题：</summary>

在镜像站中，如何找到并下载 TeX Live 的安装文件？

</details>

<details>
<summary>解答：</summary>

在搜索引擎搜索"TeX Live 清华镜像"进入 TUNA 镜像站，找到 `texlive/Images/` 目录，选择最新年份的 `texlive.iso` 文件进行下载即可。

</details>

---

### 问3. 如何安装 TeX Live？

<details>
<summary>问题：</summary>

下载 `texlive.iso` 文件后，在不同操作系统下应如何启动安装程序？

</details>

<details>
<summary>解答：</summary>

在 Windows 下，右键以**管理员身份**打开该 ISO 文件（或解压后运行 `install-tl-windows.bat`）；在 macOS/Linux 下，挂载 ISO 并在终端以 `sudo` 权限运行 `install-tl`。随后在弹出的图形界面中点击"Install"即可。

</details>

---

### 问4. 安装过程耗时过长是否正常？

<details>
<summary>问题：</summary>

安装 TeX Live 已经 1 个多小时，如何确定安装是否完成？

</details>

<details>
<summary>解答：</summary>

TeX Live 包含数千个宏包，全量安装耗时 1-2 小时属正常现象。若安装界面的进度条仍在走动，请耐心等待；若界面显示"Weelcome to TeX Live!"或命令提示符已返回，且终端输入 `xelatex --version` 能正常输出版本号，即代表安装成功。

</details>

---

### 问5. 如何使用 TeXworks 编辑器？

<details>
<summary>问题：</summary>

如何使用 TeX Live 自带的编辑器 TeXworks 来编译文档？

</details>

<details>
<summary>解答：</summary>

在开始菜单或安装目录找到并打开 TeXworks。新建 `.tex` 文件，在左上角将排版引擎下拉框切换为 `XeLaTeX`（推荐用于中文），点击绿色的"Typeset"按钮即可编译并预览 PDF。

</details>

---

### 问6. 数学论文模板

<details>
<summary>问题：</summary>

请提供一个用于编辑数学课程论文的简易 LaTeX 模板。

</details>

<details>
<summary>解答：</summary>

```latex
\documentclass{article}
\usepackage{ctex} % 中文支持
\usepackage{amsmath, amssymb} % 数学公式核心宏包
\usepackage{geometry}         % 页面设置
\geometry{a4paper, left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm}

\title{数学课程论文：微积分基础应用}
\author{张三 \\ 学号：20260001}
\date{\today}

\begin{document}
\maketitle
% \abstract{这篇课程论文研究了微积分的基础应用。}

\section{引言}
本文主要探讨极限与导数的基本性质。

\section{核心公式}
根据泰勒展开定理，函数 $f(x)$ 在 $x=a$ 处的展开式为：
\begin{equation}
    f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n
\end{equation}

\section{结论}
上述公式在近似计算中具有重要价值。
\end{document}
```

</details>

---

### 问7. 如何解释论文模板代码？

<details>
<summary>问题：</summary>

请逐行解释上述提供的 LaTeX 模板代码的含义。

</details>

<details>
<summary>解答：</summary>

- `\documentclass{article}`：声明文档类为`article`。
- `\usepackage{ctex}`：引入中文支持宏包。
- `\usepackage{amsmath, amssymb}`：引入美国数学会的数学宏包，提供丰富的数学符号和公式环境。
- `\usepackage{geometry}`：引入页面布局宏包。
- `\geometry{...}`：设置 A4 纸张及上下左右 2.5cm 的页边距。
- `\title{...}`、`\author{...}`、`\date{\today}`：分别定义论文标题、作者信息（含学号）和当前日期。
- `\begin{document}`：正文开始标记。
- `\maketitle`：根据前文设置的标题、作者、日期自动生成标题页。
- `\section{...}`：创建一级标题（如引言、核心公式）。
- `$...$`：行内数学公式标记，用于在文本中嵌入简短公式。
- `\begin{equation} ... \end{equation}`：独立公式环境，会自动对公式进行居中排版并添加右侧编号。
- `\end{document}`：正文结束标记，此行之后的代码将被忽略。

</details>

---

### 问8. 如何设置中文文档？

<details>
<summary>问题：</summary>

在 LaTeX 中，如何设置文档以良好地支持中文？

</details>

<details>
<summary>解答：</summary>

在文档的导言区（`\begin{document}` 之前），载入中文支持宏包：`\usepackage{ctex}`。

</details>

---

### 问9. 如何插入数学公式？

<details>
<summary>问题：</summary>

在 LaTeX 中，有哪两种主要方式可以插入数学公式？

</details>

<details>
<summary>解答：</summary>

有两种主要方式：

1. **行内公式**：使用 `$...$` 将公式包裹起来，公式会与文字在同一行显示。
2. **独立公式**：使用 `\begin{equation}...\end{equation}` 环境，公式会单独成行、居中显示，并自动在右侧添加编号。

</details>

---

### 问10. 如何设置页面边距？

<details>
<summary>问题：</summary>

如何修改 LaTeX 文档的页面边距？

</details>

<details>
<summary>解答：</summary>

首先，在导言区使用 `\usepackage{geometry}` 命令引入 `geometry` 宏包。然后，使用 `\geometry{...}` 命令来设置具体的页边距，例如 `\geometry{a4paper, left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm}` 可以将 A4 纸的四个边距都设置为 2.5 厘米。

</details>
