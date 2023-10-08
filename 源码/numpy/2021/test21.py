import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 1.准备数据--x，y
x = np.arange(3)
y1 = np.array([2.04, 1.57, 1.63])
y2 = np.array([1.69, 1.61, 1.64])
y3 = np.array([4.65, 4.99, 4.94])
y4 = np.array([3.39, 2.33, 4.10])
# 2.指定误差范围
error1 = [0.16, 0.08, 0.10]
error2 = [0.27, 0.14, 0.14]
error3 = [0.34, 0.32, 0.29]
error4 = [0.23, 0.23, 0.39]
# 设置条形图的宽度
bar_width = 0.2
# 刻度标签准备
labels = ['春季', '夏季', '秋季']
# 3.绘制柱形图
plt.bar(x, y1, bar_width)
plt.bar(x + bar_width, y2, bar_width, tick_label=labels, align='center')
plt.bar(x + 2*bar_width, y3, bar_width)
plt.bar(x + 3*bar_width, y4, bar_width)

# 4.绘制误差棒
plt.errorbar(x, y1, yerr=error1, fmt='k,', capsize=3, capthick=2)
plt.errorbar(x + bar_width, y2, yerr=error2, fmt='k,', capsize=3, capthick=2)
plt.errorbar(x + 2*bar_width, y3, yerr=error3, fmt='k,', capsize=3, capthick=2)
plt.errorbar(x + 3*bar_width, y4, yerr=error4, fmt='k,', capsize=3, capthick=2)

plt.show()
