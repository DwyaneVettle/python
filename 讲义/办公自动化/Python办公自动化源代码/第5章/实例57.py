import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1)            			#控制产生的随机数的数值不变
x=np.arange(5)
y=np.random.randn(5)

fig,axes=plt.subplots()
axes.bar(x,y,color='red')                 	#绘图

axes.axhline(0,color='black',linewidth=3)   	#画线

plt.show()
