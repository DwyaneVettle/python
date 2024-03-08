import numpy as np

c=np.arange(24).reshape(2,3,4)
print(c)
print("===========")
print(c[1,2,:])    	#输出数组中第2个数组（大数组中包含两个大小数组，下同）中的第3行
print("===========")
print(c[0,2,3])    	#输出数组中第1个数组中的第3行第4列
