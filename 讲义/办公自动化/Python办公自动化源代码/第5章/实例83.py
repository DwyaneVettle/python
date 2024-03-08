import numpy as np
a=np.matrix('1.0 2.0;3.0,4.0')
print(a)
print("===========")
print(a.T)               	#转置矩阵
print("===========")
b=np.matrix('5.0,7.0')
print(b)
print("===========")
c=b.T                  	#转置矩阵
print(c)
print("===========")
print(a*c)              	#矩阵乘法
print("===========")
print(a.I)              	#逆矩阵
