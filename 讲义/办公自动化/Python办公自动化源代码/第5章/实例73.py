import matplotlib.pyplot as plt
import numpy as np  
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

x=range(0,30,1)
y=np.sin(x)

f,(ax1,ax2)=plt.subplots(2,1,sharex=True)  #接收返回的两个对象

ax1.plot(x,y)
ax1.set_title('共享x轴')
ax2.scatter(x,y)

plt.show()
