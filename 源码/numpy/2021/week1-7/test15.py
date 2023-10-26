import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
"""
    绘制散点图或期盼图
    scatter(x,y,s,c,marker,alpha,linewidths,edgecolors)
"""
x = np.random.rand(50)
y = np.random.rand(50)
# 随机绘制气泡大小
area = (30 * np.random.rand(50)) ** 2
# 绘制散点图
plt.scatter(x, y, s=area, c='red', alpha=0.3)
# 显示图表
plt.show()
