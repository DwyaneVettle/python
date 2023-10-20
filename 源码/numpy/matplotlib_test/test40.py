import matplotlib.pyplot as plt

# 将画布划分为2x2的等分区域
fig, ax_arr = plt.subplots(2, 2)
# 获取sx_arr数组第1行第0列的元素，也就是第3个区域
ax_thr = ax_arr[1, 0]
ax_thr.plot([1, 2, 3, 4, 5])
plt.show()
