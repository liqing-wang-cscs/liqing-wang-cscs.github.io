## VS Code 学 Python 常见问题速查手册 —— 交互方式、环境配置与排错指南

### 问题1. VS Code 各种 Python 交互方式的区别

<details>
<summary>问题：</summary>

简要介绍 VS Code 中各种不同的 Python 交互方式。

</details>

<details>
<summary>解答：</summary>

按“轻量到重型”分为三类。

- **Terminal REPL** 就是终端里的 `>>>`，功能最基础但纯粹稳定。
- **Native REPL** 启动快、有智能提示，但历史执行顺序不可更改，适合快速验证语法。
- **Jupyter Notebook** 功能最完整，单元格可任意顺序反复执行，支持 Markdown 和图表，适合数据分析。
- **Python Interactive Window** 介于脚本和 Notebook 之间，适合写脚本时分段交互调试。

注：REPL = Read-Evaluate-Print Loop 

</details>

---

### 问题2. Jupyter 内核是什么

<details>
<summary>问题：</summary>

什么是 Jupyter 内核？

</details>

<details>
<summary>解答：</summary>

- Jupyter 内核是一个**独立运行代码的进程**，负责接收前端（Notebook 或交互窗口）发来的代码、执行并送回结果。
- 前后端通过消息协议通信，只要内核不关闭，变量状态就会保留，因此可以分多次运行代码块。
- Python 最常用的内核是 `ipykernel`，选择 Python 环境本质上就是指定用哪个解释器启动这个内核进程。

</details>

---

### 问题3. 在 VS Code 中以网页方式打开 HTML

<details>
<summary>问题：</summary>

是否可以在 VS Code 里以网页方式打开 HTML？

</details>

<details>
<summary>解答：</summary>

可以。新版 VS Code（1.121+）内置了预览功能：右键 HTML 文件或标签页，选择 “Open in Integrated Browser”，或点击编辑器右上角的 Preview 图标。旧版本可安装微软官方的 **Live Preview** 扩展，还支持保存后自动刷新。

</details>

---

### 问题4. 代码块发送到 Terminal REPL 还是 Native REPL

<details>
<summary>问题：</summary>

在 `.py` 文件中写好完整代码，选中代码块按 `Shift+Enter`，代码块被发送到 Terminal REPL, 如何发送到 Native REPL?

</details>

<details>
<summary>解答：</summary>

要让 `Shift+Enter` 把代码发送到 Native REPL，而不是 Terminal REPL，需要修改一个设置项：把 `"python.REPL.sendToNativeREPL"` 设为 `true`。操作步骤：

1. 打开 VS Code 设置（快捷键 `Ctrl+,`，或 `Cmd+,`）。
2. 搜索 `python.REPL.sendToNativeREPL`。
3. 勾选该选项，将其设为 `true`。
4. 建议重启 VS Code 或重新加载窗口，确保设置生效。

根据 VS Code 官方文档，这个设置项就是控制 `Shift+Enter`（以及“Run Selection/Line in Python REPL”命令）把代码发送到 Native REPL 还是 Terminal REPL 的开关。设为 `true` 后，`Shift+Enter` 就会指向 Native REPL。

</details>

---

### 问题5. Select Interpreter 与 Select Kernel 的区别

<details>
<summary>问题：</summary>

`Python: Select Interpreter` 和 `Select Kernel` 有什么区别？

</details>

<details>
<summary>解答：</summary>

- `Select Interpreter` 用于选择 **`.py` 文件运行/调试时使用的 Python 解释器**。
- `Select Kernel` 用于选择 **Jupyter Notebook 或 Interactive Window 背后运行的 Jupyter 内核**。
- 两者可能指向同一个 Python 环境，但控制的是不同层面的执行入口。

</details>

---

### 问题6. VS Code 与终端 Python 版本不一致

<details>
<summary>问题：</summary>

VS Code 右下角显示的 Python 版本和终端里 `python --version` 不一致，怎么办？

</details>

<details>
<summary>解答：</summary>

- 这是正常现象，**VS Code 的状态栏版本是当前选中的解释器**（用于运行/调试/智能提示），
- 终端里的 `python` 取决于系统 `PATH` 中排在最前面的版本，两者互相独立。
- 如需统一，在终端中显式使用 VS Code 选中的那个解释器的完整路径，或在 VS Code 中选中与终端默认一致的版本。
</details>

---

### 问题7. pip install 装到了哪个环境

<details>
<summary>问题：</summary>

`pip install` 装包时装到了哪个环境？怎么确认包被当前解释器识别到？

</details>

<details>
<summary>解答：</summary>

- `pip install` 装到**当前激活的 Python 环境**。
- 在 VS Code 终端中，先运行 `pip -V` 查看 pip 对应的解释器路径，再在代码中运行
  ```python
  import sys
  print(sys.executable)
  ```
  确认实际执行环境。
- 两者一致才能保证 `import` 成功。

</details>

---

### 问题8. 查看当前解释器完整路径

<details>
<summary>问题：</summary>

如何查看当前使用的是哪个 Python 解释器的完整路径？

</details>

<details>
<summary>解答：</summary>

- 在 Python 中运行
  ```python
  import sys
  print(sys.executable)
  ```
  即可输出当前解释器的完整路径。
- 在 VS Code 中也可以打开命令面板执行 `Python: Select Interpreter`，列表中每个解释器旁都会显示路径。

</details>

---

### 问题9. Run Python File 与 Interactive Window 的区别

<details>
<summary>问题：</summary>

“Run Python File”和“Run Current File in Interactive Window”有什么区别？

</details>

<details>
<summary>解答：</summary>

- **Run Python File** 在终端中执行 `python 文件.py`，几乎无额外开销。
- **Run Current File in Interactive Window** 通过 Jupyter 内核执行，会启动交互式窗口，支持分段运行和变量查看，但有启动开销。

</details>

---

### 问题10. 一键运行整个文件

<details>
<summary>问题：</summary>

如何一键运行整个 `.py` 文件，而不是只运行选中的部分？

</details>

<details>
<summary>解答：</summary>

- 点击编辑器右上角的三角形 **Run Python File** 按钮，
- 或在命令面板执行 `Python: Run Python File in Terminal`。
- 也可以右键编辑器中的文件选择 “Run Python File in Terminal”。

</details>

---

### 问题11. Native REPL 与 Terminal REPL 变量共享

<details>
<summary>问题：</summary>

Native REPL 和 Terminal REPL 里定义的变量能互相共享吗？

</details>

<details>
<summary>解答：</summary>

- **不能**。它们是两个独立的执行进程，各自维护自己的变量空间。
- 在 Native REPL 中定义的变量，Terminal REPL 里无法访问，反之亦然。

</details>

---

### 问题12. Native REPL 清屏与查看历史

<details>
<summary>问题：</summary>

Native REPL 里怎么清屏、怎么查看历史输入？

</details>

<details>
<summary>解答：</summary>

- 清屏通常可以使用命令面板中的 `Python REPL: Clear` 相关命令，或在 REPL 中尝试 `Ctrl+L`（与终端习惯一致）。
- 查看历史可用上下方向键逐条翻阅，Native REPL 的输入历史通常也会保留在当前会话中。

</details>

---

### 问题13. REPL 能 import 但文件运行报 ModuleNotFoundError

<details>
<summary>问题：</summary>

为什么在 REPL 里 `import numpy` 成功，在 `.py` 文件里运行却报 `ModuleNotFoundError`？

</details>

<details>
<summary>解答：</summary>

- 说明 **REPL 和 `.py` 文件使用的不是同一个 Python 环境**。
- REPL 的内核可能指向一个已安装 numpy 的环境，而运行 `.py` 文件的终端或调试配置指向了另一个未安装的环境。
- 用 `sys.executable` 分别检查两者，统一解释器即可。

</details>

---

### 问题14. 快速查看函数/库文档

<details>
<summary>问题：</summary>

怎么快速查看某个函数/库的官方文档？

</details>

<details>
<summary>解答：</summary>

- 鼠标悬停在函数名上会显示签名和简要说明（悬停提示）。
- `Ctrl+点击`（或 `F12`）跳转到定义（Go to Definition）。
- 在悬停卡片中点击 “Read more” 可打开在线文档（如已配置）。
- 命令面板中 `Python: Go to Python Documentation` 也可尝试。

</details>

---

### 问题15. Workspace 与普通文件夹的区别

<details>
<summary>问题：</summary>

工作区（Workspace）和普通打开文件夹有什么区别？多项目怎么管理？

</details>

<details>
<summary>解答：</summary>

- “打开文件夹”是单根目录。
- **Workspace** 支持多根目录（多文件夹）同时打开，各自可以有独立的 `.vscode/settings.json`。
- 多项目时可通过 `File > Add Folder to Workspace` 添加多个根，保存为 `.code-workspace` 文件。

</details>

---

### 问题16. 必装的 Python 扩展

<details>
<summary>问题：</summary>

学 Python 必装的 VS Code 扩展有哪些？（Python、Pylance、Jupyter 各自管什么）

</details>

<details>
<summary>解答：</summary>

- **Python**（ms-python）是基础，提供运行/调试/环境选择。
- **Pylance** 提供智能补全和类型检查。
- **Jupyter** 提供 Notebook 和 Interactive Window 支持。

三者配合覆盖了脚本开发和数据分析的常见场景。

</details>

---

### 问题17. .ipynb 与 .py 的选择

<details>
<summary>问题：</summary>

`.ipynb` 和 `.py` 文件该怎么选？什么时候用 Notebook 更合适？

</details>

<details>
<summary>解答：</summary>

- 需要**分步执行、反复调整代码块、记录分析过程、内嵌图表**时用 `.ipynb`。
- 写**可复用的脚本、模块、自动化任务**时用 `.py`。
- 两者也可以混合：用 `.py` 写稳定逻辑，用 Notebook 做探索和展示。

</details>

---

### 问题18. Notebook 单元格执行顺序混乱

<details>
<summary>问题：</summary>

Notebook 里单元格执行顺序乱了，变量状态怎么理清？

</details>

<details>
<summary>解答：</summary>

- 点击内核名称选择 **Restart Kernel**，然后从第一个单元格开始按顺序执行（`Run All` 或逐个运行）。
- 重启会清空所有变量，确保状态从零开始重建。
- 养成“从上到下顺序执行”的习惯可避免状态混乱。

</details>

---

### 问题19. Notebook 中画图不显示

<details>
<summary>问题：</summary>

怎么在 Notebook 里画图（matplotlib）并让图正常显示？

</details>

<details>
<summary>解答：</summary>

- 在 Notebook 中通常不需要额外设置，`import matplotlib.pyplot as plt` 后 `plt.plot(...)` 会自动内嵌显示。
- 如果使用 `.py` 文件配合 Interactive Window，可能需要 `%matplotlib inline`（在单元格中运行）或安装 `ipympl` 实现交互式图表。

</details>

---

### 问题20. HTML 预览不自动刷新

<details>
<summary>问题：</summary>

内置浏览器预览 HTML 时，修改代码后页面不自动刷新，怎么办？

</details>

<details>
<summary>解答：</summary>

- 内置浏览器预览通常需要手动刷新。
- 如果需要**保存后自动刷新**，安装 **Live Preview** 扩展，使用它提供的预览功能。
- 内置浏览器预览适合快速查看静态效果，不适合频繁修改的场景。

</details>

---

### 问题21. HTML 中本地资源路径加载失败

<details>
<summary>问题：</summary>

HTML 里引用的本地图片/CSS 在预览时加载不出来，路径该怎么写？

</details>

<details>
<summary>解答：</summary>

- 预览时的工作目录基准可能与 HTML 文件所在目录不同。
- 建议使用**相对路径**（如 `./image.png` 或 `../css/style.css`），确保资源相对于 HTML 文件的位置正确。
- 如果内置浏览器预览仍然失败，可尝试 Live Preview 扩展或直接用系统浏览器打开。

</details>

---

### 问题22. VS Code 中初始化 Git 仓库

<details>
<summary>问题：</summary>

VS Code 里怎么初始化 Git 仓库、提交第一次代码？

</details>

<details>
<summary>解答：</summary>

- 打开源代码管理面板（`Ctrl+Shift+G`），点击 “Initialize Repository”。
- 暂存更改（点击文件旁的 `+`），输入提交信息，点击对勾提交。
- 首次提交后，可关联远程仓库并推送。

</details>

---

### 问题23. 源代码管理面板的含义

<details>
<summary>问题：</summary>
源代码管理面板里的更改、暂存、提交分别是什么意思？
</details>

<details>
<summary>解答：</summary>

- **更改（Changes）** 是你修改但尚未暂存的文件。
- **暂存（Stage）** 表示你确认这些修改要包含在下一次提交中。
- **提交（Commit）** 是将暂存的内容永久记录到版本历史中，附带一条说明信息。

</details>

---

### 问题24. 常见报错原因

<details>
<summary>问题：</summary>

`ModuleNotFoundError`、`IndentationError`、`SyntaxError` 分别通常是什么原因？

</details>

<details>
<summary>解答：</summary>

- `ModuleNotFoundError`：模块未安装、或安装到了另一个 Python 环境、或导入名与包名不一致。
- `IndentationError`：缩进不一致（空格与 Tab 混用、层级不对）。
- `SyntaxError`：语法写错（冒号遗漏、括号不匹配、关键字拼错），报错信息会指出具体行号和位置。

</details>

---

### 问题25. 终端找不到 python 命令

<details>
<summary>问题：</summary>

终端里 `python` 命令找不到（不是内部或外部命令），怎么解决？

</details>

<details>
<summary>解答：</summary>

- Python 未加入系统 `PATH`，或安装时未勾选 “Add Python to PATH”。
- Windows 上可尝试 `py` 命令（如 `py --version`），或使用 Python 安装目录下的完整路径。
- 也可重新运行安装程序勾选添加 PATH 的选项。

</details>

---

### 问题26. 终端能跑但 VS Code 跑不了

<details>
<summary>问题：</summary>

代码在终端能跑、在 VS Code 里跑不了（或反过来），一般从哪几个方向排查？

</details>

<details>
<summary>解答：</summary>

主要排查三点：

  - **解释器是否一致**（用 `sys.executable` 对比）、
  - **工作目录是否一致**（相对路径依赖 cwd）、
  - **包环境是否一致**（`pip -V` 与执行解释器是否匹配）。
  
  这三者任一不同都可能导致“这边能跑那边不行”。

</details>

---
