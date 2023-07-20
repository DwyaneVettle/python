import numpy as np
a = np.arange(1, 10)
print(a, a.dtype)  # [1 2 3 4 5 6 7 8 9] int32

# 1.视图变维
b = a.reshape(3, 3)
print(a, '-> a')
print(b, '-> b')
"""
    [[1 2 3]
     [4 5 6]
     [7 8 9]] -> b
"""
print('=' * 8)
# 抻平数组
print(b.ravel())  # [1 2 3 4 5 6 7 8 9]

# 2.复制变维
c = b.flatten()
print(c, '->c')  # [1 2 3 4 5 6 7 8 9]
print('=' * 8)

# 3.就地变维
c.shape = (3, 3)
print(c, '->c')
"""
    [[1 2 3]
     [4 5 6]
     [7 8 9]] ->c
"""
c.resize((9,))
print(c, '->c')  # [1 2 3 4 5 6 7 8 9] ->c
