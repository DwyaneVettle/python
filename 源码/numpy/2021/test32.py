import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 准备数据
x = np.arange(5)
y1 = [1200, 2400, 1800, 2200, 1600]
y2 = [1000, 2100, 1300, 1600, 1340]

bar_width = 0.5
tick_label = ['家庭', '小说', '心里', '科技', '儿童']

fig = plt.figure()
"""
    将画布分割程1行1列，图像画在从左到右从上到下的第一块位置
    当只想画一张图是就是用111
"""
ax = fig.add_subplot(111)

# 绘制柱形图
ax.bar(x, y1, bar_width, color='#FFCC00', align='center', label='地区1')
ax.bar(x, y2, bar_width, color='#B0C4DE', align='center', label='地区2')

ax.set_ylabel('采购数量（本）')
ax.set_xlabel('图书种类')
ax.set_title('地区1和地区2对各类图书的采购情况')
ax.set_xticks(x)
ax.set_xticklabels(tick_label)
ax.legend()
ax.grid(True, axis='y', color='gray', alpha=0.5)
plt.show()


