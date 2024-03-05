"""
    数据类型的转换：
        str()-将其他类型的数据转换为字符串类型
        float()-将其他类型的数据转换为浮点类型
        int()-将其他类型数据转换为整型
        以上三种可以互相转换
        bool()-将其他数据类型转换为布尔类型
            None、0(.0)-False,其他都为True
            None是一个空值对象
"""
name = "310"
num01 = 10000
f01 = 67.89
# str()
str01 = str(num01)
str02 = str(f01)
print(type(str01))
print(type(str02))

# int()
num02 = int(name)  # 如果字符串转整型，需要纯数字
num03 = int(f01)  # 浮点类型转整型，直接截取整数，丢弃小数部分
print(num02, num03)
print(type(num02), type(num03))

# float()
f02 = float(name)
f03 = float(num01)
print(f02, f03)
print(type(f02), type(f03))

# bool()
print(bool("a"))
print(bool(12))
print(bool(12.87))
print(bool(None))  # False
print(bool(0))  # False


"""
    None表示一个空值对象，表示接触对象和值的联系，或用于占位
    null
"""
city = None
position = None
name = "sccs"
name = None
print(name)  # None
