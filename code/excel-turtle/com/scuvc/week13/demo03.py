"""
    堆积面积图：stackplot()
        x: 横坐标，是一个一维数组
        y:纵坐标，可以是一维数组，也可以二维数组
        labels:刻度标签-每个填充区域
        baseline:计算基线的方法zero
"""
import matplotlib.pyplot as plt
import numpy as np

# 准备数据
x = np.arange(0, 6)
y1 = np.array([1, 4, 3, 5, 6, 7])
y2 = np.array([1, 3, 4, 2, 7, 6])
y3 = np.array([3, 4, 3, 6, 5, 5])
# 绘制图形
plt.stackplot(x, y1, y2, y3)
plt.show()
