import numpy as np
import matplotlib.pyplot as plt

"""
    线条的样式：默认是实现
    任何的图形化绘制方法中都有一个属性-linestyle
    短虚线：':'
    长虚线：'--'
    点划线：'-.'
    实线：'-'
    数据标记：marker
    填充型数据标记：正方形、三角形等
    非填充型数据标记：加减乘除..
    mec:表示填充图案的边框颜色
    mew:填充边框的宽度
    mfc:数据标记的颜色
    mfcalt:数据标记的备用颜色
    ms:数据标记的大小
    matplotlib提供了为线条设置颜色、标记、线型的格式化方式
    语法：cms
"""
x = [1, 2, 3]
y = [4, 5, 6]
# plt.plot(x, y, linestyle='-', marker='*', mec='r',
#          mew=1, mfc='y', mfcalt='g', ms=20)
plt.plot(x, y, 'mh-.')
plt.show()
