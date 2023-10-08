import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

sale_a = [2144, 4617, 7674, 6666]
sale_b = [853, 1214, 2414, 4409]
sale_c = [153, 155, 292, 680]
fig = plt.figure()
ax = fig.add_subplot(111)
# 绘制具有不同线条样式的折线图
ax.plot(sale_a, 'D-', sale_b, '^:', sale_c, 's--')
ax.grid(alpha=0.3)
ax.set_ylabel('销售额（万元）')
ax.set_xticks(np.arange(len(sale_c)))
ax.set_xticklabels(['第1季度', '第2季度', '第3季度', '第4季度'])
ax.legend(['产品A', '产品B', '产品C'])
plt.show()

