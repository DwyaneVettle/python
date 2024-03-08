import numpy as np
a=np.ones((2,3))
print(a)
print("===========")
b=a
b[1,2]=2
print(a)     #a已经随b的改变而改变
print("===========")
print(b)
