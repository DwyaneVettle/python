"""
    比较运算符中 is (not) 比较两个对象的id是否相同
    != == 比较的是值是否相等

    布尔运算符
        and - 只有两个取值都为True，结果才为True
        or - 只要两边结果有一个为True，结果就为True
        not - 取反
"""
a = 10
b = 10
print(a is not b)
print(a == b)
c = 1000
d = 1000
print(c == d)
print(c is d)
print("========")
print(a == b and c == d)  # True
print(a == b and c != d)  # False
print(a == b or c != d)  # True
print(not a)  # False


