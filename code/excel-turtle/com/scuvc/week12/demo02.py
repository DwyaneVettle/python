"""
    折线图案例：
        如果有多条折线图可以反复调用plot()
"""
import numpy as np
import matplotlib.pyplot as plt
# 1.准备数据
x = np.arange(4, 19)
y_max = np.array([32, 33, 34, 34, 33, 31, 30, 29, 30, 29, 26,
                  23, 21, 25, 31])
y_min = np.array([19, 19, 20, 22, 22, 21, 22, 16, 18,
                  18, 17, 14, 15, 16, 16])
# 2.绘制图形
plt.plot(x, y_min)
plt.plot(x, y_max)
# 3.显示图形
plt.show()


