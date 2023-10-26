import numpy as np
import matplotlib.pyplot as plt

"""
    使用subplot()绘制子图，nrows行数,ncold列数  index区域序号，默认从1开始
"""
# 将画布划分成3*2矩阵区域，在索引为6的区域绘制子图
ax_one = plt.subplot(326)
ax_one.plot([1, 2, 3, 4, 5])

# 将画布规划为3*1的矩阵区域，之后在索引为2的区域绘制子图
ax_two = plt.subplot(312)
ax_two.plot([1, 2, 3, 4, 5])

plt.show()
