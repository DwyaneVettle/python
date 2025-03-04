import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 13)
import numpy as np
y1 = np.array([198, 215, 245, 222, 200, 236, 201, 253, 236, 200, 266, 290])
y2 = np.array([203, 236, 200, 236, 269, 216, 298, 333, 301, 349, 360, 368])
y3 = np.array([185, 205, 226, 199, 238, 200, 250, 209, 246, 219, 253, 288])
# 绘制图形
plt.stackplot(x, y1, y2, y3)
plt.show()

