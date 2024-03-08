import numpy as np
a=[[1,0],[0,1]]
b=[[4,1],[2,2]]
print(np.matmul(a,b))   	#数组乘积
print("===========")
b=[1,2]
print(np.matmul(a,b))   	#二维和一维乘积
print("===========")
print(np.matmul(b,a))   	#一维和二维乘积  
print("===========")
a=np.arange(8).reshape(2,2,2)
b=np.arange(4).reshape(2,2)
print(a)
print("===========")
print(b)
print("===========")
print(np.matmul(a,b))   	#维度大于2的数组乘积
