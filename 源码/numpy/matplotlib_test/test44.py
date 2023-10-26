import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x1 = np.linspace(0, 2*np.pi, 400)
x2 = np.linspace(0.01, 10, 100)
x3 = np.random.rand(10)
x4 = np.arange(0, 6, 0.5)
y1 = np.cos(x1**2)
y2 = np.sin(x2)
y3 = np.linspace(0, 3, 10)
y4 = np.power(x4, 3)

# 共享每一列子图之间的x轴
fig, ax_arr = plt.subplots(2, 2, sharex='col')
ax1 = ax_arr[0, 0]
ax1.plot(x1, y1)
ax2 = ax_arr[0, 1]
ax2.plot(x2, y2)
ax3 = ax_arr[1, 0]
ax3.scatter(x3, y3)
ax4 = ax_arr[1, 1]
ax4.scatter(x4, y4)
plt.show()
