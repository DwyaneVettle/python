import numpy as np
n=np.array([np.arange(3),np.arange(3),np.arange(3)]) #创建三维数组
print(n) 
print("===========")
n=np.array(np.arange(36))   	#创建一维数组
print(n.reshape(3,3,4))      	#对数组重新进行维度设置
