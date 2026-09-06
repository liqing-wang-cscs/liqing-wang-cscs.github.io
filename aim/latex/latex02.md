## TeX Live 离线安装步骤（Windows）

### 1. 挂载 ISO 镜像

双击下载好的 `texlive.iso`，Windows 10/11 会自动将其挂载为一个虚拟光驱（如 `E:` 盘）。

### 2. 运行安装程序

打开挂载的虚拟光驱，双击运行 `install-tl-windows.bat`，会弹出 TeX Live 安装向导界面。

### 3. 选择安装方案

在安装向导中，可以选择安装方案：

- **默认（full scheme）**：安装全部宏包，约占 7–8 GB 磁盘空间，省心但占空间大。
- **自定义（custom scheme）**：只选需要的宏包集合，体积更小。如需节省磁盘，选 **"scheme-small"**（基础 LaTeX + 常用宏包），后续按需补装。

### 4. 设置安装路径

建议不要装在 C 盘，改到如 `D:\texlive\2026`。路径中**避免中文和空格**。

### 5. 开始安装

点击"安装"按钮，等待完成。全量安装大约需要 20–40 分钟，取决于磁盘速度。

### 6. 配置环境变量（通常自动完成）

安装程序一般会自动将 TeX Live 加入系统 PATH。安装完成后打开命令提示符，输入：

```
xelatex --version
```

如果正常输出版本信息，说明安装成功。

### 7. 安装后更新（可选）

离线安装后，如果以后联网了，可以用以下命令更新宏包：

```
tlmgr update --self --all
```

### 8. 测试实例

安装完成后，新建一个 `.tex` 文件，写入以下内容测试：

```latex
\documentclass{ctexart}
\begin{document}
Hello, TeX Live 2026!
\end{document}
```

用 `xelatex` 编译，能正常生成 PDF 就说明一切就绪。

### 9. 中文支持

- 使用 `ctexart` 文档类 + XeLaTeX 编译，开箱即用支持中文。
- 或者使用 `\usepackage{ctex}` 宏包。

### 10. 编辑器选择

推荐搭配 **VS Code + LaTeX Workshop 插件**，或 **TeXstudio**、**sublime**、**overleaf**、等。
