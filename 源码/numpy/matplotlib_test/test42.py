import numpy as np
import matplotlib.pyplot as plt

# 将画布规划成2x3的矩阵区域，之后在第0行第2列的区域中绘制子图
ax1 = plt.subplot2grid((2, 3), (0, 2))
ax1.plot([1, 2, 3, 4, 5])
# 画布被规划成2x3的矩阵区域，之后在第一行第1-2列的区域中绘制子图
ax2 = plt.subplot2grid((2, 3), (1, 1), colspan=2)
ax2.plot([1, 2, 3, 4, 5])
plt.show()
