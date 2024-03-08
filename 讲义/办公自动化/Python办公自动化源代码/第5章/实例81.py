import numpy as np
a=np.ones((2,3))
print(a)
print("===========")
b=a.copy()
b[1,2]=2
print(a)     #a没有随着b的改变而改变
print("===========")
print(b)
