# author by Michealzou@126.com
# 2022/9/13 10:34

"""
    对象是由标识、类型、值组成
    标识：唯一-id()--在内存中的地址
    类型：type()
    值：value()
"""

a = 10
b = "10"
a = 100

# 唯一的标识
print(id(a))
print(id(b))

# 类型
print(type(a))
print(type(b))

# 值
print(a)

class Student:
    def __init__(self):
        print(1)

c = Student()
print(type(c))

a = 100
a = "abc"

# 全大写的就是常量
MAX_SCORE = 100
MIN_SCORE = 0

