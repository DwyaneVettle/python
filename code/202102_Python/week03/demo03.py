"""
    数据类型的转换
    str()-将给定数据转换成字符串
    int()-将给定的数据转换成整型
    float()-将给定的数据转换成浮点型
    bool()-将给定数据转换成布尔型，除0以外其他的对象都是True
"""
str01 = "10"
str02 = "100.01"
num01 = 10
f01 = 10.5
# 将str01转换成整型
num02 = int(str01)
print(type(num02))  # <class 'int'>
# 将str02转换成浮点型
f02 = float(str02)
print(type(f02))  # <class 'float'>

# 将num01转换成字符串
num03 = str(num01)
print(type(num03))  # <class 'str'>

# f01-str
f03 = str(f01)
print(type(f03))  # <class 'str'>

# num01-float
print(type(float(num01)))  # <class 'float'>
print(float(num01))

# f01-int
print(type(int(f01)))  # <class 'int'>
print(int(f01))

# bool() - 1,0
a = 1
b = bool(a)
print(b)  # True
print(type(b))  # <class 'bool'>

c = 0
print(bool(c))  # False
d = 3
print(bool(d))  # True

