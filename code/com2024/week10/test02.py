"""
    元组：
    特点：1.一旦创建不可修改和增加、删除-不可变的序列
        2.元组中只有一个元素，那么需要在这个元素后加上逗号
        3.元组可以存储任意数据类型
        4.元组中元素也有对应的索引，从0开始到n-1结束
    1.创建：
        1.1.使用小括号的方式 ()
        1.2.使用内置函数tuple()
"""
# 创建空元组-没有意义
tuple01 = ()
tuple02 = tuple()
print(tuple01, type(tuple01))  # <class 'tuple'>
tuple03 = (10, 20 ,30)
tuple04 = ('python')
print(type(tuple04))  # <class 'str'>
tuple05 = ('python',)
print(type(tuple05)) # <class 'tuple'>
tuple06 = ('python', 20, 99.99, True)
print(tuple06, type(tuple06))  # ('python', 20, 99.99, True) <class 'tuple'>
tuple07 = tuple([10, 20, 30])
print(tuple07)

# 元组元素的获取-索引、切片
tuple06 = ('python', 20, 99.99, True)
print(tuple06[0])
tuple08 = tuple06[1: 3: 1]
print(tuple08)  # (20, 99.99)
# 元素的遍历
for item in tuple06:
    print(item)

# 应用场景
# 1.交换变量
a = 10
b = 20
a, b = (b, a)
print(a, b)  # 20 10