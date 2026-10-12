import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. 定义一个简单的灰度图像
# ============================================================
img = np.array([
    [10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10],
], dtype=float)

# 在中间加一条竖线，模拟垂直边缘
img[:, 3:] = 100

print("原始图像：")
print(img)

# ============================================================
# 2. 二维卷积函数
# ============================================================
def conv2d(image, kernel, stride=1, padding=0):
    if padding > 0:
        image = np.pad(image, padding, mode='constant', constant_values=0)

    H, W = image.shape
    M, N = kernel.shape
    out_H = (H - M) // stride + 1
    out_W = (W - N) // stride + 1

    output = np.zeros((out_H, out_W))

    for i in range(0, out_H):
        for j in range(0, out_W):
            region = image[i*stride:i*stride+M, j*stride:j*stride+N]
            output[i, j] = np.sum(region * kernel)

    return output

# ============================================================
# 3. 垂直边缘检测
# ============================================================
vertical_kernel = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1],
])

vertical_map = conv2d(img, vertical_kernel)
print("\n垂直边缘检测结果：")
print(vertical_map)

# ============================================================
# 4. 水平边缘检测
# ============================================================
horizontal_kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1],
])

horizontal_map = conv2d(img, horizontal_kernel)
print("\n水平边缘检测结果：")
print(horizontal_map)

# ============================================================
# 5. 平移等变性
# ============================================================
img_shifted = np.roll(img, shift=1, axis=1)
vertical_map_shifted = conv2d(img_shifted, vertical_kernel)

print("\n原图垂直边缘结果：")
print(vertical_map)
print("\n平移后垂直边缘结果：")
print(vertical_map_shifted)

# ============================================================
# 6. 最大池化
# ============================================================
def max_pool2d(image, size=2, stride=2):
    H, W = image.shape
    out_H = (H - size) // stride + 1
    out_W = (W - size) // stride + 1
    output = np.zeros((out_H, out_W))

    for i in range(out_H):
        for j in range(out_W):
            region = image[i*stride:i*stride+size, j*stride:j*stride+size]
            output[i, j] = np.max(region)

    return output

pooled = max_pool2d(vertical_map, size=2, stride=2)
print("\n最大池化结果：")
print(pooled)

# ============================================================
# 7. 多通道卷积
# ============================================================
# 模拟一个 3 通道图像
img_rgb = np.stack([img, img * 0.5, img * 1.5], axis=2)
print("\nRGB 图像形状：", img_rgb.shape)

# 每个通道一个 3x3 滤波器
kernel_rgb = np.stack([
    vertical_kernel,
    vertical_kernel * 0.5,
    vertical_kernel * 1.5,
], axis=2)
print("多通道滤波器形状：", kernel_rgb.shape)

def conv2d_multichannel(image, kernel):
    H, W, C = image.shape
    M, N, C2 = kernel.shape
    assert C == C2

    out_H = H - M + 1
    out_W = W - N + 1
    output = np.zeros((out_H, out_W))

    for i in range(out_H):
        for j in range(out_W):
            region = image[i:i+M, j:j+N, :]
            output[i, j] = np.sum(region * kernel)

    return output

multi_map = conv2d_multichannel(img_rgb, kernel_rgb)
print("\n多通道卷积结果：")
print(multi_map)

# ============================================================
# 8. 1x1 卷积
# ============================================================
def conv1x1(image, weights):
    H, W, C = image.shape
    output = np.zeros((H, W))

    for i in range(H):
        for j in range(W):
            output[i, j] = np.sum(image[i, j, :] * weights)

    return output

weights_1x1 = np.array([0.2, 0.3, 0.5])
out_1x1 = conv1x1(img_rgb, weights_1x1)

print("\n1x1 卷积结果：")
print(out_1x1)

# ============================================================
# 9. 可视化
# ============================================================
fig, axes = plt.subplots(2, 3, figsize=(10, 6))

axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title("Original")
axes[0, 1].imshow(vertical_map, cmap='gray')
axes[0, 1].set_title("Vertical Edge")
axes[0, 2].imshow(horizontal_map, cmap='gray')
axes[0, 2].set_title("Horizontal Edge")

axes[1, 0].imshow(pooled, cmap='gray')
axes[1, 0].set_title("Max Pooling")
axes[1, 1].imshow(multi_map, cmap='gray')
axes[1, 1].set_title("Multi-channel Conv")
axes[1, 2].imshow(out_1x1, cmap='gray')
axes[1, 2].set_title("1x1 Conv")

for ax in axes.ravel():
    ax.axis('off')

plt.tight_layout()
plt.show()