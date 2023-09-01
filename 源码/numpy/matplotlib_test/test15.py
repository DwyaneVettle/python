import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 准备x轴和y轴数据
x_speed = np.arange(10, 210, 10)
y_distance = np.array([0.5, 2.0, 4.4, 7.9, 12.3, 17.7,
                       24.1, 31.5, 39.9, 49.2, 59.5, 70.8,
                       83.1, 96.4, 110.7, 126.0, 142.2,
                       159.4, 177.6, 196.8])
# 绘制散点图
plt.scatter(x_speed, y_distance, s=50, alpha=0.9)
plt.show()
