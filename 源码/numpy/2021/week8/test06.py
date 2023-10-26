import numpy as np
import matplotlib.pyplot as plt

# 将画布划分2x2的等分区域
fig, ax_arr = plt.subplots(2, 2)
# 获取数组对象中的第二行，第一列的元素-也就是第三个区域
ax_thr = ax_arr[1, 0]
ax_thr.plot([1, 2, 3, 4, 5])
plt.show()
