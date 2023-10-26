import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = np.array([20, 50, 10, 15, 30, 55])
pie_labels = np.array(['a', 'b', 'c', 'd', 'e', 'f'])

# 绘制圆环图
plt.pie(data, radius=1.5, wedgeprops={'width': 0.8},
        labels=pie_labels, autopct='%3.1f%%', pctdistance=0.75)
plt.show()
