# author by Michealzou@126.com
# 2022/3/28 17:12
# 列表的排序
# 1.sort(),仍然是原列表
list01 = [33, 88, 22, 13, 9]
print(id(list01))
# list01.sort()
# print(list01)
list01.sort(reverse=True)
print(list01, id(list01))

# 2.sorted()，变成一个新的列表
list02 = [33, 88, 22, 13, 9]
list02_new = sorted(list02)
print(list02_new, id(list02_new), id(list02))