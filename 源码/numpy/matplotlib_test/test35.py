import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(4, 19)
y_max = np.array([32, 33, 34, 34, 33, 31, 30, 29, 30,
                  29, 26, 23, 21, 25, 31])
y_min = np.array([19, 19, 20, 22, 22, 21, 22, 16, 18,
                  18, 17, 14, 15, 16, 16])
# 绘制折线图
plt.plot(x, y_max, marker='o', label='最高温度')
plt.plot(x, y_min, marker='o', label='最低温度')
plt.show()
# 为图表添加注释并设置字体的样式
x_temp = 4
for y_h, y_l in zip(y_max, y_min):
    plt.text(x_temp-0.3, y_h + 0.7, y_h, family='SimHei', fontsize=8, fontstyle='normal')
    plt.text(x_temp-0.3, y_l + 0.7, y_l, family='SimHei', fontsize=8, fontstyle='normal')
    x_temp += 1
plt.title('未来15天最高气温和最低气温的走势')
plt.xlabel('日期')
plt.ylabel('温度($^\\circ$C)')
plt.ylim(0, 40)
plt.legend()
plt.show()
