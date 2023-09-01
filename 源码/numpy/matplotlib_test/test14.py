import numpy as np
import matplotlib.pyplot as plt
num = 50
x = np.random.rand(num)
y = np.random.rand(num)
area = (30 * np.random.rand(num))**2
plt.scatter(x, y, s=area)
plt.show()
