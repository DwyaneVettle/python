"""
    数据类型的转换
        1.str()-将其他数据类型转换为字符串
        2.int()-将其他数据类型转换为整型，包含中文、字母等字符不能转换
        3.float()-将其他数据类型转换为浮点类型，包含中文、字母等字符不能转换
                    整型转浮点型，在后面自动.0
        4.bool()-将其他数据类型转换为布尔类型
"""

a = 100
b = 99.99
c = True
d = "hello"
e = "101"
f = "122abc"
# 1.str()-将其他数据类型转换为字符串
str01 = str(a)
str02 = str(b)
str03 = str(c)
print(str01, type(str01))
print(str02, type(str02))
print(str03, type(str03))
print("=============")
#  2.int()-将其他数据类型转换为整型
i01 = int(b)
i02 = int(c)
# i03 = int(d)
print(i01, type(i01))
print(i02, type(i02))
# print(i03, type(i03)) ValueError
print("=============")
# 3.float()-将其他数据类型转换为浮点类型
f01 = float(a)
f02 = float(c)
# f03 = float(d)
# f04 = float(e)
# f05 = float(f)
print(f01, type(f01))
print(f02, type(f02))
# print(f03, type(f03))  ValueError
# print(f04, type(f04))
print("=============")
# print(f05, type(f05))

print("=============")
# 4.bool()-将其他数据类型转换为布尔类型
# 只有None、0、空的列表/元组/字典/集合、空字符串、Flase、空格会转换为Flase,其他都为True
b01 = bool(0)
b02 = bool([])
b03 = bool("")
print(b01, type(b01))
print(b02, type(b02))
print(b03, type(b03))