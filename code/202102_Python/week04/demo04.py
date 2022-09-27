# author by Michealzou@126.com
# 2022/9/27 9:54
# 运算符
# //整除：表示只取整数部分
a = 100
b = 3
print(a / b)  # 33.333333333333336
print(a // b)  # 33
# **幂运算符
print(10**3)  # 1000
# %取余
print(a % b)  # 1

# 参数赋值 += -= /= *= %= --> a+=b -> a = a + b
c = 10
d = 20
c += d
print(c)
x = 100
y = 10
# x = x -y
x -= y
print(x)  # 90
print("-----------")
x = y = z = 10
print(id(x))
print(id(y))
print(id(z))
print("-----------")
# 比较运算符 < > <= >= != 返回的是一个boolean
# == 比较的是两个的值是否相等
# is、 is not 判断的id值
a = 10
b = 20
c = 10
print(a > b)  # False
print(a == c)  # True
print(a is b)  # False
print(a is not c)  # False

"""
    is is not 和 == !=的区别
    is ,is not比较的是对象内存的引用 ——>  id值 
    ==,!=比较的是对象的值
    如果比较的是不可变的类型（数字、字符串、元组），is和==是没有区别的
    如果比较的是可变类型（列表、字典、集合），就有区别
    is在一般时候比==的效率要高一些，在变量和None比较时，一般用is,is not
"""
a = 10
b = 10
print(a is b, a == b)  # True True

c = ["aa", "bb"]
d = ["aa", "bb"]
print(c is d, c == d)  # False True

print("-----------")
"""
    布尔运算符 and or not
    and 都为true时才为true
    or 只要有一个为true，结果为true
    not 取反都为true时结果为false, 都为false时结果为true
"""
a, b = 1, 2
print(a == 1 and b == 2)  # True
print(a == 2 and b == 2)  # False
print(a == 2 and b == 1)  # False

print(a == 1 or b == 2)  # True
print(a == 2 or b == 2)  # True
print(a == 2 or b == 1)  # False

f01 = True
print(not f01)  # False


"""
    位运算符
    & 对应位上都为1才是1，否则为0
    | 对应位上都为0才为0，否则为1
    >> 除以2
    << 乘以2
"""
a, b = 4, 8
print(a & b)  # 0
print(a | b)  # 12
print(a >> 1)  # 2
print(a << 1)  # 8
c = -4
print(c >> 1)
print(c << 1)