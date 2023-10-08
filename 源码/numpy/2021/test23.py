import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1.准备数据
labels = ['哪吒之魔童降世', '流浪地球', '复仇者联盟4：终局之战',
          '疯狂的外星人', '飞驰人生', '烈火英雄', '蜘蛛侠：英雄远征',
          '速度与激情：特别行动', '扫毒2：天地对决', '大黄蜂',
          '惊奇队长', '比悲伤更悲伤的故事', '哥斯拉2：怪兽之王',
          '阿丽塔：战斗天使', '银河补习班']
bar_width = [48.57, 46.18, 42.05, 21.83, 17.03, 16.70, 14.01,
             13.84, 12.85, 11.38, 10.25, 9.46, 9.27, 8.88, 8.64]
y_data = range(len(labels))

# 2.绘制图形
fig = plt.figure()
ax = fig.add_subplot(111)
ax.barh(y_data, bar_width, height=0.3, color='orange')

# x轴y轴标签
ax.set_xlabel("总票房(亿元)")
ax.set_ylabel("电影名称")
# 设置刻度位置、刻度标签
ax.set_yticks(y_data)
ax.set_yticklabels(labels)
# 设置标题
# plt.title("2022年电影票房统计")
ax.set_title("2022年电影票房统计")
# 3.展示图形
plt.show()
