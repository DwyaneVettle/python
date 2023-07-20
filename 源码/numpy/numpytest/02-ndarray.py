import numpy as np
# 1.第一种创建方式
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
# 2.第二种创建方式 arange(start, stop, step)
b = np.arange(1, 10)
print(b)
# 3.第三种创建方式 zeros dtype指定类型 int32指32位二进制整型
# 输出多少个数字
c = np.zeros(10, dtype='int32')
print(c, c.dtype)
# 4.第四种创建方式ones()-生成2行3列
d = np.ones((2, 3), dtype='float32')
print(d, d.shape, d.dtype)
