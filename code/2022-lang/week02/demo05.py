"""
    数据类型的转换
    str()-将其他类型的数据-->字符串
    int()-将其他类型的数据-->整型
    float()-将其他类型的数据-->浮点型
    bool()-将其他类型数据-->布尔型
"""
a = "100"
b = 100
c = 99.99
d = str(b)
e = str(c)
print(type(d), type(e))  # <class 'str'> <class 'str'>
print(int(a), int(c))  # 100 99 浮点型转整型，直接取整
# x = "100abc" print(int(x))  不是纯数字的字符串没办法转换成整型
print(float(a), float(b))  # 100.0 100.0

# 除了0和None之外，所有的数据转换为布尔类型都为True
print(bool(0))
print(bool(None))
print(bool("123"))
print(bool(1))
print(bool(1.1))
print(bool(-1.1))
print(bool(1234e+12))

"""
    None表示空值对象
    作用：1.在没有想好变量的值的时候用None占位
            2.解除变量和值的关系
"""
name = None
age = 18
age = None
print(id(None))

