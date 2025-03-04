"""
    散点图或气泡图：
        scatter()
        x,y:数据点的位置
        s:数据点的大小
        c：数据点的颜色
        marker:表示数据点的样式，默认为圆形 'o'
        linewidth:数据描边的宽度
        edgecolors:数据描边的颜色
"""

import matplotlib.pyplot as plt
import numpy as np

num = 70  # 散点的个数
x = np.random.rand(num)  # 随机生成位置
y = np.random.rand(num)

# 绘制散点图
# plt.scatter(x, y, s=2.5, c='red')
# 绘制气泡图-将大小随机
size = np.random.rand(num) ** 2 * 30
plt.scatter(x, y, s=size, c='red')
# 显示图形
plt.show()
