import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(1)
ax1=plt.subplot(111)
ax2=ax1.twinx()

ax1.plot(np.arange(1,5),'g--')
ax1.set_ylabel('ax1',color='r')
ax2.plot(np.arange(7,10),'b-')
ax2.set_ylabel('ax2',color='b')

plt.show()
