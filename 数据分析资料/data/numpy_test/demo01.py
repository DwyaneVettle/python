# author by Michealzou@126.com
# 2022/10/13 21:04
"""
    测试numpy
"""
import numpy as np
ary = np.array([1, 2, 3, 4, 5, 6])
print(ary, type(ary))  # [1 2 3 4 5 6] <class 'numpy.ndarray'>
print(ary.shape)  # shape代表数组的维度 (6,)-元组，代表数组是一维数组，并有6个元素
# 修改维度，shape是属性可以访问，也可以修改
ary.shape = (2, 3)  # 改为2行3列
print(ary, ary.shape)  # [[1 2 3] [4 5 6]]  , (2, 3)
# 变回来
ary.shape = (6,)
# 数组的运算
print(ary)
print(ary * 3)  # 让数组每个元素*3 [ 3  6  9 12 15 18]
print(ary > 3)  # 让数组每个元素和3比较，返回布尔值 [False False False  True  True  True]
print(ary + ary)  # [ 2  4  6  8 10 12] 每个位上数相加
