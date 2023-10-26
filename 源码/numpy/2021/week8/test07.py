import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 添加无指向型的文本
def autolabel(ax, rects):
    # 在每个矩形条上方附加一个文本标签，以显示其高度
    for rect in rects:
        width = rect.get_width()  # 获取每个矩形条的高度
        ax.text(width + 3, rect.get_y(), s="{}".format(width),
                ha='center', va='bottom')


y = np.arange(12)
x1 = np.array([19, 33, 28, 29, 14, 24, 57, 6, 26, 15, 27, 39])
x2 = np.array([25, 33, 58, 39, 15, 64, 29, 23, 22, 11, 27, 50])
labels = np.array(['中国', '加拿大', '巴西', '澳大利亚', '日本', '墨西哥',
                   '俄罗斯', '韩国', '瑞士', '土耳其', '英国', '美国'])

# 将画布划分为1x2的矩阵区域，依次在每个区域中绘制子图
fig, (ax1, ax2) = plt.subplots(1, 2)
barh_rects = ax1.barh(y, x1, height=0.5, tick_label=labels,
         color='orange')

ax1.set_xlabel('人群比例（%）')
ax1.set_title('部分国家养猫人群的比例')
autolabel(ax1, barh_rects)

barh2_rects = ax2.barh(y, x2, height=0.5, tick_label=labels,
                       color='green')

ax2.set_xlabel('人群比例（%）')
ax2.set_title('部分国家养狗人群的比例')
autolabel(ax2, barh2_rects)

# 调整子图之间的距离
plt.tight_layout()
plt.show()
