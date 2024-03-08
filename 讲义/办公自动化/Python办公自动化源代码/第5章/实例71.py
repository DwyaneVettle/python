import matplotlib.pyplot as plt
import numpy as np

plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.5, hspace=0.5)
x=np.arange(0.1,4.0,0.1)
y1=x**2
y2=x**(1/2)
y3=x**(-1)
y4=x**(3)

plt.subplot(221)
plt.plot(x,y1,'r')   	#红色
plt.subplot(222)
plt.plot(x,y2,'b')   	#蓝色
plt.subplot(223)
plt.plot(x,y3,'y')   	#黄色
plt.subplot(224)
plt.plot(x,y4,'k')   	#黑色

plt.show()
