import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,200)
data={'x':x,'y1':2*x+1,'y2':3*x+1.2,'mean':0.5*x*np.cos(2*x)+2.5*x+1.1}

fig,ax=plt.subplots()
ax.plot('x','mean',color='black',data=data)  #绘制“中心线”

plt.show()







