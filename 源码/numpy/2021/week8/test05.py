import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1.准备数据
x = [x for x in range(1, 13)]
y1 = [20, 28, 23, 16, 29, 36, 39, 33, 31, 19, 21, 25]  # 产品A
y2 = [17, 22, 39, 26, 35, 23, 25, 27, 29, 38, 28, 20]  # 产品B
labels = ['1月', '2月', '3月', '4月', '5月', '6月', '7月',
          '8月', '9月', '10月', '11月', '12月']

# 将画布划分成2x1矩阵区域，之后在索引为1的区域中绘制子图-折线图
ax1 = plt.subplot(211)
ax1.plot(x, y1, 'm--o', lw=2, ms=5, label='产品A')
ax1.plot(x, y2, 'g--o', lw=2, ms=5, label='产品B')
ax1.set_ylim(10, 45)   # y轴的区间
ax1.set_title('产品A和产品B的销售额')
ax1.set_xlabel('月份')
ax1.set_ylabel('销售额（亿元）')




# 2.遍历折线图数据
for xy1 in zip(x, y1):
    ax1.annotate("%s" % xy1[1], xy=xy1,
                 xytext=(-5, 5), textcoords='offset points')

for xy2 in zip(x, y2):
    ax1.annotate("%s" % xy2[1], xy=xy2,
                 xytext=(-5, 5), textcoords='offset points')
ax1.legend()

# 将画布规划为2x2的矩阵区域，之后在索引3的区域绘制产品A的子图
ax2 = plt.subplot(223)
ax2.pie(y1, radius=1, wedgeprops={'width': 0.5}, labels=labels,
        autopct="%3.1f%%", pctdistance=0.75)
ax2.set_title('产品A的销售额')

# 将画布规划为2x2的矩阵区域，之后在索引4的区域绘制产品B的子图
ax3 = plt.subplot(224)
ax3.pie(y2, radius=1, wedgeprops={'width': 0.5}, labels=labels,
        autopct="%3.1f%%", pctdistance=0.75)
ax3.set_title('产品B的销售额')

# 调整子图之间距离
plt.tight_layout()

plt.show()
