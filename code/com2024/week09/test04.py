"""
浅拷贝：复制过程中，只复制一层变量， 不会深层变量绑定的对象的复制过程；
深拷贝：复制整个依赖过程。
python中默认为浅拷贝，因为深拷贝更耗内存
"""
list01 = ["张无忌","赵敏"]
list02 = list01
# 修改的是列表第一个元素
list01[0] = "无忌"
print(list02[0])  # 无忌

list01 = ["张无忌","赵敏"]
list02 = list01
# 修改的是list01变量
list01 = ["无忌"]
print(list02[0])#张无忌

list01 = [800,1000]
# 通过切片获取元素，会创建新列表.
list02 = list01[:]
list01[0] = 900
print(list02[0])#?800
list01 = [500]
print(list02[0])#?800

# 列表套列表
list01 = [800,[1000,500]]
list02 = list01
list01[1][0] = 900
print(list02[1][0])#?900


list01 = [800,[1000,500]]
# 浅拷贝
# list02 = list01[:]
list02 = list01.copy()
list01[1][0] = 900
print(list02[1][0])#?900


import copy

list01 = [800,[1000,500]]
# 深拷贝
list02 =copy.deepcopy(list01)
list01[1][0] = 900
print(list02[1][0])#?1000