import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

fig,ax=plt.subplots()
ax.plot([1,2,3,4],[10,20,25,30],label='新疆')
ax.plot([1,2,3,4],[30,23,13,4],label='上海')
ax.scatter([1,2,3,4],[20,10,30,15],label='时间')
ax.set(ylabel='温度',xlabel='时间',title='对比图')
ax.legend(loc=3)       #设置图例在左下角

plt.show()











