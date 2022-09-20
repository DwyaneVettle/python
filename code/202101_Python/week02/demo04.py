# author by Michealzou@126.com
# 2022/9/14 11:21

"""
    变量:
    命名：变量 = 表达式
    一个变量不再被引用的时候，就会被垃圾回收器回收
    也可以采用手动回收垃圾，del object
"""

a = "张无忌"
print(id(a))  # 2549813392944
print(type(a))  # <class 'str'>
print(a)  # 张无忌
del a
# print(a)


# 链式赋值
x = 100
y = 100
x = y = 100

# 系列解包赋值
a, b, c = 20, 10, 30
print(a)
print(b)
print(c)

# 交换两个变量的值
a, b = 100, 200
a, b = b, a
print(a)
print(b)
