# author by Michealzou@126.com
# 2022/10/13 21:51
"""
    ndarray的API
"""
import numpy as np
# 1.第一种创建方式
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
# 2.第二种创建方式 arange(start, stop, step)
b = np.arange(1, 10)
print(b)
# 3.第三种创建方式 zeros dtype指定类型 int32指整型
c = np.zeros(10, dtype='int32')
print(c, c.dtype)
# 4.第四种创建方式ones()
d = np.ones((2, 3), dtype='float32')
print(d, d.shape, d.dtype)
"""
    运行结果
        [1 2 3 4 5 6]
        [1 2 3 4 5 6 7 8 9]
        [0 0 0 0 0 0 0 0 0 0] int32
        [[1. 1. 1.]
         [1. 1. 1.]] (2, 3) float32
"""
# 测试5个1/5
print(np.ones(5) / 5)  # [0.2 0.2 0.2 0.2 0.2]

"""
    扩展
        np.zeros_like()  维度像xxx
        np.ones_like()   
"""
print(np.zeros_like(a))
