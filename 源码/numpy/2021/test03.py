import numpy as np
import matplotlib.pyplot as plt
"""
    折线图绘制：plot(x,y)
    如果是多个折线图，可以多次调用plot()
    numpy的arange(start,end,step),start默认从0开始
    start:表示数据的开始-包含
    end:表示数据的结束-不包含
    step:表示数据变化的步长,默认为1可以不写
    np.array([])
"""
x = np.arange(4, 19)
y_max = np.array([32, 33, 34, 34, 33, 31, 30, 29, 30,
                 29, 26, 23, 21, 25, 31])
y_min = np.array([19, 19, 20, 22, 22, 21, 22, 16, 18, 18, 17,
                 14, 15, 16, 16])
# 绘制折线图
plt.plot(x, y_max)
plt.plot(x, y_min)
# 展示图标-show()
plt.show()

