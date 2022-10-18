# author by Michealzou@126.com
# 2022/10/14 21:43
"""
    ndarray属性测试
    shape:维度
    dtype:类型
    size:大小
"""
import numpy as np

# 1.维度shape
a = np.arange(1, 9)
print(a, a.shape)  # [1 2 3 4 5 6 7 8] (8,)
a.shape = (2, 4)  # 维度变成2行4列
print(a, a.shape)  # [[1 2 3 4] [5 6 7 8]]  (2, 4)
print("----------")
# 2.dtype数据类型基础操作
print(a.dtype)  # int32-表示32位二进制数据
# a.dtype = 'float32'  # 强制转换为float32-错误的修改方式，因为flaot和Int表现方式不一样
# print(a, a.dtype)  # [7.0e-45 8.4e-45 9.8e-45 1.1e-44]] float32
b = a.astype('float32')  # 正确的转换方式，但必须声明新的变量
print(b, b.dtype)
print("----------")
# 3.size属性：表示元素个数，len()表示多少行
print(b, 'size:',b.size, 'length:', len(b))  # [5. 6. 7. 8.]] size: 8 length: 2
print("----------")
# 4.索引index
c = np.arange(1, 19)
c.shape = (3, 2, 3)
print(c, c.shape)
"""
运行结果：三维数组
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]

 [[13 14 15]
  [16 17 18]]] (3, 2, 3)
"""
# 根据索引拿数据可以先参考维度shape
# 拿第一页第二行第一列--4
print(c[0][1][0])  # 等效于print(c[0,1,0])
# 也可用三层for循环嵌套遍历
for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        for k in range(c.shape[0]):
            print(c[i, j, k])  # 1-18
