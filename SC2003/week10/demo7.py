# author by Michealzou@126.com
# 2022/4/25 16:13
# 形参传递
# 1.缺省参数-默认值传参
def fun01(a=0, b=0, c=0, d=0):
    print(a)
    print(b)
    print(c)
    print(d)


fun01(a=1, b=2)
fun01(c=100, a=100)


# 2.元组传参,用*表示动态形参
def fun02(*args):
    print(args)


fun02(1, 2, 3, 4, 5, 6, 7, 8, 89, 9, 67, 46, 4, 6345, 3, 53)


def fun03(a, *args, b):
    print(a)
    print("=====")
    print(args)
    print("=====")
    print(b)


fun03(1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, b=9)


# 4.字典传参
def fun04(**a):
    print(a)

fun04(a=1,b=2,c=3)