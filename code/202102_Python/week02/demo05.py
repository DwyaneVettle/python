# author by Michealzou@126.com
# 2022/9/13 11:18
# 变量  变量名 = value

a = 100
print(a)

# del 删除对象地址空间的引用
del a
# print(id(a))  # name 'a' is not defined

# 链式赋值
# b = 10
# c = 10

b = c = 10
print(b)
print(c)

# 系列解包赋值
x, y, z = 10, 30, 20
print(x)
print(y)
print(z)

e, f = 10, 20
f, e = e, f
print(e)
