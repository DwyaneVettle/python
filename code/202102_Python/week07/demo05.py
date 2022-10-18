# author by Michealzou@126.com
# 2022/10/18 11:11
"""
    列表内存
"""
list01 = ["张无忌", "赵敏"]
list02 = list01
list01[0] = "无忌"
print(list01[0])  #无忌


list01 = ["张无忌", "赵敏"]
list02 = list01
list01 = ["无忌"]
print(list02[0])

list01 = [800, 1000]
list02 = list01[:]  # 创建新的列表
list01[0] = 900
print(list02[0])
list01 = [500]
print(list02[0])

list01 = [800, [1000, 500]]
list02 = list01
list01[1][0] = 900
print(list02[1][0])  # 900

# 浅拷贝：只复制一层对象
# copy()
list01 = [800, [1000, 500]]
list02 = list01.copy()
list01[1][0] = 900
print(list02[1][0])  # 900

import copy
# 深拷贝：复制整个依赖过程。
list01 = [800, [1000, 500]]
list02 =copy.deepcopy(list01)
list01[1][0] = 900
print(list02[1][0])  # 1000
