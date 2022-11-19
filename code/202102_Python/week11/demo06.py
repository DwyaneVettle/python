# author by Michealzou@126.com
# 2022/11/15 10:33
def fun01(a=0, b=0, c=0, d=0):
    print(a)
    print(b)
    print(c)
    print(d)


# 如果参数个数不匹配，那么会报错
# fun01(1, 2)
# 如果参数实际情况就是不匹配，使用形参默认值，用关键字传递实参
# 缺省参数
# fun01(b = 1,  c = 2)

# 当实参个数不确定的时候，采用星号元组拆分法
# def fun02(*args):
#     print(args)
#
# fun02(1)  # (1,)
# fun02(1, 2)  # (1, 2)
# fun02(1, 2, 3)  # (1, 2, 3)

# 当时使用星号元素拆分实参配合关键字实参使用时，一定要注明关键字是谁
# def fun03(a, *args, b):
#     print(a)
#     print(args)
#     print(b)
#
# fun03(1, 2, 3, 4, 5, b = 6)

# **字典参数的传递，拆分出的值是一个字典
def fun04(**args):
    print(args)


fun04(a=1, b=2)
