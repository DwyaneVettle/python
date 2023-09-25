import numpy as np
import matplotlib.pyplot as plt
"""
    绘制柱状图/堆积柱形图
    bar(x, height, width, tick_label, xerr, yerr)
    x表示x轴的数据个数，tick_label表示x轴的刻度值[]
"""
# x轴个数
x = np.arange(5)
# 高度
y1 = np.array([10, 8, 7, 11, 13])
y2 = np.array([12, 6, 8, 11, 15])

# 误差棒的值
error = [4, 2, 1, 6, 3]
# 宽度
bar_width = 0.3
# 刻度
tick = ['a', 'b', 'c', 'd', 'e']
# 绘制柱状图
plt.bar(x, y1, width=bar_width, tick_label=tick)
# 绘制第二条柱状图
plt.bar(x, y2, bottom=y1, width=bar_width, yerr=error)
# 展示
plt.show()

