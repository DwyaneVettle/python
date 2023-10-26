import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 准备数据-随机100
data = np.random.rand(100)

plt.boxplot(data, meanline=True, widths=0.3, showfliers=False,
            patch_artist=True)

plt.show()
