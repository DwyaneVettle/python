import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


x_month = np.array(['1月', '2月', '3月', '4月', '5月', '6月'])
y_sales = np.array([2150, 1050, 1560, 1480, 1530, 1490])
x_citys = np.array(['北京', '上海', '广州', '深圳', '浙江', '山东'])
y_sale_count = np.array([83775, 62860, 59176, 64205, 48671, 39968])
# 创建画布和布局
fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(2, 2)
ax_one = fig.add_subplot(gs[0, 1])
ax_two = fig.add_subplot(gs[1, 0])
ax_thr = fig.add_subplot(gs[1, 1])
# 第一个子图
ax_one.bar(x_month, y_sales, width=0.5, color='#3299CC')
ax_one.set_title('2018年上半年某品牌汽车的销售额')
ax_one.set_ylabel('销售额（亿元）')
# 第二个子图
ax_two.plot(x_citys, y_sale_count, 'm--o', ms=8)
ax_two.set_title('分公司某品牌汽车的销量')
ax_two.set_ylabel('销量（辆）')
# 第三个子图
ax_thr.stackplot(x_citys, y_sale_count, color='#9999FF')
ax_thr.set_title('分公司某品牌汽车的销量')
ax_thr.set_ylabel('销量（辆）')
plt.show()
