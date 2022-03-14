# author by Michealzou@126.com
# 2022/2/28 16:32
# 数据类型-整型int
from decimal import Decimal
a = 10
b = -10
c = 0
print(a, type(a))  # <class 'int'>
print(b, type(b))  # -10 <class 'int'>
print(c, type(c))  # 0 <class 'int'>
print("十进制", 999)
print("二进制", 0b110101110)
print("八进制", 0o776)
print("十六进制", 0x7E)

print("-------------------")
# 数据类型-浮点型
x = 3.1415
print(x, type(x))  # 3.1415 <class 'float'>
y = 100.0
print(y, type(y))  # 100.0 <class 'float'>
# 浮点型的数据会丢失精度，所以一般不做运算
print(1.1 + 2.2)
print(2.2 + 1.1)  # 3.3000000000000003
print(Decimal("2.2") + Decimal("1.1"))

print("----------------------")
# 数据类型-布尔型：True=1 False=0
b1 = True
b2 = False
print(b1, type(b1))  # True <class 'bool'>
print(b2, type(b2))  # False <class 'bool'>
print(1 != 1)  # False
print(1 == 1)  # True
print(True + 1)
print(False + 1)

print("--------------------")
# 数据类型-字符串str
# 三引号的字符串是可以换行的
str1 = '人生苦短，快学python'
str2 = "python好学，人生苦短"
str3 = """我是Python程序员
            我是java程序员"""
print(str1, type(str1))  # 人生苦短，快学python <class 'str'>
print(str2, type(str2))
print(str3, type(str3))
