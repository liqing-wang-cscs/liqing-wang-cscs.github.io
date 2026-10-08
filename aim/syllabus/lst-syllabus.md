## 《LaTeX科技排版入门》教学大纲

- 作者：王立庆（2025级各专业）
- 开课学期：2026-2027-1

---

### 参考教材

1. Oetiker 等，The Not So Short Introduction to LaTeX2e. 
2. 斯蒂芬·科特维茨著，沈冲译，LaTeX 入门实战，清华大学出版社，2024年5月第1版。

---

### 课程仓库

<https://gitee.com/liqing-wang-cscs>

---

### 参考网站

1. <https://www.ctan.org/>
2. <https://www.overleaf.com/>
3. <https://texdoc.org/>

---

### 时间地点

1. 上课时间地点：星期一下午9-10节：2D217.
2. 答疑时间地点：星期一下午7-8节：1-420.

---

### 课程成绩

1. 平时成绩 100%，包括课堂考勤、课堂实验、课程论文、阶段测验。
   1. 课堂考勤20分，12次。
   2. 课外作业30分，12次。（在学习通提交每周作业。）
   3. 课程论文20分，1次。（课程论文1篇，用LaTeX排版一份完整的数学或科技类文档。）
   4. 阶段测验30分，1次。（期末考查1次，检验对LaTeX基本语法、数学公式排版、文档结构、参考文献和绘图的理解程度。）

---

### 课程描述

本课程面向本科二年级各专业学生，普及LaTeX科技排版的基础知识，为大学后续课程论文、毕业论文和学术写作做好准备。内容包括LaTeX的安装与使用、文档结构、数学公式排版、图表制作、参考文献管理，以及使用Markdown与LaTeX结合做数学笔记的基本方法。通过本课程的学习，学生应能独立使用LaTeX排版一份符合学术规范的科技文档。

---

### 课程内容

1. LaTeX的安装与基础使用
   - 安装TeX Live与TeXworks，了解LaTeX的编译流程。
   - 掌握LaTeX文档的基本结构：导言区、正文区、文档类。
   - 了解常用文档类（article、report、book）与宏包（ctex、amsmath、graphicx、hyperref）。
   - 使用VSCode + LaTeX Workshop插件编写和编译LaTeX文档。

2. LaTeX中的文本与文档结构
   - 掌握章节、段落、列表、脚注、交叉引用等基本排版命令。
   - 掌握字体、字号、对齐、间距等格式控制方法。
   - 了解中文排版的基本方法（ctex宏包与xeCJK）。
   - 掌握表格排版（tabular、booktabs、multirow、multicolumn）。

3. 数学公式排版
   - 掌握行内公式与行间公式的排版方法。
   - 掌握上下标、分式、根式、求和、积分、极限等常用数学符号。
   - 掌握矩阵、行列式、分段函数、多行公式对齐（align、gather、cases）。
   - 掌握定理、定义、证明等数学环境的使用（amsthm）。

4. 图形、表格与参考文献
   - 掌握插入图片与浮动体（figure、subfigure、caption）。
   - 掌握使用TikZ或PGFPlots绘制简单函数图像与几何图形。
   - 掌握使用BibTeX或BibLaTeX管理参考文献。
   - 了解生成目录、索引与超链接的方法。

5. LaTeX与Markdown的结合
   - 了解Markdown与LaTeX在数学笔记中的不同使用场景。
   - 掌握在Markdown中嵌入LaTeX数学公式的方法。
   - 了解Pandoc在Markdown与LaTeX格式转换中的应用。
   - 了解使用Overleaf在线协作编辑LaTeX文档的基本方法。

---

### 授课计划

| 周 | 日期 | 内容 | 备注 | 相关包 | 软件工具 | 作业 |
|---|---|---|---|---|---|---|
| 1 | 9.7 | LaTeX基本知识、文档结构、编译流程、中文排版、文档边距。 | 安装TeXLive | ctex geometry | texworks | 写一个LaTeX文档 |
| 2 | 9.14 | 字体控制、章节、列表、脚注、交叉引用。 |  | mathrsfs upgreek | texworks | 写一个LaTeX文档（微积分10个定理） |
| 3 | 9.21 | Markdown基本知识、VSCode写Markdown、Edge浏览器预览Markdown文件。 | 安装VSCode |  | vscode edge | 写一个md文档（概率论与数理统计） |
| 4 | 9.28 | 比较md与tex的语法，实现：标题与段落、强调与列表、链接与图片、代码与引用、表格与分隔线。 |  |  | vscode | 分别写一个md文件与一个tex文件，实现这些功能 |
| 5 | 10.5 | 国庆节放假 |  |  |  |  |
| 6 | 10.12 | 常见数学公式：上下标、分式、根式、求和、积分；矩阵、分段函数、多行公式对齐。 | 布置课程论文 | amssymb amsmath bm mathtools | vscode |  |
| 7 | 10.19 | 定理、定义、证明、例子、注释。 |  | amsthm | vscode |  |
| 8 | 10.26 | 表格、图片、代码、算法。 |  | tabular booktabs multirow graphicx listings algorithm | vscode |  |
| 9 | 11.2 | 目录、索引、超链接、参考文献。 |  |  | vscode |  |
| 10 | 11.9 | 使用LaTeX做汇报幻灯片。 |  | beamer | vscode |  |
| 11 | 11.16 | 函数图像、几何图形、流程图、知识图谱。 |  | tikz | vscode |  |
| 12 | 11.23 | 文档类型：论文、幻灯片、图书、期刊、杂志。 |  | article beamer book letter standalone | vscode |  |
| 13 | 11.30 | Pandoc格式转换，overleaf在线协同。 |  |  | vscode pandoc overleaf |  |
| 14 | 12.7 | 展示交流课程论文。 |  |  |  |  |
| 15 | 12.14 | 阶段测验 | 在教室闭卷考试 |  |  |  |
