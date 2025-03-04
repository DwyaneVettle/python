"""
    python一切皆为对象，对象拥有三大特性：
    标识：表示对象唯一的id   id()
    类型：表示对象所属的类型  type()
    值：表示对象的所具有的值  value
    创建对象方式：
    Java：int a = 10;
    python: a = 10
"""
# 1.创建对象  对象名 = 值
a = 10
A = 100
b = 20
c = 30

# 2.获取标识id
print(id(a))  # 2612340785680
print(id(b))  # 2612340786000
print(id(c))  # 2612340786320

# 3.获取类型type
print(type(a))  # <class 'int'>
print(type(b))
print(type(c))

# 4.获取值value，直接输出对象名本身就可以得到它的值
print("a",a)
print("A",A)
print(b)
print(c)


# 命名规则
_a = 10


print(help())