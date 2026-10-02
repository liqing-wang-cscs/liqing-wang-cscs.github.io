import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import seaborn as sns

# 设置中文字体（可选，如需中文标签）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

# 加载鸢尾花数据集
iris = load_iris()
X = iris.data  # [sepal_length, sepal_width, petal_length, petal_width]
y = iris.target  # 0: setosa, 1: versicolor, 2: virginica

# 仅使用 sepal length 和 sepal width（对应第0列和第1列）
X_sepal = X[:, [0, 1]]  # shape: (150, 2)
feature_names = iris.feature_names
print(f"特征名称: {feature_names}")
print(f"使用的特征: {feature_names[0]} (sepal length), {feature_names[1]} (sepal width)")

# 划分训练集和测试集（保留部分用于演示分类）
X_train, X_test, y_train, y_test = train_test_split(
    X_sepal, y, test_size=0.2, random_state=42, stratify=y
)

# 使用KNN分类器（简单直观，符合图中"最近邻"直觉）
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 创建一个新测试点（如图中 × 所示位置：约 sepal_length=5.8, sepal_width=3.0）
test_point = np.array([[5.5, 3.0]])  # 位于红点（setosa）和绿点（versicolor）之间
predicted_class = knn.predict(test_point)[0]
predicted_name = iris.target_names[predicted_class]

print(f"\n测试点坐标: sepal_length={test_point[0,0]}, sepal_width={test_point[0,1]}")
print(f"预测类别: {predicted_name} (类别 {predicted_class})")

# 绘制散点图（Figure 6.1 风格）
plt.figure(figsize=(8, 6))
colors = ['red', 'green', 'blue']
markers = ['o', 'o', 'o']
# markers = ['o', 's', '^']
labels = iris.target_names

# 绘制训练数据点
for i, (color, marker, label) in enumerate(zip(colors, markers, labels)):
    mask = y_train == i
    plt.scatter(X_train[mask, 0], X_train[mask, 1],
                c=color, marker=marker, s=50, alpha=0.7, label=label, edgecolors='k', linewidth=0.5)

# 绘制测试点（用 × 表示）
plt.scatter(test_point[0, 0], test_point[0, 1],
            c='black', marker='x', s=100, linewidths=2, zorder=5,
            label=f'测试点 → {predicted_name}')

# 添加坐标轴标签
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.title('Figure 6.1: Iris 数据集（仅使用 sepals）\n红: Setosa, 绿: Versicolor, 蓝: Virginica')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)

# 可选：添加决策边界（展示分类区域）
xx, yy = np.meshgrid(np.linspace(X_sepal[:,0].min()-0.5, X_sepal[:,0].max()+0.5, 100),
                      np.linspace(X_sepal[:,1].min()-0.5, X_sepal[:,1].max()+0.5, 100))
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.1, levels=np.arange(-0.5, 3.5, 1), colors=['#ffcccc', '#ccffcc', '#ccccff'])

plt.tight_layout()
plt.show()

# 额外：打印分类结果摘要
print("\n--- 分类结果摘要 ---")
print(f"训练样本数: {len(X_train)}")
print(f"测试样本数: {len(X_test)}")
print(f"各类别分布（训练集）:")
for i, name in enumerate(labels):
    count = (y_train == i).sum()
    print(f"  {name}: {count} 个")

# 可选：评估模型在测试集上的准确率
y_pred = knn.predict(X_test)
accuracy = (y_pred == y_test).mean()
print(f"\nKNN分类器在测试集上的准确率: {accuracy:.2%}")