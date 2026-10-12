# 卷积实验：分段运行版

# 大家好，这个实验用最少的 Python 代码，帮助初学者直观理解卷积神经网络里的几个核心概念：

# - 卷积
# - 边缘检测
# - 平移等变性
# - 最大池化
# - 多通道卷积
# - 1×1 卷积

# 我们只用 `numpy` 和 `matplotlib`，不需要任何深度学习框架。

# %%
# ====================================================
## 第 0 段：导入库
# ====================================================
import numpy as np
import matplotlib.pyplot as plt

# **讲解：**  
# 先导入 `numpy` 和 `matplotlib`，后面所有实验都基于它们。

# %%
# ====================================================
# 第 1 段：定义一个简单的灰度图像（8x8，带随机整数噪声）
# ====================================================
np.random.seed(0)  # 固定随机种子，保证每次运行结果一致

img = np.array([
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
], dtype=float)

# 在中间加一条竖线，模拟垂直边缘
img[:, 4:] = 30

# 在 -3 到 3 之间随机生成整数噪声
noise = np.random.randint(low=-3, high=4, size=img.shape)
img = img + noise

print("原始图像（无噪声）：")
print(img)

print("\n加噪后的图像：")
print(img)

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img, cmap='gray')
plt.title("Noisy")
plt.axis('off')

plt.tight_layout()
plt.show()

# ====================================================
# 讲解稿
# ====================================================
#
# 这里我们构造了一个 8×8 的灰度图像。
# 左半边像素值是 10，右半边是 100，中间形成一条明显的垂直边缘。
#
# 然后我们加入了一点随机整数噪声，范围是 -3 到 3。
# 这样做的目的是：模拟真实图像中常见的干扰，
# 也能观察滤波器对噪声的鲁棒性。
#
# 观察：
# 左图是干净的原图，右图是加噪后的图像。
# 边缘仍然可见，但像素值不再完全整齐。
#
# ====================================================

# %%
# ====================================================
# 第 2 段：二维卷积函数
# ====================================================
def conv2d(image, kernel, stride=1, padding=0):
    if padding > 0:
        image = np.pad(image, padding, mode='constant', constant_values=0)

    H, W = image.shape
    M, N = kernel.shape
    out_H = (H - M) // stride + 1
    out_W = (W - N) // stride + 1

    output = np.zeros((out_H, out_W))

    for i in range(out_H):
        for j in range(out_W):
            region = image[i*stride:i*stride+M, j*stride:j*stride+N]
            output[i, j] = np.sum(region * kernel)

    return output

print("conv2d 函数已定义")

# **讲解：**  
# 这是卷积的核心函数，它做的事情就是：
# - 把滤波器放在图像上
# - 对应位置相乘再求和
# - 然后按步长滑动
# - 最后得到一张新的特征图

# 这里同时支持：
# - `stride`：步长
# - `padding`：填充
# 这就是卷积层最基本的运算过程。

# 运行后只打印一行提示，说明函数已准备好。

# %%
# ====================================================
# 第 3 段：垂直边缘检测
# ====================================================
vertical_kernel = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1],
])

vertical_map = conv2d(img, vertical_kernel)

print("垂直边缘检测结果：")
print(vertical_map)

plt.figure(figsize=(4, 4))
plt.imshow(vertical_map, cmap='gray')
plt.title("Vertical Edge")
plt.axis('off')
plt.show()

# **讲解：**  
# 这个滤波器左边是负的，右边是正的，目的是在图像水平方向求差值。这样可以用来检测垂直边缘。

# 当图像中出现从左到右的强度变化时，也就是垂直边缘，它会产生很强的响应。

# 运行后你会看到，特征图在中间边缘处出现明显的正负值。


# %%
# ====================================================
# 第 4 段：水平边缘检测
# ====================================================
horizontal_kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1],
])

horizontal_map = conv2d(img, horizontal_kernel)

print("水平边缘检测结果：")
print(horizontal_map)

plt.figure(figsize=(4, 4))
plt.imshow(horizontal_map, cmap='gray')
plt.title("Horizontal Edge")
plt.axis('off')
plt.show()

# **讲解：**  
# 这个滤波器在垂直方向求差值，用来检测水平边缘。
# 观察：因为原图只有垂直边缘，所以这里几乎全是零。

# 这个滤波器是上面那个的转置。
# 它在垂直方向求差值，用来检测水平边缘。
# 因为我们的图像只有垂直边缘，所以水平边缘的结果几乎全是零。
# 这一步说明：不同的滤波器，检测不同的特征。

# %%
# ====================================================
# 第 5 段：平移等变性
# ====================================================
img_shifted = np.roll(img, shift=1, axis=1)
vertical_map_shifted = conv2d(img_shifted, vertical_kernel)

print("原图垂直边缘结果：")
print(vertical_map)
print("平移后垂直边缘结果：")
print(vertical_map_shifted)

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(vertical_map, cmap='gray')
plt.title("Original Vertical Edge")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(vertical_map_shifted, cmap='gray')
plt.title("Shifted Vertical Edge")
plt.axis('off')

plt.tight_layout()
plt.show()

# **讲解：**  
# 我们把图像向右平移一个像素，再做同样的垂直边缘卷积。
# 你会发现：特征图也整体向右平移了一个像素。
# 这就是平移等变性。
# 意思是：输入平移，输出也对应平移。
# 这正是卷积层天然具备的性质。

# %%
# ====================================================
# 第 6 段：最大池化
# ====================================================
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

print("最大池化结果：")
print(pooled)

plt.figure(figsize=(4, 4))
plt.imshow(pooled, cmap='gray')
plt.title("Max Pooling")
plt.axis('off')
plt.show()

# **讲解：**  
# 池化操作在 2×2 区域取最大值，没有学习参数。
# 效果是：
# - 特征图变小了
# - 但仍然保留了“有没有边缘”的信息
# - 对小幅平移不再敏感
# 这就是局部平移不变性。

# %%
# ====================================================
# 第 7 段：多通道卷积
# ====================================================
img_rgb = np.stack([img, img * 0.5, img * 1.5], axis=2)
print("RGB 图像形状：", img_rgb.shape)

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

print("多通道卷积结果：")
print(multi_map)

plt.figure(figsize=(4, 4))
plt.imshow(multi_map, cmap='gray')
plt.title("Multi-channel Conv")
plt.axis('off')
plt.show()

# **讲解：**  
# 这里我们模拟了一个 RGB 三通道图像。
# 每个通道都有自己的滤波器。
# 卷积时，三个通道分别计算，最后再相加。
# 这就是彩色图像卷积的基本做法。

# %%
# ====================================================
# 第 8 段：1×1 卷积
# ====================================================
def conv1x1(image, weights):
    H, W, C = image.shape
    output = np.zeros((H, W))

    for i in range(H):
        for j in range(W):
            output[i, j] = np.sum(image[i, j, :] * weights)

    return output

weights_1x1 = np.array([0.2, 0.3, 0.5])
out_1x1 = conv1x1(img_rgb, weights_1x1)

print("1x1 卷积结果：")
print(out_1x1)

plt.figure(figsize=(4, 4))
plt.imshow(out_1x1, cmap='gray')
plt.title("1x1 Conv")
plt.axis('off')
plt.show()

# **讲解：**  
# 1×1 卷积的滤波器只有一个像素。
# 它不改变空间尺寸，只对通道方向做加权求和。
# 常用来：
# - 改变通道数
# - 降低通道数
# - 融合不同通道的信息

# %%
# ====================================================
# ## 第 9 段：综合可视化
# ====================================================
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

# **讲解：**  
# 最后我们用 2×3 的图，把结果全部展示出来：

# - 原图
# - 垂直边缘
# - 水平边缘
# - 最大池化
# - 多通道卷积
# - 1×1 卷积

# 这样一眼就能看出每种操作的效果。

# ====================================================
## 建议的动手练习
# ====================================================
# 这个实验虽然代码很短，但覆盖了卷积神经网络最核心的几个概念：

# - 卷积
# - 边缘检测
# - 平移等变性
# - 池化
# - 多通道
# - 1×1 卷积

# 建议大家动手改一改：

# 1. 换滤波器
# 2. 改步长
# 3. 加 Padding
# 4. 改池化方式

# 通过观察结果变化，会理解得更深。

# 1. 把 `vertical_kernel` 改成：
#    ```python
#    [[1, 1, 1],
#     [0, 0, 0],
#     [-1, -1, -1]]
#    ```
# 2. 把 `conv2d` 的 `stride` 改成 2。
# 3. 把 `padding` 改成 1。
# 4. 把 `np.max` 改成 `np.mean`。
# 5. 把 `weights_1x1` 改成两个不同的向量。
