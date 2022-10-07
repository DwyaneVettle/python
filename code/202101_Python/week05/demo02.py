# author by Michealzou@126.com
# 2022/10/5 8:51
"""
    对象的布尔值：
        除了False、0、0.0、空字符串、空列表、空元组
        空字典、空集合、None的布尔值为False
        其他的都为True
        bool()
"""
print(bool(False))
print(bool(0),bool(0.0))
print(bool(''))
print(bool(None))
print(bool(1))
print(bool("aa"))
print(bool(2.12))