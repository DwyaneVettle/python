import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
"""
    堆积面积图-stackplot(x,y,labels, baseline)
    x:x轴的数据
    y:y轴的数据
    labels:每个填充区域的标签
    baseline：计算基线的方法，zero,sym,wiggle,weight_wiggle
"""
x = np.arange(6)
y1 = np.array([1, 4, 3, 5, 6, 7])
y2 = np.array([1, 3, 4, 2, 7, 7])
y3 = np.array([3, 4, 3, 5, 5, 7])
# 绘制堆积面积图
plt.stackplot(x, y1, y2, y3)
plt.show()
