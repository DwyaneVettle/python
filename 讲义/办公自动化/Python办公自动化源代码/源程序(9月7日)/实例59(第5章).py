import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
np.random.seed(19680801)
n_bins=10
x=np.random.randn(1000,3)

fig=plt.figure()
ax=fig.add_subplot(111)

colors=['red','tan','lime']
ax.hist(x,n_bins,density=True,histtype='bar',color=colors,label=colors)
ax.legend(prop={'size':10})
ax.set_title('直方图')

fig.tight_layout()

plt.show()










