import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

data=[('苹果',2),('橘子',3),('桃子',1)]
fruit,value=zip(*data)

fig=plt.figure()
ax=fig.add_subplot(111)

x=np.arange(len(fruit))
ax.bar(x,value)
ax.set(xticks=x,xticklabels=fruit)

plt.show()
