import numpy as np
import matplotlib.pyplot as plt

data = np.array([1, 2, 3, 4, 5])
flg = plt.figure()
ax = flg.add_subplot(111)
ax.plot(data)
plt.show()
