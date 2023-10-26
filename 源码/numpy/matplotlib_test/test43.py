import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data_2017 = np.array([21, 35, 22, 19, 3])
data_2018 = np.array([13, 32, 27, 27, 1])
x = np.arange(5)
y = np.array([51, 73, 99, 132, 45])
labels = np.array(['一线城市', '二线城市', '三线城市', '四线及以外', '其他国家及地区'])

# 平均增长倍数
average = 75
bar_width = 0.5
# 添加无指向型注释文本
def autolabel(ax, rects):
    """ 在每个举行条的上方附加一个文本标签，以显示其高度"""
    for rect in rects:
        height = rect.get_height()  # 获取每个矩形条的高度
        ax.text(rect.get_x() + bar_width / 2, height + 3,
                s='{}'.format(height), ha='center', va='bottom')

# 第一个子图
ax_one = plt.subplot2grid((3, 2), (0, 0), rowspan=2, colspan=2)
bar_rects = ax_one.bar(x, y, tick_label=labels, color='#20B2AA',
                       width=bar_width)
ax_one.set_title('抖音2018vs2017人群增长倍数')
ax_one.set_ylabel('增长倍数')
ax_one.set_ylim(0, y.max() + 20)
ax_one.axhline(y=75, ls='--', lw=1, color='gray')

# 第二个子图
ax_two = plt.subplot2grid((3, 2), (2, 0))
ax_two.pie(data_2017, radius=1.5, labels=labels, autopct='%3.1f%%',
           colors=['#2F4F4F', '#FF0000', '#A9A9A9', '#FFD700', '#B0C4DE'])
ax_two.set_title('2017年抖音用户地区分布的比例')

# 第三个子图
ax_thr = plt.subplot2grid((3, 2), (2, 1))
ax_thr.pie(data_2018, radius=1.5, labels=labels, autopct='%3.1f%%',
           colors=['#2F4F4F', '#FF0000', '#A9A9A9', '#FFD700', '#B0C4DE'])
ax_thr.set_title('2018年抖音用户地区分布的比例')

# 调整子图之间的距离
plt.tight_layout()
plt.show()
