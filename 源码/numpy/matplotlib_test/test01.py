import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4, 19)
y_max = np.array([32, 33, 34, 34, 33, 31, 30, 29, 30,
                  29, 26, 23, 21, 25, 31])
y_min = np.array([19, 19, 20, 22, 22, 21, 22, 16, 18,
                  18, 17, 14, 15, 16, 16])
# 绘制折线图
plt.plot(x, y_max)
plt.plot(x, y_min)
plt.show()
