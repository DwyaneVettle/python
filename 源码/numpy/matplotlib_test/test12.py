import numpy as np
import matplotlib.pyplot as plt
data = np.array([20, 50, 10, 15, 30, 55])
pie_labels = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
# 绘制圆环图
plt.pie(data, radius=1.5, wedgeprops={'width': 0.7},
           labels=pie_labels, autopct='%3.1f%%',
           pctdistance=0.75)
plt.show()
