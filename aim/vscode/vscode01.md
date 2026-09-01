## 安装与使用 VS Code 的简单问答

### 问1. 什么是 VS Code？

<details>
<summary>问题：</summary>

Visual Studio Code 是什么？它和 Visual Studio 有什么区别？

</details>

<details>
<summary>解答：</summary>

Visual Studio Code（简称 VS Code）是微软开发的一款**免费、开源、跨平台**的轻量级代码编辑器，支持 Windows、macOS 和 Linux 三大操作系统。它内置了 Git 版本控制、智能代码补全（IntelliSense）、调试器和集成终端等功能，并通过丰富的扩展市场支持 100 多种编程语言。

VS Code 与 Visual Studio 是完全不同的产品。Visual Studio 是一个功能庞大的集成开发环境（IDE），安装包通常数 GB 起步；而 VS Code 安装包不到 200MB，更加轻量灵活，通过安装插件来按需扩展功能，适合各类开发场景。
</details>

---

### 问2. 如何下载与安装 VS Code？

<details>
<summary>问题：</summary>

初学者应该去哪里下载 VS Code？安装时有哪些注意事项？

</details>

<details>
<summary>解答：</summary>

访问 VS Code 官网 https://code.visualstudio.com 即可下载。初学者建议选择**稳定版（Stable）**，它经过充分测试，稳定性更高。Windows 用户推荐下载 User Setup（`.exe`），macOS 用户下载 `.zip` 或 `.dmg`，Linux 用户下载 `.deb` 或 `.rpm` 包。

Windows 安装时，建议勾选"添加到 PATH"选项，这样后续可以在命令行中直接使用 `code .` 命令打开项目文件夹。macOS 用户安装后，可通过命令面板（`Cmd+Shift+P`）输入 `Shell Command: Install 'code' command in PATH` 来启用终端命令。
</details>

---

### 问3. 如何切换为中文界面？

<details>
<summary>问题：</summary>

VS Code 默认是英文界面，如何将其切换为中文？

</details>

<details>
<summary>解答：</summary>

按下 `Ctrl+Shift+X`（macOS 为 `Cmd+Shift+X`）打开扩展市场，搜索 **"Chinese (Simplified) Language Pack"**，点击安装。安装完成后，重启 VS Code 即可自动切换为中文界面。

如果重启后没有自动切换，可以按下 `Ctrl+Shift+P` 打开命令面板，输入 `Configure Display Language`，然后选择 `zh-cn` 即可。
</details>

---

### 问4. VS Code 的界面由哪些部分组成？

<details>
<summary>问题：</summary>

首次打开 VS Code，界面上的各个区域分别有什么作用？

</details>

<details>
<summary>解答：</summary>

VS Code 的界面主要分为五个区域：

- **活动栏（Activity Bar）**：最左侧的窄条，包含资源管理器、搜索、源代码管理（Git）、调试、扩展等功能的入口图标。
- **侧边栏（Side Bar）**：活动栏右侧的面板，根据所选功能显示对应的内容，如文件树、搜索结果等。
- **编辑区（Editor Group）**：中间最大的区域，用于打开和编辑代码文件，支持多标签页和分屏。
- **面板（Panel）**：位于底部，可显示集成终端、输出、问题诊断和调试控制台。
- **状态栏（Status Bar）**：最底部，显示当前文件的编码格式、语言模式、行列号、Git 分支等信息。
</details>

---

### 问5. 如何安装和使用扩展插件？

<details>
<summary>问题：</summary>

VS Code 的扩展插件如何安装？初学者推荐安装哪些插件？

</details>

<details>
<summary>解答：</summary>

按下 `Ctrl+Shift+X` 打开扩展市场，在搜索框中输入插件名称，找到后点击 **Install** 即可安装。部分插件安装后需要重启编辑器才能生效。

初学者推荐安装以下基础插件：

- **LaTeX Workshop**：VS Code 上最核心的 LaTeX 插件，提供实时 PDF 预览、智能命令补全、编译错误诊断等功能，支持 XeLaTeX 编译中文文档。
- **Python (Microsoft)**：微软官方 Python 插件，提供语法高亮、智能补全（Pylance）、代码调试、环境切换等全面支持，是 Python 开发的基础。
- **Jupyter**：支持在 VS Code 中运行和编辑 Jupyter Notebook，方便进行数学计算、函数画图和数据分析的交互式探索。
- **Code Runner**：一键运行多种语言的代码，适合初学者快速测试 Python 脚本，无需手动打开终端输入命令。
- **Markdown Preview Enhanced**：功能全面的 Markdown 预览插件，支持实时预览、数学公式渲染（LaTeX/KaTeX）、流程图绘制、导出 PDF 等，非常适合做课程笔记。
- **Markdown All in One**：提供 Markdown 快捷键支持（如 Ctrl+B 加粗）、自动生成目录、表格格式化等功能，与 Markdown Preview Enhanced 搭配使用效果更佳。

</details>

---

### 问6. 什么是命令面板？

<details>
<summary>问题：</summary>

命令面板是什么？它有什么作用？

</details>

<details>
<summary>解答：</summary>

命令面板是 VS Code 最核心的功能入口，按下 `Ctrl+Shift+P`（macOS 为 `Cmd+Shift+P`）即可调出。它集中了 VS Code 的所有命令，你只需输入关键词就能快速找到并执行对应操作，无需在菜单栏中逐层查找。

例如，输入 "theme" 可以快速切换颜色主题，输入 "format" 可以格式化代码，输入 "snippet" 可以管理代码片段。熟练使用命令面板能大幅提升操作效率。
</details>

---

### 问7. 有哪些常用的快捷键？

<details>
<summary>问题：</summary>

初学者应该优先掌握哪些 VS Code 快捷键？

</details>

<details>
<summary>解答：</summary>

以下是日常使用频率最高的快捷键（Windows/Linux，macOS 将 `Ctrl` 替换为 `Cmd`）：

| 快捷键 | 功能 |
|---|---|
| `Ctrl+S` | 保存文件 |
| `Ctrl+P` | 快速打开文件（输入文件名即可跳转） |
| `Ctrl+Shift+P` | 打开命令面板 |
| `Ctrl+`` ` | 打开/关闭集成终端 |
| `Ctrl+/` | 注释/取消注释当前行 |
| `Ctrl+Shift+F` | 全局搜索 |
| `Ctrl+B` | 切换侧边栏显示/隐藏 |
| `Alt+Click` | 添加多光标，实现多行同时编辑 |
</details>

---

### 问8. 如何配置用户设置？

<details>
<summary>问题：</summary>

如何自定义 VS Code 的字体大小、自动保存等设置？

</details>

<details>
<summary>解答：</summary>

按下 `Ctrl+,`（macOS 为 `Cmd+,`）打开设置界面。VS Code 的设置分为两种：**用户设置**（全局生效，对所有项目有效）和**工作区设置**（仅对当前项目生效，会覆盖用户设置）。

初学者建议进行以下配置：

- 搜索 `editor.fontSize`，将字体大小调整为 14-16，提升阅读舒适度。
- 搜索 `files.autoSave`，设置为 `afterDelay`，开启自动保存，避免忘记保存代码。
- 搜索 `editor.formatOnSave`，勾选开启，保存时自动格式化代码。
</details>

---

### 问9. 如何使用集成终端？

<details>
<summary>问题：</summary>

VS Code 的集成终端如何使用？它有什么优势？

</details>

<details>
<summary>解答：</summary>

按下 `` Ctrl+` ``（反引号键）即可打开或关闭集成终端。它直接嵌入在编辑器底部，支持 PowerShell、Git Bash、WSL 等多种 Shell，无需切换到外部终端窗口。

集成终端的优势在于可以**在编辑器内直接运行命令**，如编译代码、安装依赖、执行 Git 操作等，配合编辑区使用非常高效。你还可以通过终端面板右上角的 `+` 号创建多个终端实例。
</details>

---

### 问10. 如何使用调试功能？

<details>
<summary>问题：</summary>

VS Code 内置的调试功能如何使用？

</details>

<details>
<summary>解答：</summary>

点击左侧活动栏的调试图标（或按 `F5`）即可启动调试。首次调试时，VS Code 会引导你创建 `launch.json` 配置文件，用于指定程序路径、调试器类型等参数。

调试过程中的核心操作：

- **F9**：在当前行设置或取消断点。
- **F5**：启动/继续调试。
- **F10**：单步跳过（不进入函数内部）。
- **F11**：单步进入（进入函数内部）。
- **Shift+F5**：停止调试。

调试面板还可以查看变量值、监视表达式、查看调用栈，帮助你快速定位和修复代码中的问题。
</details>

---

### 问11. 如何设置 LaTeX Workshop 插件？

<details>
<summary>问题：</summary>

在 Visual Studio Code 的 LaTeX Workshop 插件中，如何将默认的编译工具设置为 XeLaTeX，以便于编译中文文档？

</details>

<details>
<summary>解答：</summary>

在 LaTeX Workshop 中，最简单且推荐的方法是直接修改 VS Code 的用户设置。通过指定默认的编译“配方（recipe）”为 `latexmk (xelatex)`，即可实现每次编译时自动使用 XeLaTeX 引擎。

具体操作步骤如下：
1.  在 VS Code 中，按下 `Ctrl + ,`（Windows/Linux）或 `Cmd + ,`（macOS）快捷键打开“设置”面板。
2.  在设置页面右上角，点击“打开设置(JSON)”图标，进入 `settings.json` 文件。
3.  在 `settings.json` 文件的顶层大括号内，添加或修改如下配置项：
    ```json
    "latex-workshop.latex.recipe.default": "latexmk (xelatex)"
    ```
4.  保存 `settings.json` 文件，配置即可生效。

此外，该插件会记录你上一次使用的编译方式。你也可以通过设置 `"latex-workshop.latex.recipe.default": "lastUsed"` 来实现同样的效果，这样插件就会记住并默认使用你最后一次选择的编译工具。

</details>
