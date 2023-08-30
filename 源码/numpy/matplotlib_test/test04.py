import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1, 8)
y = np.array([10770, 16780, 24440, 30920, 37670, 48200, 57270])
# 绘制柱形图
plt.bar(x, y, tick_label=['FY2013', 'FY2014', 'FY2015', 'FY2016',
                          'FY2017', 'FY2018', 'FY2019'], width=0.5)
plt.show()
