import numpy as np
import matplotlib.pyplot as plt
x = np.arange(5)
y1 = np.array([10, 8, 7, 11, 13])
# 柱形的宽度
bar_width = 0.3
# 绘制柱形图
plt.bar(x, y1, tick_label=['a', 'b', 'c', 'd', 'e'], width=bar_width)
plt.show()
