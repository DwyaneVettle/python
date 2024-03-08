import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
np.random.seed(1)             	#控制产生的随机数的数值不变
y=10
x=np.random.randn(1000,3)     	#产生1000×3维数组

fig=plt.figure()
ax=fig.add_subplot(111)

colors=['red','tan','lime']
ax.hist(x,y,density=True,histtype='bar',color=colors,label=colors)
ax.legend(prop={'size':10})    	#加入图例
ax.set_title('直方图')         	#加入标题
plt.show()
