# author by Michealzou@126.com
# 2022/2/28 15:28
# 变量 命名：变量名=变量值
computer = "hp"
# print(computer)
# 使用变量必须先初始化
car = ""
# 删除变量： del 变量名
# del删除的是变量所引用的值，而不是变量名。删除了值之后，变量就没有引用，就会被垃圾回收器回收
del computer
# print(computer)  # NameError
# 链式赋值、系列解包赋值
# a = 100
# b = 100
a = b = 100
print(a)
print(b)
x, y, z = 10, 20, 30
print(x)
print(y)
print(z)
# 两个变量的值交换
d, e = 100, 200
d, e = e, d
print(d)
print(e)

print("------------------------------------")
# 常量：Python中不支持常量，但是没有语法限制不可以创建常量，常量名字母全部大写
MAX_SCORE = 100
print(MAX_SCORE)
# 修改常量的值是可以的，但不推荐。一般情况下常量一旦赋值就不能更改
MAX_SCORE = 150
print(MAX_SCORE)

