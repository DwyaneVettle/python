# author by Michealzou@126.com
# 2022/11/16 11:18
"""
    形参传递
"""
# 当实参传递个数不确定，那么形参就用星号元组的方式接收
def fun01(*args):
    print(args)

fun01(1)  # (1,)
fun01(1, 2)
fun01(1, 2, 3)
print("------")
# 如果要使用*元组+关键字参数的方式接收实参
# 需要指定实参的关键字(最后一个)
def fun02(a, *args, b):
    print(a)
    print(b)
    print(args)

fun02(100, 200, 300, 400, b=500)


# 字典实参-**拆分实参，结果是一个字典
def fun03(**args):
    print(args)

fun03(a=1, b=2)