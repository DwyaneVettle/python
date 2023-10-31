import numpy as np
import matplotlib.pyplot as plt
x1 = np.linspace(0, 2*np.pi, 400)
y1 = np.cos(x1**2)
x2 = np.linspace(0.01, 10, 100)
y2 = np.sin(x2)
ax_one = plt.subplot(221)
ax_one.plot(x1, y1)
# 共享子图ax_one和ax_two的x轴
ax_two = plt.subplot(224, sharex=ax_one)
ax_two.plot(x2, y2)

plt.show()
