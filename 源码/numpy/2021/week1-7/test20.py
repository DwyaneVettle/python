import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

"""
    errorbar()
    x,y:表示数据点的位置
    xerr,yerr:表示数据误差范围
    fmt:连接线的样式
    capsize:横杆的大小
    capthick:横杆的宽度
"""
x = np.arange(5)
y = (25, 32, 34, 20, 25)
y_error = (5, 10, 3, 5, 5)
plt.errorbar(x, y, yerr=y_error, capsize=3, capthick=2)
plt.show()
