"""
    演示matplotlib：
        安装：pip install matplotlib
            numpy:pip install numpy
            pandas:pip install pandas
"""
# 导包  import 包名 as(起别名) 别名
import matplotlib.pyplot as plt
import numpy as np
# 1.准备数据
data = np.array([1, 2, 3, 4, 5])
# 2.创建一个画布-Figure对象
fig = plt.figure()
# 在画布上添加坐标系风格的绘图区域
ax = fig.add_subplot(111)
# 3.绘制图表 - 折线图plot()
ax.plot(data)
# 4.现实图表
plt.show()
