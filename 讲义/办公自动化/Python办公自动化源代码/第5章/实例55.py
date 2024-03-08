import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,200)
mm={'mean':0.5*x*np.cos(2*x)+2.1*x}

fig,ax=plt.subplots()
ax.plot('mean',data=mm)  #绘制“中心线”

plt.show()
