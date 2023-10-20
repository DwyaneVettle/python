import matplotlib.pyplot as plt

# 画布被规划为3x2的矩阵区域，之后在索引为6的区域中绘制子图
ax_one = plt.subplot(326)
ax_one.plot([1, 2, 3, 4, 5])
# 画布被绘画为3x1的矩阵区域，之后在索引为2的区域中绘制子图
ax_two = plt.subplot(312)
ax_two.plot([1, 2, 3, 4, 5])
plt.show()


