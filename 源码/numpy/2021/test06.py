import numpy as np
import matplotlib.pyplot as plt

"""
    绘制条形图(堆积条形图)：barh(y, width, height, tick_label, xerr, yerr)
    y:y轴上的数据个数
    height:条形图的宽度
"""
y = np.arange(5)
x1 = np.array([10, 8, 7, 11, 13])
x2 = np.array([9, 6, 4, 15, 10])
tick = ['a', 'b', 'c', 'd', 'e']
error = [3, 5, 6, 4, 3]
# 绘制条形图
plt.barh(y, x1, tick_label=tick, height=0.4)
plt.barh(y, x2, left=x1, height=0.4, xerr=error)
plt.show()
