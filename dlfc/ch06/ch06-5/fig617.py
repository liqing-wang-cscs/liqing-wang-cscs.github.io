import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim

# --- 1. 生成数据集 ---
def generate_data(n_samples=100, noise_std=0.1):
    """
    生成 Figure 6.17 中使用的 toy 数据集。

    Args:
        n_samples (int): 生成的样本数量。
        noise_std (float): 添加噪声的标准差。

    Returns:
        tuple: (x_forward, t_forward, x_inverse, t_inverse)
               x_forward, t_forward: 正向问题数据 (x -> t)
               x_inverse, t_inverse: 逆向问题数据 (t -> x)
    """
    # 生成均匀分布的 x
    x = np.random.uniform(0, 1, size=n_samples)
    
    # 计算正向问题的目标 t = x + 0.3 * sin(2*pi*x) + noise
    noise = np.random.uniform(-noise_std, noise_std, size=n_samples)
    t = x + 0.3 * np.sin(2 * np.pi * x) + noise
    
    # 逆向问题只是交换了 x 和 t 的角色
    x_inv = t.copy()
    t_inv = x.copy()

    # 确保值在 [0, 1] 范围内，如果噪声导致越界则裁剪
    x_inv = np.clip(x_inv, 0, 1)
    t_inv = np.clip(t_inv, 0, 1)

    return x, t, x_inv, t_inv

# --- 2. 定义神经网络模型 ---
class SimpleNet(nn.Module):
    def __init__(self, input_dim=1, output_dim=1, hidden_dim=6):
        super(SimpleNet, self).__init__()
        self.hidden = nn.Linear(input_dim, hidden_dim)
        self.output = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, x):
        x = torch.tanh(self.hidden(x)) # 使用 tanh 激活函数
        x = self.output(x)
        return x

# --- 3. 训练函数 ---
def train_model(model, X_train, y_train, epochs=5000, lr=0.01):
    """
    使用最小二乘误差训练模型。

    Args:
        model (nn.Module): PyTorch 神经网络模型。
        X_train (np.ndarray): 训练输入数据。
        y_train (np.ndarray): 训练目标数据。
        epochs (int): 训练轮数。
        lr (float): 学习率。
    """
    criterion = nn.MSELoss() # 平方误差损失
    optimizer = optim.Adam(model.parameters(), lr=lr)

    X_tensor = torch.tensor(X_train, dtype=torch.float32).unsqueeze(1) # 形状: (N, 1)
    y_tensor = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1) # 形状: (N, 1)

    model.train()
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(X_tensor)
        loss = criterion(outputs, y_tensor)
        loss.backward()
        optimizer.step()
        
        if epoch % 100 == 0:
            print(f"Epoch [{epoch}/{epochs}], Loss: {loss.item():.6f}")

# --- 4. 主程序 ---
if __name__ == "__main__":
    # 设置随机种子以复现结果
    np.random.seed(42)
    torch.manual_seed(42)

    # 生成数据
    x_forward, t_forward, x_inverse, t_inverse = generate_data(n_samples=100)

    # --- 正向问题 (x -> t) ---
    print("--- Training on Forward Problem (x -> t) ---")
    net_forward = SimpleNet(input_dim=1, output_dim=1, hidden_dim=6)
    train_model(net_forward, x_forward, t_forward, epochs=5000, lr=0.01)

    # 生成平滑的 x 值用于绘图
    x_smooth = np.linspace(0, 1, 100)
    x_smooth_tensor = torch.tensor(x_smooth, dtype=torch.float32).unsqueeze(1)
    net_forward.eval()
    with torch.no_grad():
        t_pred_forward = net_forward(x_smooth_tensor).numpy().squeeze()


    # --- 逆向问题 (t -> x) ---
    print("\n--- Training on Inverse Problem (t -> x) ---")
    net_inverse = SimpleNet(input_dim=1, output_dim=1, hidden_dim=6)
    train_model(net_inverse, x_inverse, t_inverse, epochs=5000, lr=0.01) # 注意：x_inverse 是输入，t_inverse 是目标

    # 生成平滑的 t 值（作为逆向问题的输入）用于绘图
    t_smooth = np.linspace(0, 1, 100)
    t_smooth_tensor = torch.tensor(t_smooth, dtype=torch.float32).unsqueeze(1)
    net_inverse.eval()
    with torch.no_grad():
        x_pred_inverse = net_inverse(t_smooth_tensor).numpy().squeeze() # 预测的是 x (原输入)


    # --- 5. 可视化 ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # 左图：正向问题
    ax1.scatter(x_forward, t_forward, alpha=0.5, c='green', edgecolors='none', s=20, label='Training Data')
    ax1.plot(x_smooth, t_pred_forward, color='red', linewidth=2, label='Neural Network Fit')
    ax1.set_xlabel('$x$')
    ax1.set_ylabel('$t$')
    ax1.set_title('Forward Problem: $t$ vs $x$')
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.6)

    # 右图：逆向问题
    ax2.scatter(x_inverse, t_inverse, alpha=0.5, c='green', edgecolors='none', s=20, label='Training Data (Swapped)')
    ax2.plot(x_pred_inverse, t_smooth, color='red', linewidth=2, label='Poor Neural Network Fit') # 注意：x_pred 是输出，t_smooth 是输入
    ax2.set_xlabel('$t$')
    ax2.set_ylabel('$x$')
    ax2.set_title('Inverse Problem: $x$ vs $t$')
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.show()


'''
Q: 给出实现图6.17这个例子的python代码
A: 好的，下面是生成 Figure 6.17 示例数据集及其可视化（包括正向和逆向问题，以及使用传统神经网络拟合的结果）的 Python 代码。

这个代码包含以下几个部分：
1.  **生成数据集**：按照 PRML 描述的方式生成正向和逆向问题的数据。
2.  **定义神经网络模型**：使用 PyTorch 创建一个简单的两层全连接网络。
3.  **训练函数**：用于在正向或逆向数据上训练网络（最小化平方误差）。
4.  **可视化**：绘制 Figure 6.17 的左右两幅图。

### 代码说明

1.  **`generate_data`**: 函数按照 $t = x + 0.3 \sin(2\pi x) + \varepsilon$ 生成数据点，然后简单地交换 $x$ 和 $t$ 来模拟逆问题。
2.  **`SimpleNet`**: 一个简单的 PyTorch 模型，包含一个隐藏层（6 个单元，tanh 激活）和一个输出层。这与 PRML 图注中提到的“two-layer neural network with six hidden units”一致（PRML 中的“两层”通常指隐藏层+输出层，而不是输入层+隐藏层+输出层）。
3.  **`train_model`**: 使用 Adam 优化器和 MSE 损失函数来训练模型。这等效于最小化平方误差。
4.  **主程序**:
    *   生成数据。
    *   分别训练两个独立的模型：一个用于正向问题，一个用于逆向问题。
    *   使用训练好的模型对平滑的输入序列进行预测，以便绘制平滑的拟合曲线。
    *   使用 `matplotlib` 绘制两个子图，对应 Figure 6.17 的左右图。

运行此代码将重现 Figure 6.17 的核心现象：在正向问题上网络拟合良好，而在逆向问题上网络无法捕捉多模态特性，给出了一个“糟糕”的单一预测路径。

'''