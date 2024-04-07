"""
    元组：不可变的序列容器
    1.创建元组： ()   tuple(可迭代对象)
    2.元组查找：  index(value,start,end) 在start-end之间查找value，返回当前元素
                 所在的下标
                 count(value)：返回value所出现的次数
    3.元组的索引和列表相同，也有反向的所有，从-1到-n
"""
tup01 = (1, 2, 3.2, True)
tup02 = tuple("python")
print(tup01, tup02)
print(type(tup01), type(tup02))  # <class 'tuple'> <class 'tuple'>
print(tup01.index(2, 0, 4))
print(tup01.count(2))
# 切片
print(tup02[0: 4: 1])
# 索引
print(tup02[-1])  # 反向
print(tup02[1])  # 正向
# 遍历
for i in tup02:
    print(i)
print("==========")
# 反向遍历，仍然从左至右遍历
for i in range(len(tup02)-1, -1, -1):
    print(tup02[i])
