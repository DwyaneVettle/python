import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

plt.figure()                          	#创建对象
x=np.arange(0.0,4.0,0.1)
y=np.sin(np.pi*x)
plt.plot(x,y,'r--*',label='正弦曲线')  		#红色、虚线、星形

plt.legend()                         	#显示图标
plt.xlabel('时间')                     	#设置x轴的标签
plt.ylabel('电流')                     	#设置y轴的标签
plt.title('正弦曲线')                  	#设置标题
plt.grid(True)                       	#显示网格

plt.show()
