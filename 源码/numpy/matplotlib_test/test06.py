import numpy as np
import matplotlib.pyplot as plt

y = np.arange(5)
x1 = np.array([10, 8, 7, 11, 13])
x2 = np.array([9, 6, 5, 10, 12])
bar_height = 0.3
error = [2, 1, 2.5, 2, 1.5]
plt.barh(y, x1, tick_label=['a', 'b', 'c', 'd', 'e'], height=bar_height)
# plt.barh(y+bar_height, x2, height=bar_height)
plt.barh(y, x2, left=x1, height=bar_height, xerr=error)
plt.show()
