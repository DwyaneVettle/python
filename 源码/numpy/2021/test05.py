import numpy as np
import matplotlib.pyplot as plt

# bar(x, height, width, tick_label)

x = np.arange(1, 8)
y1 = np.array([10770, 16780, 24440, 30920, 37670, 48200, 57270])
y2 = np.array([24440, 30920, 57270, 48200, 37670, 24440, 16780])

# 绘制柱状图
plt.bar(x, y1, tick_label=['FY2013', 'FY2014', 'FY2015',
                           'FY2016', 'FY2017', 'FY2018', 'FY2018'],
        width=0.5)
plt.bar(x + 0.5, y2, width=0.5)
plt.show()
