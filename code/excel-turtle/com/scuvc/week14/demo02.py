"""
    绘制饼图或者圆环图
    pie(x, explod=None,labels=None,radius=1)
    x: 数据; labels:标签；explod:扇形离开中心点的位置；
    radius:半径；wedgeprops={'width':0.5}:扇形属性，常用宽度
    autopct:数值显示的字符串，指定小数点后的位数:%.1f%
"""
import matplotlib.pyplot as plt
import numpy as np

# 1.准备数据
x = np.array([20, 50, 10, 15, 30, 55])
pie_labels = np.array(['A', 'B', 'C', 'D', 'E', 'F'])

# 2.绘制饼图图形
# plt.pie(x, radius=1,
#         labels=pie_labels, autopct='%3.1f%%')
# 绘制圆环图
plt.pie(x, radius=1, wedgeprops={'width':0.7}, labels=pie_labels,
        autopct='%3.1f%%', pctdistance=0.7)
# 3.显示图形
plt.show()
