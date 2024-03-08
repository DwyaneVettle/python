import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,np.pi)
ysin=np.sin(x)
ycos=np.cos(x)

fig=plt.figure()
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)

ax1.plot(x,ysin)
ax2.plot(x,ysin,'-.',linewidth=2)
ax3.plot(x,ycos,color='blue',marker='<',linestyle='dashed')

plt.show()
