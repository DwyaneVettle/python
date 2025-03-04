import matplotlib.pyplot as plt
import numpy as np

# 1.准备数据
x = np.arange(5)
y1 = np.array([10, 8, 7, 11, 13])
y2 = np.array([19, 6, 5, 10, 12])
# 助兴的宽度
bar_width = 0.2
# 2.绘制图形
plt.bar(x, y1, width=bar_width, tick_label=['1月', '2月', '3月', '4月', '5月'])
# plt.bar(x+bar_width, y2, width=bar_width)
plt.bar(x, y2, width=bar_width, bottom=y1)  # 堆积柱状图的绘制
# 3.显示图形
plt.show()

