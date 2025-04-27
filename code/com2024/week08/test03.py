"""
    列表的创建：
        1. 直接使用方括号[] list01 = [ele01, ele02, ...]
        2.内置函数list(可迭代对象)
    列表的类型：<class 'list'>
"""
# 1.第一种方式[]
list01 = ["python", 123, 99.9, True]
list02 = [123, "python",  99.9, True]
print(id(list01), type(list01))  # 1959213334272
print(id(list02))  # 1727750045184
print(list01)
list02 = []
print(list02)
# 2.第二种list()
list03 = list("python")
print(list03)
list04 = list()
print(list04)
