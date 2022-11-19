# author by Michealzou@126.com
# 2022/11/15 8:36
"""
    函数内存图
    不可变类型的数据传递参数时，不会改变实参的值
    可变类型的数据传递参数时，会改变原有的值
    不可变类型：
        整型、浮点型、字符串、布尔、元组
    可变：
        列表、字典、集合
"""


def fun01(a):
    a = 100


num01 = 1
fun01(num01)
print(num01)  # 1


def fun02(a):
    a[0] = 100


list01 = [1]
fun02(list01)
print(list01)  # [100]


def fun03(a):
    a = 100


list01 = [1]
fun03(list01)
print(list01[0])  # 1
