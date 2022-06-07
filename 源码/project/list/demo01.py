# author by Michealzou@126.com
# 2022/4/12 9:44
list01 = [800, 1000]
# 通过切片获取元素，会创建新列表.
list02 = list01[:]
list01[0] = 900
print(list02[0])  # 800
list01 = [500]
print(list02[0])  # 800

print("=====")
# 列表套列表
list01 = [800, [1000, 500]]
list02 = list01
list01[1][0] = 900
print(list01)
print(list02[1][0])  # 900

print("=====")
list01 = [800, [1000, 500]]
# 浅拷贝
# list02 = list01[:]
list02 = list01.copy()
list01[1][0] = 900
print(list02[1 ][0])  # ?900

print("=====")

import copy

list01 = [800, [1000, 500]]
# 深拷贝
list02 = copy.deepcopy(list01)
list01[1][0] = 900
print(list02[1][0])  # 1000
