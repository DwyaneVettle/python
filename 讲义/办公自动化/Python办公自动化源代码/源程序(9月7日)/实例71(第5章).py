import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

x1=np.linspace(0.0,5.0)   #生成一维数组
x2=np.linspace(0.0,2.0)

y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(2*np.pi*x2)

plt.subplot(2,2,1)      #subplot为2*1的样式,同时在第1个子图上画出
plt.plot(x1,y1,'yo-')
plt.title('图表1')
plt.ylabel('阻尼振荡')

plt.subplot(2,2,2)      #第2个子图加个空图
plt.title('空图')

plt.subplot(2,2,4)
plt.plot(x2,y2,'g.-')
plt.xlabel('时间(s)')
plt.ylabel('无阻尼')

plt.show()















