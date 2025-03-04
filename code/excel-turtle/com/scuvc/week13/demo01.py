"""
    条形图：barh()
        y:条形的y值
        width:条形的宽度
        height:条形的高度
        tick_lable:条形的标签
"""
import matplotlib.pyplot as plt
import numpy as np
# 1.准备数据
y = np.arange(5)
x1 = np.array([10, 8, 7, 11, 13])
x2 = np.array([11, 5, 6, 5, 17])
bar_width = 0.3
label = ['a', 'b', 'c', 'd', 'e']
# 2.绘制图形
plt.barh(y, x1, height=bar_width, tick_label=label)
plt.barh(y, x2, height=bar_width, tick_label=label)
# 3.显示图形
plt.show()
