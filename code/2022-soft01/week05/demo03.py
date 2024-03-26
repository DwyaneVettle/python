"""
    浅拷贝：复制一层变量，不会复制依赖的过程
    深拷贝：将依赖过程一并复制,copy()
    默认浅拷贝
    浅拷贝仍然指向同一个堆空间的地址，而深拷贝重新复制了一个堆中的内存
    重新指向
"""
list01 = [3, 4, 5]
list02 = list01
list01[0] = 6
print(list02)  # [6, 4, 5]
list03 = list01.copy()
list01[2] = 10
print(list03)  # [6, 4, 5]
# list01 = [6, 4, 10]

import copy
list04 = copy.deepcopy(list01)
list01[1] = 5
print(list04)  # [6, 4, 10]
