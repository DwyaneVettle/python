"""
    对象的布尔值：
        bool():任何对象都有自己的布尔值，可以通过该方法进行转换
        1. 对象的布尔值默认为True
        2. 如果对象的布尔值为False，则该对象为假对象
            常见的假对象：
                1. None
                2. False
                3. 0  0.0  布尔值转换为整型：0-False,1-True
                4. 空的容器：空字符串、空列表、空元组、空字典、空集合
"""
a = 1
print(type(a))
print(bool(a))  # True
print(bool(None))  # False
print(bool(False))  # False
print(bool(""))  # False
print(bool(list()))  # False
print(bool(tuple()))  # False
print(bool(dict()))  # False
print(bool(set()))  # False

if bool(""):
    print("hello")
