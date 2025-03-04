"""
    误差棒：errorbar()
        x,y:数据点的位置
        xerr,yerr:误差范围
        capsize：误差棒大小
        capthick:误差棒边界厚度
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
y = (25, 32, 34, 21, 25)
y_offset = (3, 5, 2, 3, 3)
# 绘制误差棒
plt.errorbar(x, y, y_offset, capsize=3, capthick=2)
plt.show()
