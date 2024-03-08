import numpy as np

c=np.arange(24).reshape(2,3,4)
print(c)
print("===========")
print(c[1,2,:])     #输出数组中第2个数组中的第3行
print("===========")
print(c[0,2,3])     #输出数组中第1个数组中第3行第4列的值
















