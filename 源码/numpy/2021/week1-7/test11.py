import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 准备10000个随机数
random_state = np.random.RandomState(189325).randn(10000)
# 绘制直方图
plt.hist(random_state, bins=25)
plt.show()
