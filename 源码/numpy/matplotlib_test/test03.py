import numpy as np
import matplotlib.pyplot as plt
x = np.arange(5)
y1 = np.array([10, 8, 7, 11, 13])
y2 = np.array([19, 6, 5, 10, 12])
# 柱形的宽度
bar_width = 0.3
# 误差棒定义
error = [2, 1, 2.5, 2, 1.5]
# 根据多组数据绘制柱形图
plt.bar(x, y1, tick_label=['1月', '2月', '3月', '4月', '5月'],
        width=bar_width)
# plt.bar(x+bar_width, y2, width=bar_width)
plt.bar(x, y2, bottom=y1, width=bar_width, yerr=error)
plt.show()
