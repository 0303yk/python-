import numpy as np
import matplotlib.pyplot as plt

data = np.array([[3, 2], [4, 1], [3, 6], [4, 7], [3, 9], [6, 8], [6, 6], [7, 7]])

plt.scatter(data[:, 0], data[:, 1], c="blue", marker='o', label='samples')  # 以红色圆圈样式绘制散点图并加上标签
plt.legend()  # 设置图例，图例内容为上面设置的label参数

#KMeans聚类（聚类成2类）
from sklearn.cluster import KMeans
kms = KMeans(n_clusters=2)
label = kms.labels_
plt.scatter(data[label == 0][:, 0], data[label == 0][:, 1], c="red", marker='o', label='class0')  # 以红色圆圈样式绘制散点图并加上标签
plt.scatter(data[label == 1][:, 0], data[label == 1][:, 1], c="green", marker='*', label='class1')  # 以绿色星星样式绘制散点图并加上标签
plt.legend()  # 设置图例

#聚类成3类，并可视化呈现
kms_3 = KMeans(n_clusters=3)
kms_3.fit(data)
label_3 = kms_3.labels_
print(label_3)
plt.scatter(data[label_3 == 0][:, 0], data[label_3 == 0][:, 1], c="red", marker='o', label='class0')  # 以红色圆圈样式绘制散点图并加上标签
plt.scatter(data[label_3 == 1][:, 0], data[label_3 == 1][:, 1], c="green", marker='*', label='class1')  # 以绿色星星样式绘制散点图并加上标签
plt.scatter(data[label_3 == 2][:, 0], data[label_3 == 2][:, 1], c="blue", marker='+', label='class2')  # 以蓝色加号样式绘制散点图并加上标签
plt.legend()  # 设置图例
