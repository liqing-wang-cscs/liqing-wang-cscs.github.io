## 问：LaTeX文档类型有哪些？例如论文、幻灯片、图书、杂志？article beamer book 

## 答：

LaTeX 的文档类（document class）决定了文档的整体结构和默认排版风格。你提到的 `article`、`beamer`、`book` 是最常用的几个，下面按用途分类介绍。

### 核心文档类（标准发行版自带）

**`article`**：最通用的文档类，适合短篇文档。
- 适用：期刊论文、课程笔记、实验报告、讲义、短篇作业。
- 结构：`\section` → `\subsection` → `\subsubsection`，没有 `\chapter`。
- 特点：单面排版为主，标题不另起页（可配置）。

**`report`**：比 `article` 多一层 `\chapter`，适合中长篇文档。
- 适用：学位论文、技术报告、项目文档、本科毕业论文。
- 结构：`\chapter` → `\section` → `\subsection`。
- 特点：每个 `\chapter` 自动另起一页，默认双面排版。

**`book`**：最完整的文档类，专为成书设计。
- 适用：教材、专著、论文集。
- 结构：`\part` → `\chapter` → `\section` → `\subsection`。
- 特点：默认双面排版，有奇偶页页眉页脚区分，支持前言、目录、索引等书籍结构。

**`beamer`**：专门制作幻灯片的文档类。
- 适用：学术报告、课堂课件、会议演讲。
- 结构：以 `\begin{frame}...\end{frame}` 为基本单位，而不是 `\section`。
- 特点：内置大量主题和配色方案，支持分步显示（`\pause`）、区块（`block`）等演示功能。

**`letter`**：专门写正式信件的文档类，国内使用较少。

**`minimal`**：极简文档类，只加载最基本的字体和页面设置，通常用于调试或最小工作示例（MWE）。

### 期刊与会议专用文档类

这类文档类通常由出版社或会议组织方提供，**不能自行选择**，必须使用他们指定的模板。

- **期刊**：`elsarticle`（Elsevier）、`IEEEtran`（IEEE）、`svjour3`（Springer）、`revtex4-2`（美国物理学会）。
- **会议**：`llncs`（Springer LNCS）、`acmart`（ACM）、`IEEEtran`（IEEE 会议）。
- **学位论文**：各高校通常有自己的模板，如 `thuthesis`（清华）、`ustcthesis`（中科大）、`njuthesis`（南大）。

### 其他常见文档类

- **`ctexart` / `ctexrep` / `ctexbook`**：`ctex` 宏包提供的文档类，在标准文档类基础上针对中文排版做了优化。写中文文档时推荐用这几个，而不是直接改 `article` 的字体。
- **`moderncv`**：制作简历。
- **`tikzposter` / `beamerposter`**：制作学术海报。
- **`exam`**：制作试卷。
- **`standalone`**：制作可独立编译的图片或表格，方便插入其他文档。

### 选择建议

| 需求 | 推荐文档类 |
|---|---|
| 课程笔记、短论文 | `article` 或 `ctexart` |
| 本科毕业论文 | `report` 或学校指定模板 |
| 教材、专著 | `book` 或 `ctexbook` |
| 学术报告幻灯片 | `beamer` |
| 期刊/会议投稿 | 出版社指定模板 |
| 中文文档 | `ctexart` / `ctexrep` / `ctexbook` |

如果你写的是中文课程论文，直接用 `ctexart` 最省事；如果是英文投稿，就用期刊给的模板。
