import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

fig=plt.figure()                        #创建一个区域
ax=fig.add_axes([0.1,0.5,0.8,0.5])  #add_axes()新增子区域
ax.set_xlabel('X轴')                   #设置X轴
ax.set_ylabel('Y轴')                   #设置Y轴
line=ax.plot([0,5],[0,1])             #绘图

plt.show()







