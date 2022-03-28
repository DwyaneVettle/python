# author by Michealzou@126.com
# 2022/3/28 15:11
# 列表的查询
list01 = ['p', 'y', 't', 'h', 'o', 'n']
# 1.获取单个元素-根据下标获取元素
print(list01[3])
print(list01[-1])
# 2.获取单个元素-根据元素获取下标：index()
print(list01.index('y'))
# 3.获取多个元素-切片
print(list01[1:4:1])
print(list01[1:6:2])
print(list01[1::])
print(list01[:2:])
print(list01[-3:-6:-1])