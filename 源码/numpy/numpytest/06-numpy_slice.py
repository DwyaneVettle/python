import numpy as np

a = np.arange(1, 10)
# 一维数组
print(a)  # 1 2 3 4 5 6 7 8 9
print(a[:3])  # 1 2 3
print(a[3:6])  # 4 5 6
print(a[6:])  # 7 8 9
print(a[::-1])  # 9 8 7 6 5 4 3 2 1
print(a[:-4:-1])  # 9 8 7
print(a[-4:-7:-1])  # 6 5 4
print(a[-7::-1])  # 3 2 1
print(a[::])  # 1 2 3 4 5 6 7 8 9
print(a[:])  # 1 2 3 4 5 6 7 8 9
print(a[::3])  # 1 4 7
print(a[1::3])  # 2 5 8
print(a[2::3])  # 3 6 9

# 二维数组
a.resize(3, 3)
print(a)
"""
    切前两行前两列
    [[1 2]
     [4 5]]
"""
print(a[:2, :2])
"""
    一三两行
 [[1 2 3]
 [7 8 9]]   
"""
print(a[::2, :])

print('+' * 8)
a = np.arange(1, 10)
mask = [True, False, True, False, True, False, True, False, True]
print(a[mask])

print('+' * 8)
# 1-100中既是3也是7的倍数
a = np.arange(1, 100)
mask = (a % 3 == 0) & (a % 7 == 0)
print(a[mask])

# 基于索引的掩码
names = np.array(['Chuizi', 'Huawei', 'Oppo', 'Xiaomi', 'Vivo'])
rank = [1, 3, 4, 2, 0]
print(names[rank])
