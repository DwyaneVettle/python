"""
    绘制柱状图:
        bar(x,height,width,tick_label)
        x:表示x坐标轴
        height:表示各个柱状图的高度
        width:表示柱状图宽度
        tick_label:表示柱形图对应的刻度标签
"""
import matplotlib.pyplot as plt
import numpy as np
# 1.准备数据
x = np.arange(5)
height = np.array([10, 8, 7, 11, 13])
bar_width = 0.3
label = ['a', 'b', 'c', 'd', 'e']
# 绘制图形
plt.bar(x, height, width=bar_width, tick_label=label)
# 显示图形
plt.show()

