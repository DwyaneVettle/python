import numpy as np

a=np.array([20,30,40,50])
b=np.arange(1,5)
print(a/b)             	#除运算
print("===========")  
c=np.arange(4)
print(c)
print("===========")
d=a-c                 	#减运算
print(d)
print("===========")
print(c**2)            	#乘方运算
print("===========")
e=np.array([[1,1],[0,1]])
print(e)
print("===========")
f=np.array([[2,0],[3,4]])
print(f)
print("===========")
print(e*f)            	#乘运算
print("===========")
print(e.sum())          	#求和
print("===========")
print(e.min())          	#求最小值 
print("===========")
print(e.max())          	#求最大值
