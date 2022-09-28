# author by Michealzou@126.com
# 2022/9/28 10:35
"""
    运算符
    1.算数运算符 +-*/ //整除 % **幂运算符
    2.赋值运算符 = += -= *= /=
    3.比较运算符 > < >= <=
    4.布尔运算符 and or not
    5.位运算符 >> << & |
    6.运算符的优先级
"""
# 算数运算符
a = 100
b = 3
print(a // b)  # 33,整除只取整数，不管小数点后面的数
print(a**b)  # 1000000
print(a % b)  # 1

# 赋值运算符
a = b = c = 10
print(id(a))
print(id(b))
print(id(c))
# 参数赋值 += -= *= /=
a = 100
a += 10  # a = a+10
print(a)

print("-----------")
# 比较运算符 -结果都为布尔型 ==比较的是value，is， is not比较是id
"""
    is,is not比较的是内存地址
    == 比较的对象的值
    不可变类型（字符串、数值、元素）--> is和==是没有区别的
    可变类型（列表、集合、字典）--> 有区别
    is比==的效率高，在变量和None比较时，建议用is
"""
a = 10
b = 10
print(a == b)  # True
print(a is b)  # True

c = ["aa", "bb"]
d = ["aa", "bb"]
print(c == d, c is d)  # True False
print("-----------")
# 布尔运算符 and or not
"""
    and 当两个都为True,结果为True
    or 当有一个为True，结果就为True
    not 全为True，结果为False，反之，结果为True
"""
# and
a, b = 1, 2
print(a == 1 and b == 2)  # True
print(a == 2 and b == 2)  # False
print(a == 2 and b == 1)  # False
# or
print(a == 1 or b == 2)  # True
print(a == 2 or b == 2)  # True
print(a == 2 or b == 1)  # False
print("-------")
# not
print(not b == 2)  # False
print(not b == 1)  # True

"""
    位运算符
    & 对应位上都为1才为1，否则为0
    | 对应位上都为0才为0，否则为1
    >> 除以2
    << 乘以2
"""
a, b = 4, 8
print(a & b)  # 0
print(a | b)  # 12
print(a >> 1)  # 2
print(a << 1)  # 8
