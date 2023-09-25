import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = np.arange(1, 8)
y = np.array([10770, 16780, 24440, 30920, 37670, 48200, 57270])
# 绘制柱形图
bar_rects = plt.bar(x, y, tick_label=['FY2013', 'FY2014', 'FY2015', 'FY2016',
                          'FY2017', 'FY2018', 'FY2019'], width=0.5)
# 添加无指向型注释文本
def autolabel(rects):
    """在每个矩形条的上方附加一个文本标签，以显示其高度"""
    for rect in rects:
        height = rect.get_height()  # 获取每个矩形条的高度
        plt.text(rect.get_x() + rect.get_width() / 2,
                 height + 300, s='{}'.format(height),
                 ha='center', va='bottom')
autolabel(bar_rects)
plt.ylabel('GMV(亿元)')
plt.show()
