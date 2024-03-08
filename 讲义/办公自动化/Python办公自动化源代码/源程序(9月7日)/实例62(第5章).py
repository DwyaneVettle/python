import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
ax=fig.add_subplot(111)

x=np.arange(-5,5,0.1)
y=np.arange(-5,5,0.1)
xx,yy=np.meshgrid(x,y,sparse=True)
z=np.sin(xx**2+yy**2)/(xx**2+yy**2)
ax.contour(x,y,z)

plt.show()











