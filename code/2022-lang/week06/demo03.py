"""
    浅拷贝：拷贝对象一层
    深拷贝：拷贝整个复制过程
"""
# 导包
import copy
list01 = ["python", "java", "c++", "javascript"]
list02 = list01
print(list02)  # ['python', 'java', 'c++', 'javascript']
print(id(list01), id(list02))
print(type(list01), type(list02))
print("========")
list03 = list01.copy()
print(list03)  # ['python', 'java', 'c++', 'javascript']
print(id(list01), id(list03))
list03[0] = "java"
print(list01)

list04 = copy.deepcopy(list01)
print(id(list04), id(list01))
list04[0] = "java"
print(list01)
