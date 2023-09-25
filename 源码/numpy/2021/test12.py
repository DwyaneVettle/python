import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
"""
    pie(x, expload,labes,autopct,pctdistance,labeldistance)
    - **x：**表示扇形或楔形的数据。
    - **explode：**表示扇形或楔形<font color="red">离开圆心的距离</font>。
    - **labels：**表示扇形或楔形对应的标签文本。
    - **autopct：**表示控制扇形或楔形的数值显示的字符串，可通过格式字符串指定小数点后的位数。
    - **pctdistance：**表示扇形或楔形对应的数值标签距离圆心的比例，默认为0.6。
    - **shadow：**表示是否<font color="red">显示阴影</font>。
    - **labeldistance：**表示标签文本的绘制位置（相对于半径的比例），默认为1.1。
"""

data = np.array([20, 50, 10, 15, 30, 55])
pie_labels = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
# 绘制饼图
plt.pie(data, radius=1.5, labels=pie_labels, autopct='%3.1f%%')
plt.show()

