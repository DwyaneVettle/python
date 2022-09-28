# author by Michealzou@126.com
# 2022/9/28 9:13
"""
    数据类型的转换
    原因：客户传递的数据往往和服务器端的数据不匹配
    str()-->将其他类型数据转换成字符串类型
    int()-->将可转换成整型的数据转换成整型
    float()-->将可转换成浮点型的数据转换成浮点型
    bool()-->将数据转换成布尔型
"""
# str() -- 所有的数据类型都可以转换成字符串
a = 10
b = 99.99
c = True
d = None
e = "python"
f = str(a)
g = ["aa", "bb"]
print(type(f))  # <class 'str'>
print(type(str(b)))  # <class 'str'>
print(type(str(c)))  # <class 'str'>
print(type(str(d)))  # <class 'str'>
print(type(str(g)))  # <class 'str'>

# int()-将可转换的数据转换成整型
# 纯数字、浮点型、布尔型、整型才能用int()转换
a = 10
b = 99.99
c = True
d = None
e = "1100"
g = False
print(type(int(b)))  # 将浮点型数据转换成整型，去点小数点，只保留整数部分 <class 'int'>
print(int(c))  # 1 将浮点型数据转换成整型，True-1，False-0
print(int(g))  # 0
# print(int(None))  # TypeError
print(int(e))

# float()-把可转换的数据转换成浮点型
# 纯数字、浮点型、布尔型、整型才能用float()转换
a = 10
b = 99.99
c = True
d = None
e = "1100"
g = False
print(float(a))  # 10.0,整型数据转浮点型，就是在末尾加.0
print(float(c))  # 1.0,将True转换成1再加.0
# print(float(None))  # TypeError
print(float(e))  # 1100.0
print(float(g))  # 0.0

# bool()
# 测试对象的布尔值
print(bool(False))
print(bool(0), bool(0.0))
print(bool(None))
print(bool(''), bool(""))
print(bool([]))  # 空列表
print(bool(list()))  # 空列表
print(bool(()))  # 空元组
print(bool(tuple()))  # 空元组
print(bool({}))  # 空字典
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合
# 除以上布尔值为False，其他的都为True

# None
name = "吴林"
name = None
print(type(name))  # <class 'NoneType'>

sex = None  # 占位
sex = "boy"
