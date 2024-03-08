import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1)
x=np.arange(5)
y=np.random.randn(5)

fig,axes=plt.subplots(ncols=2,figsize=plt.figaspect(1./2))

vert_bars=axes[0].bar(x,y,color='red',align='center')   #绘图
horiz_bars=axes[1].barh(x,y,color='blue',align='center')#绘图

axes[0].axhline(0,color='black',linewidth=3)            #画线
axes[1].axvline(0,color='black',linewidth=3)            #画线 

plt.show()








