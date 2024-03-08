import numpy as np
a=np.array([[1,2],[3,4]])
b=np.linalg.inv(a)          	#计算a的逆矩阵
print(a)
print("===========")
print(b)
print("===========")
print(np.dot(a,b))          	#验证a的逆矩阵
