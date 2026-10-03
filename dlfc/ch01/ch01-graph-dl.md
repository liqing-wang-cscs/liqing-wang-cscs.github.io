# 深度学习知识图谱

```mermaid
graph LR
    DL["深度学习<br/>Deep Learning"]

    DL --> ARCH["核心架构"]
    DL --> APP["应用领域"]
    DL --> OPT["优化与训练"]
    DL --> MATH["数学基础"]

    ARCH --> CNN["CNN<br/>卷积网络"]
    ARCH --> RNN["RNN/LSTM<br/>循环网络"]
    ARCH --> TRANS["Transformer<br/>注意力机制"]

    APP --> CV["计算机视觉<br/>CV"]
    APP --> NLP["自然语言处理<br/>NLP"]
    APP --> AUDIO["音频处理<br/>Audio AI"]

    OPT --> BP["反向传播"]
    OPT --> ADAM["优化器<br/>Adam/SGD"]
    OPT --> DROP["Dropout<br/>正则化"]

    MATH --> LINEAR["线性代数"]
    MATH --> CALC["微积分"]
    MATH --> PROB["概率统计"]

    classDef core fill:#dbeafe,stroke:#93c5fd,stroke-width:2px,color:#1f2937,font-weight:bold;
    classDef arch fill:#fee2e2,stroke:#fca5a5,stroke-width:1.5px,color:#1f2937;
    classDef app fill:#dcfce7,stroke:#86efac,stroke-width:1.5px,color:#1f2937;
    classDef opt fill:#ffedd5,stroke:#fdba74,stroke-width:1.5px,color:#1f2937;
    classDef math fill:#f3e8ff,stroke:#d8b4fe,stroke-width:1.5px,color:#1f2937;

    class DL core;
    class ARCH,CNN,RNN,TRANS arch;
    class APP,CV,NLP,AUDIO app;
    class OPT,BP,ADAM,DROP opt;
    class MATH,LINEAR,CALC,PROB math;