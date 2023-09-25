import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
kinds = ['面粉', '全麦面', '酵母', '苹果酱', '鸡蛋', '黄油', '盐', '白糖']
weight = [250, 150, 4, 250, 50, 30, 4, 20]
total_weight = 0
for i in weight:
    total_weight += 1
batching_scale = [i / total_weight for i in weight]
plt.pie(batching_scale, autopct='%3.1f%%')
plt.legend(kinds, loc='upper right', bbox_to_anchor=[1.1, 1.1])
# 添加表格
plt.table(cellText=[weight],
          cellLoc='center',
          rowLabels=['重量(g)'],
          colLabels=kinds,
          loc='lower center')
plt.show()
