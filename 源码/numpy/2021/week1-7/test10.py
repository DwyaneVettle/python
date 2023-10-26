import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
"""
    hist(x, bins, range, cumulative, histtype)
    x:x轴的数据
    bins:表示矩形条的个数，默认值是10
    range：数据的范围，默认xmin,xmax
    histtype:直方图的类型
            bar:传统直方图-默认
            barstacked:堆积直方图
            step:未填充的直方图
            stepfilled：填充后的直方图
            
"""
# 准备50个随机数作为测试数据-x
scores = np.random.randint(0, 100, 50)
# print(scores)
# 绘制直方图
plt.hist(scores, bins=8, histtype='stepfilled')
plt.show()
