import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

plt.figure('正弦曲线')      #创建对象
t=np.arange(0.0,4.0,0.1)
s=np.sin(np.pi*t)
plt.plot(t,s,'g--o',label='sinx')
plt.legend()                #显示右上角标签
plt.xlabel('时间(s)')       #设置x轴的标签
plt.ylabel('电压(mV)')      #设置y轴的标签
plt.title('正弦曲线')
plt.grid(True)              #显示网格

plt.show()














