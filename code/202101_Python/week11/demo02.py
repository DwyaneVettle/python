# author by Michealzou@126.com
# 2022/11/16 8:48
"""
    函数内存
    不可变类型的数据传参时，函数内部不会改变原有的值
    可变类型的数据传参时，函数内部的值会改变
    不可变类型：字符串、布尔、数值、None、元组、固定集合
    可变类型：字典、集合、列表
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
print(list01[0])  # 100


def fun03(a):
    a = 100


list01 = [1]
fun03(list01)
print(list01[0])  # 1
