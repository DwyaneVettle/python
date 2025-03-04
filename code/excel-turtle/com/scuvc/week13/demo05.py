"""
    直方图：hist()
        x:x轴的护具
        bins:矩形条的个数默认为10
        histtype:直方图的类型
        np.random.randint(0, 100, 50)表示准备50
        个0-100之间的整数
"""
import numpy as np
import matplotlib.pyplot as plt

# 准备数据
scores = np.random.randint(0, 100, 50)
# 绘制直方图
plt.hist(scores, bins=10, histtype='bar')
# 显示图形
plt.show()
