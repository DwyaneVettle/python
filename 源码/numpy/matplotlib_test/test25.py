import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
men_means = (90.5, 89.5, 88.7, 88.5, 85.2, 86.6)
women_means = (92.7, 87.0, 90.5, 85.0, 89.5, 89.8)
# 每组柱形的x位置
ind = np.arange(len(men_means))
# 各柱形的宽度
width = 0.2
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(ind - width / 2, men_means, width, label='男生平均成绩')
ax.bar(ind + 0.2, women_means, width, label='女生平均成绩')
ax.set_title('高二各班男生、女生英语平均成绩')
ax.set_ylabel('分数')
ax.set_xticks(ind)
ax.set_xticklabels(['高二1班', '高二2班', '高二3班', '高二4班', '高二5班',
                    '高二6班'])

# 添加参考线
ax.axhline(88.5, ls='--', linewidth=1.0, label='全体平均成绩')
ax.legend(loc='lower right')
plt.show()
