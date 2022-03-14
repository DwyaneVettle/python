# author by Michealzou@126.com
# 2022/3/7 15:22
# 数据类型的转换
a = 123
b = '123'
c = 100
d = 'hello123'
e = 100.61
# 1.将其他类型转换成字符串-str()
x = str(a)
print(type(x))  # <class 'str'>

# 2.将其他类型转换成整型-int()
y = int(b)
print(type(y))  # <class 'int'>
# z = int(d)
# print(z)
u = int(e)
print(u)  # 100
print(type(str(e)))  # <class 'str'>

# 3.将其他类型转换成浮点型-float()
w = float(a)
print(type(w))  # <class 'float'>
v = float(b)
print(type(v))  # <class 'float'>
# print(float(d))

# 4.将其他类型转换成布尔类型-bool()
f = False
print(int(f))
g = 0
print(bool(g))
h = 10
print(bool(h))
