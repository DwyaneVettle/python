import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
# 准备 x 轴和 y 轴的数据
x = np.arange(3)
y1 = np.array([2.04, 1.57, 1.63])
y2 = np.array([1.69, 1.61, 1.64])
y3 = np.array([4.65, 4.99, 4.94])
y4 = np.array([3.39, 2.33, 4.10])
# 指定测量偏差
error1 = [0.16, 0.08, 0.10]
error2 = [0.27, 0.14, 0.14]
error3 = [0.34, 0.32, 0.29]
error4 = [0.23, 0.23, 0.39]
bar_width = 0.2
# 绘制柱形图
plt.bar(x, y1, bar_width)
plt.bar(x + bar_width, y2, bar_width, align="center",
        tick_label=["春季", "夏季", "秋季"])
plt.bar(x + 2*bar_width, y3, bar_width)
plt.bar(x + 3*bar_width, y4, bar_width)
# 绘制误差棒 : 横杆大小为 3,  线条宽度为 3,  线条颜色为黑色, 数据点标记为像素点
plt.errorbar(x, y1, yerr=error1, capsize=3, elinewidth=2, fmt=' k,')
plt.errorbar(x + bar_width, y2, yerr=error2, capsize=3, elinewidth=2, fmt='k,')
plt.errorbar(x + 2*bar_width, y3, yerr=error3, capsize=3, elinewidth=2, fmt='k,')
plt.errorbar(x + 2*bar_width, y3, yerr=error3, capsize=3, elinewidth=2, fmt='k,')
plt.show()
