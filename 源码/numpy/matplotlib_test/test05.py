import numpy as np
import matplotlib.pyplot as plt
y = np.arange(5)
x1 = np.array([10, 8, 7, 11, 13])
# 条形的高度
bar_height = 0.3
# 绘制条形图
plt.barh(y, x1, tick_label=['a', 'b', 'c', 'd', 'e'],
         height=bar_height)
plt.show()
