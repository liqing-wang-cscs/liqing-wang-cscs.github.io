import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim

# --- 1. 设置 ---
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 设置随机种子以确保结果可复现
np.random.seed(42)
torch.manual_seed(42)
if device.type == 'cuda':
    torch.cuda.manual_seed(42)

# --- 2. 数据生成 ---
def generate_data(n_samples=300):
    """
    Generates the toy dataset as described in the text.
    Forward process: x -> y = x + 0.3 * sin(2*pi*x) + noise
    The inverse problem is what we model: x (input) -> t=y (target)
    """
    x = np.random.uniform(0, 1, size=(n_samples, 1)).astype(np.float32)
    y_clean = x + 0.3 * np.sin(2 * np.pi * x)
    noise = np.random.uniform(-0.1, 0.1, size=(n_samples, 1)).astype(np.float32)
    t = y_clean + noise
    return torch.tensor(t), torch.tensor(x)

X_train_tensor, T_train_tensor = generate_data(n_samples=300)
train_dataset = torch.utils.data.TensorDataset(X_train_tensor, T_train_tensor)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)

# --- 3. MDN 模型定义 ---
class MixtureDensityNetwork(nn.Module):
    def __init__(self, input_dim=1, num_gaussians=3):
        super(MixtureDensityNetwork, self).__init__()
        self.num_gaussians = num_gaussians
        
        # 输入层到隐藏层
        self.fc_hidden = nn.Linear(input_dim, 5) # 5 个 tanh 单元
        
        # 隐藏层到输出层，输出 3*K 个参数 (K=3)
        # 输出: [pi_1, ..., pi_K, mu_1, ..., mu_K, sigma_1, ..., sigma_K]
        self.fc_out_pi = nn.Linear(5, num_gaussians)
        self.fc_out_mu = nn.Linear(5, num_gaussians)
        self.fc_out_sigma = nn.Linear(5, num_gaussians)

    def forward(self, x):
        h = torch.tanh(self.fc_hidden(x))
        
        # 混合系数
        log_pi = self.fc_out_pi(h)
        pi = nn.functional.softmax(log_pi, dim=1) # Shape: (batch_size, K)
        
        # 均值
        mu = self.fc_out_mu(h) # Shape: (batch_size, K)
        
        # 标准差 (确保为正)
        log_sigma = self.fc_out_sigma(h)
        sigma = torch.exp(log_sigma) # Shape: (batch_size, K)
        
        return pi, mu, sigma

model = MixtureDensityNetwork(input_dim=1, num_gaussians=3).to(device)

# --- 4. 损失函数定义 ---
def mdn_loss(pi, mu, sigma, target):
    """
    Calculates the negative log-likelihood loss for MDN.
    """
    # Expand dimensions for broadcasting
    # target: (batch_size, 1)
    # pi, mu, sigma: (batch_size, K)
    target_expanded = target.unsqueeze(-1) # Shape: (batch_size, 1, 1)

    # Calculate Gaussian PDF values
    # Normalization constant part: 1 / sqrt(2*pi*sigma^2) = exp(-log(sigma * sqrt(2*pi)))
    normalizer = torch.log(sigma * np.sqrt(2 * np.pi))
    # Exponent part: exp(-0.5 * ((target - mu) / sigma)^2)
    exponent = -0.5 * ((target_expanded - mu.unsqueeze(1)) / sigma.unsqueeze(1))**2
    log_prob = - normalizer.unsqueeze(1) + exponent # Shape: (batch_size, 1, K)

    # Weight by mixing coefficients
    weighted_log_prob = torch.log(pi.unsqueeze(1)) + log_prob # Shape: (batch_size, 1, K)
    
    # Sum over mixture components (log-sum-exp for numerical stability)
    # log(sum(exp(log_p))) = log_sum_exp(log_p)
    log_sum_probs = torch.logsumexp(weighted_log_prob, dim=-1) # Shape: (batch_size, 1)
    
    # Return the mean negative log-likelihood
    return -torch.mean(log_sum_probs)

# --- 5. 训练模型 ---
optimizer = optim.Adam(model.parameters(), lr=0.001)
num_epochs = 2000 # 可能需要调整

losses = []
for epoch in range(num_epochs):
    epoch_losses = []
    for batch_x, batch_t in train_loader:
        batch_x, batch_t = batch_x.to(device), batch_t.to(device)

        optimizer.zero_grad()
        pi, mu, sigma = model(batch_x)
        loss = mdn_loss(pi, mu, sigma, batch_t)
        loss.backward()
        optimizer.step()

        epoch_losses.append(loss.item())
    
    epoch_avg_loss = np.mean(epoch_losses)
    losses.append(epoch_avg_loss)
    if (epoch + 1) % 500 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_avg_loss:.4f}')

# --- 6. 生成用于可视化的数据 ---
# 生成一个密集的 x 网格用于绘图
x_plot_range = np.linspace(0, 1, 200).reshape(-1, 1).astype(np.float32)
x_plot_tensor = torch.tensor(x_plot_range).to(device)

with torch.no_grad():
    model.eval()
    pi_vals, mu_vals, sigma_vals = model(x_plot_tensor)
    pi_vals_np = pi_vals.cpu().numpy()
    mu_vals_np = mu_vals.cpu().numpy()
    sigma_vals_np = sigma_vals.cpu().numpy()

# --- 7. 绘制 Figure 6.19 ---
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Figure 6.19: Mixture Density Network Results', fontsize=16)

# (a) Plot mixing coefficients pi_k(x)
ax_a = axes[0, 0]
ax_a.plot(x_plot_range, pi_vals_np[:, 0], label=r'$\pi_1(x)$', color='blue')
ax_a.plot(x_plot_range, pi_vals_np[:, 1], label=r'$\pi_2(x)$', color='green')
ax_a.plot(x_plot_range, pi_vals_np[:, 2], label=r'$\pi_3(x)$', color='red')
ax_a.set_xlabel(r'$x$')
ax_a.set_ylabel(r'$\pi_k(x)$')
ax_a.set_title('(a) Mixing Coefficients $\pi_k(x)$')
ax_a.legend()
ax_a.grid(True)

# (b) Plot means mu_k(x)
ax_b = axes[0, 1]
ax_b.plot(x_plot_range, mu_vals_np[:, 0], label=r'$\mu_1(x)$', color='blue')
ax_b.plot(x_plot_range, mu_vals_np[:, 1], label=r'$\mu_2(x)$', color='green')
ax_b.plot(x_plot_range, mu_vals_np[:, 2], label=r'$\mu_3(x)$', color='red')
ax_b.set_xlabel(r'$x$')
ax_b.set_ylabel(r'$\mu_k(x)$')
ax_b.set_title(r'(b) Means $\mu_k(x)$')
ax_b.legend()
ax_b.grid(True)

# (c) Plot contours of p(t|x)
ax_c = axes[1, 0]
# Define a fine grid for x and t
x_grid = np.linspace(0, 1, 100)
t_grid = np.linspace(-0.2, 1.2, 100) # Adjusted based on data range
X_mesh, T_mesh = np.meshgrid(x_grid, t_grid)
X_flat = X_mesh.flatten().astype(np.float32)
T_flat = T_mesh.flatten().astype(np.float32)

x_tensor = torch.tensor(X_flat).unsqueeze(-1).to(device)
t_tensor = torch.tensor(T_flat).unsqueeze(-1).to(device)

with torch.no_grad():
    pi_grid, mu_grid, sigma_grid = model(x_tensor)
    # Reshape for broadcasting
    pi_grid = pi_grid.cpu().numpy().reshape(len(t_grid), len(x_grid), -1) # (H, W, K)
    mu_grid = mu_grid.cpu().numpy().reshape(len(t_grid), len(x_grid), -1) # (H, W, K)
    sigma_grid = sigma_grid.cpu().numpy().reshape(len(t_grid), len(x_grid), -1) # (H, W, K)
    
    # Calculate p(t|x) for each point on the grid
    t_expanded = t_tensor.cpu().numpy().reshape(len(t_grid), len(x_grid), 1) # (H, W, 1)
    
    # Gaussian PDF calculation
    normalizer = np.log(sigma_grid * np.sqrt(2 * np.pi))
    exponent = -0.5 * ((t_expanded - mu_grid) / sigma_grid)**2
    log_prob = - normalizer + exponent
    weighted_log_prob = np.log(pi_grid) + log_prob
    
    log_p_tx = np.logaddexp.reduce(weighted_log_prob, axis=-1) # Log-Sum-Exp
    p_tx = np.exp(log_p_tx)

# Create contour plot with colored lines and white background
# Use contour instead of contourf for the lines only
contour_set = ax_c.contour(X_mesh, T_mesh, p_tx, levels=15, cmap='viridis') # Colored lines
ax_c.clabel(contour_set, inline=True, fontsize=8, fmt='%1.2f') # Add labels to contours
# Add scatter plot with green points
ax_c.scatter(X_train_tensor.cpu().numpy(), T_train_tensor.cpu().numpy(), c='green', s=10, alpha=0.7, edgecolors='black', linewidth=0.3)
ax_c.set_xlabel(r'$x$')
ax_c.set_ylabel(r'$t$')
ax_c.set_title('(c) Contours of Conditional Density $p(t|x)$')

# (d) Plot approximate conditional mode
ax_d = axes[1, 1]
# Find the mode by finding the k that maximizes pi_k for each x
dominant_component_idx = np.argmax(pi_vals_np, axis=1) 
mode_approximation = mu_vals_np[np.arange(len(mu_vals_np)), dominant_component_idx]

# Plot the training data points
ax_d.scatter(X_train_tensor.cpu().numpy(), T_train_tensor.cpu().numpy(), c='green', s=15, alpha=0.6, label='Training Data')
# Plot the approximate mode
ax_d.plot(x_plot_range, mode_approximation, 'r.', label='Approx. Conditional Mode', linewidth=2)
ax_d.set_xlabel(r'$x$')
ax_d.set_ylabel(r'$t$')
ax_d.set_title('(d) Approximate Conditional Mode')
ax_d.legend()
ax_d.grid(True)

plt.tight_layout()
plt.show()

# Optional: Plot the training loss curve
plt.figure(figsize=(8, 4))
plt.plot(losses)
plt.title('Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.show()