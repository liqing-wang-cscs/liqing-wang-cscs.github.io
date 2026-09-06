import numpy as np
import matplotlib.pyplot as plt

# ==================== 1. 读取图像并提取红色通道 ====================
image = plt.imread('rice.png')
red_channel = image[:, :, 0]  # 提取 RGB 图像中的红色通道（灰度矩阵）

# ==================== 2. 对红色通道进行奇异值分解（SVD） ====================
U, S, Vh = np.linalg.svd(red_channel)

# ==================== 3. 取前 p 个奇异值进行低秩近似 ====================
p = 10  # 保留的奇异值个数（秩），数值越大图像越清晰，但压缩率越低

U_truncated = U[:, 0:p]          # 左奇异向量矩阵，取前 p 列
S_truncated = np.diag(S[0:p])    # 奇异值矩阵，取前 p 个对角元素
Vh_truncated = Vh[0:p, :]        # 右奇异向量矩阵，取前 p 行

# 重构近似矩阵：B ≈ U_p · Σ_p · Vh_p
approximated = U_truncated @ S_truncated @ Vh_truncated

# ==================== 4. 绘制原图与近似图的对比 ====================
fig = plt.figure(figsize=(12, 5))

ax1 = fig.add_subplot(121)
ax1.imshow(red_channel, cmap='summer')
ax1.set_title('Original (Full Rank)')
ax1.axis('off')

ax2 = fig.add_subplot(122)
ax2.imshow(approximated, cmap='summer')
ax2.set_title(f'Approximated (Rank = {p})')
ax2.axis('off')

plt.tight_layout()
plt.show()

# ==================== 5. 对比存储空间 ====================
original_size = np.size(red_channel)
compressed_size = np.size(U_truncated) + np.size(S_truncated) + np.size(Vh_truncated)

print(f'原图存储元素数：{original_size}')
print(f'近似图存储元素数：{compressed_size}')
print(f'压缩率：{compressed_size / original_size:.2%}')
