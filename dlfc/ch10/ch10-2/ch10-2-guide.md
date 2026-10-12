# 知识图谱：Convolutional Filters（ch10-2）

> 基于《CONVOLUTIONAL NETWORKS》第 10.2 节内容整理  
> 适用工具：Typora、Obsidian、VS Code、GitHub、Notion 等支持 Mermaid 的 Markdown 环境

---

## 1. 本节知识总览

```mermaid
mindmap
  root((10.2 Convolutional Filters))
    动机
      全连接参数爆炸
      需要归纳偏置
      减少数据需求
      提升泛化
    四个核心概念
      Hierarchy 层次
      Locality 局部性
      Equivariance 等变性
      Invariance 不变性
    特征检测器
      感受野
      滤波器/核
      ReLU 输出
      特征匹配
    平移等变性
      权重共享
      特征图
      稀疏连接
      卷积
    卷积细节
      二维卷积公式
      边缘检测例子
      Padding
      Strided Convolution
      多维卷积
      1x1 卷积
    池化
      Max Pooling
      Average Pooling
      局部平移不变性
      降维
      跨通道池化
      处理可变尺寸
    多层卷积
      层级结构
      有效感受野增长
      末端全连接层
      超参数选择
    经典架构
      LeNet
      ImageNet
      AlexNet
      VGG-16
```

---

## 2. 核心动机：为什么需要卷积网络

```mermaid
flowchart TD
    A[图像是高维数据] --> B[全连接网络参数爆炸]
    B --> B1[例：1000x1000x3 图像]
    B1 --> B2[第一层 1000 隐藏单元]
    B2 --> B3[约 3×10^9 个权重]

    A --> C[需要从样本中学习不变性]
    C --> C1[需要巨大数据集]

    D[引入归纳偏置] --> E[减少数据需求]
    D --> F[提升泛化]
    D --> G[利用图像空间结构]

    B3 --> D
    C1 --> D
```

---

## 3. 四个 interrelated concepts

```mermaid
flowchart LR
    A[利用二维图像结构] --> B[Hierarchy 层次]
    A --> C[Locality 局部性]
    A --> D[Equivariance 等变性]
    A --> E[Invariance 不变性]

    B --> B1[人脸 → 眼睛 → 虹膜 → 边缘]
    C --> C1[单元只连接小区域]
    D --> D1[输入平移 → 输出对应平移]
    E --> E1[输入平移 → 输出不变]

    B1 --> F[复杂特征由简单特征组合]
    C1 --> G[感受野]
    D1 --> H[卷积 + 权重共享]
    E1 --> I[池化]
```

---

## 4. 特征检测器与感受野

```mermaid
flowchart TD
    A[第一层单个单元] --> B[输入：小矩形区域 patch]
    B --> C[感受野 Receptive Field]
    C --> D[局部性 Locality]

    A --> E[输出]
    E --> F["z = ReLU(w^T x + w0)"]

    G[权重] --> H[形成二维网格]
    H --> I[滤波器 Filter / 核 Kernel]
    I --> J[可可视化为图像]

    K[固定 w 和 w0] --> L[最大化输出]
    L --> M[最优输入 x = αw]
    M --> N[单元检测与核相似的图像块]
    N --> O[ReLU 超过阈值 -w0 时激活]
    O --> P[作为特征检测器]
```

---

## 5. 平移等变性 Translation Equivariance

```mermaid
flowchart TD
    A[同一特征出现在不同位置] --> B[需要在所有位置泛化]
    B --> C[复制同一组权重到多个位置]
    C --> D[权重共享 Weight Sharing]
    C --> E[稀疏连接 Sparse Connections]

    D --> F[隐藏层单元形成特征图 Feature Map]
    E --> F

    F --> G[局部 patch 响应]
    G --> H[相同像素值在不同位置]
    H --> I[在特征图对应平移位置产生相同响应]
    I --> J[等变性 Equivariance]

    J --> K[卷积 Convolution]
```

---

## 6. 二维卷积

```mermaid
flowchart TD
    A[图像 I] --> C[卷积]
    B[滤波器 K] --> C
    C --> D[特征图 C]

    D --> E["C(j,k) = Σ_l Σ_m I(j+l, k+m) K(l,m)"]
    E --> F[省略非线性激活]
    F --> G[严格说是互相关 cross-correlation]
    G --> H[机器学习文献常称卷积]

    H --> I[Batch Norm 注意]
    I --> J[同一特征图内所有空间位置]
    J --> K[使用相同均值和方差]
```

---

## 7. 边缘检测示例

```mermaid
flowchart LR
    A[垂直边缘] --> B[水平方向强度显著变化]
    B --> C["滤波器: [-1 0 1; -1 0 1; -1 0 1]"]

    D[水平边缘] --> E[垂直方向强度显著变化]
    E --> F["滤波器: [-1 -1 -1; 0 0 0; 1 1 1]"]

    C --> G[特征图正值/负值]
    F --> G
    G --> H[正值：强度增加]
    G --> I[负值：强度减少]
```

---

## 8. 卷积相比全连接的优势

```mermaid
flowchart TD
    A[卷积结构优势] --> B[连接稀疏]
    A --> C[权重共享]
    A --> D[可处理不同尺寸图像]

    B --> B1[大图像下权重仍很少]
    C --> C1[独立参数大幅减少]
    C1 --> C2[所需训练集更小]
    D --> D1[输入尺寸变化只改变特征图大小]
    D1 --> D2[不改变权重数量]

    A --> E[GPU 并行]
    E --> F[卷积计算高效]
```

---

## 9. Padding

```mermaid
flowchart TD
    A["卷积后特征图变小"] --> B["输入 J x K"]
    B --> C["核 M x M"]
    C --> D["输出 (J-M+1) x (K-M+1)"]

    D --> E{"是否需要同尺寸"}
    E -->|否| F["Valid Convolution"]
    F --> F1["P = 0"]

    E -->|是| G["Padding"]
    G --> H["填充 P 像素"]
    H --> I["输出 (J+2P-M+1) x (K+2P-M+1)"]
    I --> J["Same Convolution"]
    J --> J1["P = (M-1)/2"]

    G --> K["通常 M 取奇数"]
    K --> K1["对称填充"]
    K1 --> K2["有明确中心像素"]

    G --> L["填充值选择"]
    L --> L1["常用 0"]
    L1 --> L2["先减去图像均值"]
    L2 --> L3["0 表示平均强度"]
```

---

## 10. Strided Convolutions

```mermaid
flowchart TD
    A[特征图过大] --> B[需要更小特征图]
    B --> C[Strided Convolution]
    C --> D[滤波器移动步长 S]

    D --> E["输出尺寸 = floor((J+2P-M)/S - 1) × floor((K+2P-M)/S - 1)"]
    E --> F[大图像 + 小滤波器]
    F --> G[特征图约缩小 1/S]
```

---

## 11. 多维卷积与多通道

```mermaid
flowchart TD
    A["灰度图"] --> B["单通道卷积"]
    C["彩色图"] --> D["三通道 RGB"]
    D --> E["输入张量 J×K×C"]
    E --> F["滤波器张量 M×M×C"]
    F --> G["每个输入通道一个 M×M 滤波器"]
    G --> H["输出特征图 (J-M+1)×(K-M+1)"]

    H --> I["单个滤波器只能检测一种特征"]
    I --> J["引入多个滤波器"]
    J --> K["滤波器张量 M×M×C×C_OUT"]
    K --> L["每个输出通道独立特征图"]
    L --> M["参数数量 (M²C + 1)C_OUT"]

    N["1×1 卷积"] --> O["滤波器大小 1 像素"]
    O --> P["每个输入通道一个权重"]
    P --> Q["加偏置"]
    Q --> R["改变通道数"]
    R --> S["通常用于降通道"]
    S --> T["不改变特征图空间尺寸"]
```

---

## 12. 池化 Pooling

```mermaid
flowchart TD
    A[卷积层] --> B[平移等变性 Equivariance]
    B --> B1[适合定位任务]

    A --> C[分类任务需要]
    C --> D[平移不变性 Invariance]

    D --> E[Pooling]
    E --> F[无学习参数]
    E --> G[固定函数]
    E --> H[有滤波器大小和步长]

    H --> I[Max Pooling]
    H --> J[Average Pooling]

    I --> K[保留特征是否出现及强度]
    K --> L[丢弃部分位置信息]
    J --> L

    L --> M[局部平移不变性]
    E --> N[降采样]
    N --> O[降低表示维度]

    E --> P[逐通道独立池化]
    P --> P1[例：8×64×64 → 8×32×32]

    E --> Q[跨通道池化]
    Q --> Q1[可学习其他不变性]
    Q1 --> Q2[如：不同方向的同一特征 → 近似旋转不变]

    E --> R[处理可变尺寸图像]
    R --> R1[调整池化步长]
    R1 --> R2[保持池化输出数量恒定]
```

---

## 13. 多层卷积

```mermaid
flowchart TD
    A["单层卷积"] --> B["多层卷积"]
    B --> C["每层滤波器张量 M x M x C_IN x C_OUT"]
    C --> D["参数量 (M^2 C_IN + 1) C_OUT"]
    D --> E["每层可选池化"]

    E --> F["多层卷积与池化交替"]
    F --> G["局部性 Locality"]
    G --> H["每单元只看上一层小 patch"]
    H --> I["有效感受野随深度增长"]

    F --> J["末端全连接层"]
    J --> J1["整合全图信息"]
    J1 --> J2["分类等整体预测"]
    J2 --> J3["最终卷积层维度较低"]
    J3 --> J4["全连接层参数可能占多数"]

    F --> K["完整 CNN"]
    K --> K1["多层卷积"]
    K1 --> K2["池化"]
    K2 --> K3["末端全连接"]
    K3 --> K4["大量超参数"]
    K4 --> K5["层数 通道数 滤波器大小 步长等"]
```

---

## 14. 有效感受野随深度增长

```mermaid
flowchart BT
    A[输入层 5 个单元] --> B[中间层 3 个单元]
    B --> C[输出层 1 个单元]

    C --> C1[依赖中间层 3 个单元]
    C1 --> C2[依赖输入层 5 个单元]
    C2 --> C3[有效感受野扩大]
```

---

## 15. 经典网络架构

```mermaid
flowchart TD
    A[早期 CNN] --> B[LeNet]
    B --> B1[手写数字分类]
    B1 --> B2[低分辨率单色图像]

    A --> C[ImageNet]
    C --> C1[1400 万自然图像]
    C1 --> C2[约 22000 类]
    C2 --> C3[强调大规模数据 + 归纳偏置]

    C --> D[ImageNet Challenge]
    D --> D1[1000 类]
    D1 --> D2[128 万训练 / 5 万验证 / 10 万测试]
    D2 --> D3[Top-1 / Top-5 错误率]

    D --> E[AlexNet]
    E --> E1[2012 年夺冠]
    E1 --> E2[Top-5 错误率 15.3%]
    E2 --> E3[ReLU]
    E2 --> E4[GPU 训练]
    E2 --> E5[Dropout]

    D --> F[后续进展]
    F --> F1[错误率约 3%]
    F1 --> F2[优于人类约 5%]
    F2 --> F3[原因：人类难区分细微类别]

    A --> G[VGG-16]
    G --> G1[Visual Geometry Group]
    G1 --> G2[16 个可学习层]
    G2 --> G3[结构统一]
    G3 --> G4[3×3 卷积, stride 1, same padding, ReLU]
    G3 --> G5[2×2 max-pooling, stride 2]
    G5 --> G6[每池化降采样 4 倍]
    G3 --> G7[通道数逐层翻倍]
    G7 --> G8[64 → 128 → 256 → 512]
    G3 --> G9[末端 3 个全连接层]
    G9 --> G10[4096 → 4096 → 1000]
    G10 --> G11[输出 softmax]
    G10 --> G12[约 1.38 亿参数]
    G12 --> G13[约 1.03 亿在第一全连接层]
```

---

## 16. 大感受野 vs 多层小感受野

```mermaid
flowchart LR
    A[大感受野] --> A1[AlexNet 11×11, stride 4]
    A1 --> A2[参数多]

    B[多层小感受野] --> B1[VGG 3×3 堆叠]
    B1 --> B2[参数显著更少]
    B2 --> B3[对大的滤波器施加归纳偏置]
    B3 --> B4[大滤波器由卷积子滤波器组合而成]
```

---

## 17. 关键概念索引

| 概念 | 所属主题 | 说明 |
|---|---|---|
| 归纳偏置 | 动机 | 利用图像结构减少参数和数据需求 |
| Hierarchy | 四个核心概念 | 复杂特征由简单特征逐层组合 |
| Locality | 四个核心概念 | 单元只连接输入的小局部区域 |
| Equivariance | 四个核心概念 | 输入平移导致输出对应平移 |
| Invariance | 四个核心概念 | 输入平移时输出保持不变 |
| 感受野 | 特征检测器 | 单元所连接输入图像的小区域 |
| 滤波器 / 核 | 特征检测器 | 权重形成的二维网格，可可视化 |
| 特征检测器 | 特征检测器 | 匹配核模式时产生强响应 |
| 权重共享 | 平移等变性 | 同一组权重在多个位置复用 |
| 稀疏连接 | 平移等变性 | 大多数连接不存在 |
| 特征图 | 平移等变性 | 共享权重的隐藏单元形成的图 |
| 卷积 | 卷积机制 | 局部加权求和，实现等变性 |
| Cross-correlation | 卷积机制 | 严格数学定义下与卷积略有差异 |
| Padding | 卷积细节 | 填充像素以控制输出尺寸 |
| Valid Convolution | Padding | P = 0，输出尺寸变小 |
| Same Convolution | Padding | P = (M-1)/2，输出与输入同尺寸 |
| Strided Convolution | 卷积细节 | 用步长 S 移动滤波器，实现降采样 |
| 多维卷积 | 卷积细节 | 对多通道输入使用 M×M×C 滤波器 |
| 多滤波器 | 卷积细节 | 每个滤波器产生一个输出通道 |
| 1×1 卷积 | 卷积细节 | 改变通道数，不改变空间尺寸 |
| Pooling | 池化 | 无学习参数的固定函数 |
| Max Pooling | 池化 | 取感受野最大值 |
| Average Pooling | 池化 | 取感受野平均值 |
| 局部平移不变性 | 池化 | 对小范围平移不敏感 |
| 跨通道池化 | 池化 | 可学习旋转等其他不变性 |
| 多层卷积 | 多层结构 | 卷积与池化交替堆叠 |
| 有效感受野 | 多层结构 | 随深度增加而扩大 |
| 末端全连接层 | 多层结构 | 整合全图信息做整体预测 |
| LeNet | 经典架构 | 早期手写数字分类 CNN |
| ImageNet | 经典架构 | 大规模图像分类基准 |
| AlexNet | 经典架构 | 2012 年 ImageNet 冠军 |
| VGG-16 | 经典架构 | 结构统一、3×3 卷积堆叠的经典 CNN |

---

## 18. 本节总结

```mermaid
flowchart TD
    A[10.2 卷积滤波器] --> B[用归纳偏置替代全连接]
    A --> C[四个核心概念]
    C --> C1[Hierarchy]
    C --> C2[Locality]
    C --> C3[Equivariance]
    C --> C4[Invariance]

    A --> D[卷积]
    D --> D1[感受野 + 滤波器]
    D --> D2[权重共享 + 稀疏连接]
    D --> D3[平移等变性]
    D --> D4[Padding / Stride / 多通道 / 1×1]

    A --> E[池化]
    E --> E1[局部平移不变性]
    E --> E2[降采样]
    E --> E3[Max / Average / 跨通道]

    A --> F[多层卷积]
    F --> F1[层级特征]
    F --> F2[有效感受野增长]
    F --> F3[末端全连接]

    A --> G[经典架构]
    G --> G1[LeNet]
    G --> G2[AlexNet]
    G --> G3[VGG-16]
```
---
