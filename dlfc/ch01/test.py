import torch
import torch.nn as nn
import torch.optim as optim

# 1. 准备数据（简单人造数据）
X = torch.randn(100, 2)          # 100个样本，每个2维
y = (X[:, 0] + X[:, 1] > 0).float().unsqueeze(1)  # 标签：x1 + x2 > 0 则为1，否则为0

# 2. 定义最简单的神经网络：一个线性层 + sigmoid（用于二分类）
# class SimpleNet(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.linear = nn.Linear(2, 1)      # 输入2维，输出1维
#         self.sigmoid = nn.Sigmoid()        # 输出概率

#     def forward(self, x):
#         return self.sigmoid(self.linear(x))

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 10),
            nn.ReLU(),
            nn.Linear(10, 1),
            nn.Sigmoid()
        )
    def forward(self, x):
        return self.net(x)

model = SimpleNet()

# 3. 损失函数和优化器
criterion = nn.BCELoss()               # 二分类交叉熵
optimizer = optim.SGD(model.parameters(), lr=0.1)

# 4. 训练循环
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 20 == 0:
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# 5. 测试（可选）
with torch.no_grad():
    pred = model(X)
    acc = ((pred > 0.5) == y).float().mean()
    print(f"Accuracy: {acc.item():.2%}")


