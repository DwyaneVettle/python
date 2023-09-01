import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 13)
y_a = np.array([198, 215, 245, 222, 200, 236, 201, 253, 236, 200, 266, 290])
y_b = np.array([203, 236, 200, 236, 269, 216, 298, 333, 301, 349, 360, 368])
y_c = np.array([185, 205, 226, 199, 238, 200, 250, 209, 246, 219, 253, 288])
# 绘制堆积面积图
plt.stackplot(x, y_a, y_b, y_c)
plt.show()
