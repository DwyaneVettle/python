import numpy as np
import matplotlib.pyplot as plt
data = np.array([20, 50, 10, 15, 30, 55])
pie_labels = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
# 绘制饼图：半径为0.5，数值保留1位小数
plt.pie(data, radius=1.5, labels=pie_labels, autopct='%3.1f%%')
plt.show()
