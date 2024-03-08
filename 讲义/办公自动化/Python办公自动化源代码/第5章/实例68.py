import matplotlib.pyplot as plt

fig,ax=plt.subplots()
ax.plot([-2,2,3,4],[-10,20,25,5])

ax.spines['top'].set_visible(False)         	#上边界不可见
ax.spines['right'].set_visible(False)        	#右边界不可见

ax.spines['bottom'].set_position(('data',0))   	#移动x轴
ax.spines['left'].set_position(('data',0))      	#移动y轴

plt.show()
