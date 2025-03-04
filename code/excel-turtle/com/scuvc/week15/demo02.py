import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data_2018 = np.array([5200, 5254.5, 5283.4, 5107.8, 5443.3,
                      5550.6, 6400.2, 6404.9, 5483.1, 5330.2, 5543,
                      6199.9])
data_2017 = np.array([4605.2, 4710.3, 5168.9, 4767.2, 4947,
                      5203, 6047.4, 5945.5, 5219.6, 5038.1, 
                      5196.3, 5698.6])
label = ('2018年', '2017年')
# 绘制箱型图
plt.boxplot([data_2018, data_2017], label=label, meanline=True,
            vert=False, patch_artist=True, widths=0.5)
plt.show()

