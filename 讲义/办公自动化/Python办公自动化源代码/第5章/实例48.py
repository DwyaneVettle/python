import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

fig=plt.figure()
ax=fig.add_subplot(111)
ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='标题',ylabel='y轴', xlabel='x轴')

plt.show()
