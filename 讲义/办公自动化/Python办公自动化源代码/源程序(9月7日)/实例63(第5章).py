import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2*np.pi)
y=np.sin(x)
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(x,y)
ax.set_xlim([-2,8])
ax.set_ylim([-3,2])

plt.show()











