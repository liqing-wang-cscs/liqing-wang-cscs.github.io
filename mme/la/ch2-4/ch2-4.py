import numpy as np

# ==================== 1. 定义评分矩阵 ====================
# 行：用户（第17行对应"高辛"）
# 列：菜品（0~10号）
# 值为0表示未评分
A = np.array([
    [5, 2, 1, 4, 0, 0, 2, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
    [1, 0, 5, 2, 0, 0, 3, 0, 3, 0, 1],
    [0, 5, 0, 0, 4, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 5, 0],
    [5, 0, 2, 4, 2, 1, 0, 3, 0, 1, 0],
    [0, 4, 0, 0, 5, 4, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 4, 0, 4, 5, 0],
    [0, 0, 0, 4, 0, 0, 1, 5, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 0, 0, 0, 0, 3],
    [4, 2, 1, 4, 0, 0, 2, 4, 0, 0, 0],
    [0, 1, 4, 1, 2, 1, 5, 0, 5, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0],
    [2, 5, 0, 0, 4, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 4, 2, 0, 0],
    [0, 2, 4, 0, 4, 3, 4, 0, 0, 0, 0],
    [0, 3, 5, 1, 0, 0, 4, 1, 0, 0, 0],
])

# ==================== 2. 计算菜品间的相似度矩阵 ====================
num_dishes = A.shape[1]  # 菜品数量

# 方法一：手动计算皮尔逊相关系数
mean_per_dish = np.mean(A, axis=0)          # 每道菜的平均分
centered = A - mean_per_dish                # 中心化矩阵

R = np.zeros([num_dishes, num_dishes])
for i in range(num_dishes):
    for j in range(num_dishes):
        numerator = np.sum(centered[:, i] * centered[:, j])
        denominator = np.sqrt(np.sum(centered[:, i] ** 2)) * np.sqrt(np.sum(centered[:, j] ** 2))
        R[i, j] = numerator / denominator

# 方法二：用 NumPy 内置函数验证（结果一致）
# R2 = np.corrcoef(A)

# 将相关系数 [-1, 1] 映射到相似度 [0, 1]
similarity = (R + 1) / 2

# ==================== 3. 基于相似度的协同过滤推荐 ====================
# 高辛（第17行）的评分情况
user_idx = 17
rated_dishes = (1, 2, 3, 6, 7)        # 已评分的菜品
unrated_dishes = (0, 4, 5, 8, 9, 10)  # 未评分的菜品

print(f"=== 为用户 {user_idx}（高辛）推荐未评分菜品 ===\n")

for target_dish in unrated_dishes:
    weighted_sum = 0.0
    similarity_sum = 0.0

    for rated_dish in rated_dishes:
        weighted_sum += A[user_idx, rated_dish] * similarity[rated_dish, target_dish]
        similarity_sum += similarity[rated_dish, target_dish]

    predicted_score = weighted_sum / similarity_sum
    print(f"对高辛推荐菜品{target_dish}的打分估计为：{predicted_score:.2f}")
    