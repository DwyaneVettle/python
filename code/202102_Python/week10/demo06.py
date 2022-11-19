# author by Michealzou@126.com
# 2022/11/8 10:46
"""
    return:返回当前函数的值
    return返回结果，终端函数的执行
    return下的代码不会执行

    函数没有返回值时，会自动返回None
"""


def fun01():
    # print("fun01执行咯！")
    return "fun01执行咯！"
    print("hello")


re = fun01()
print(re)
fun01()
print("------")


def fun02(a):
    print("fun02执行咯！")


re = fun02(100)
print(re)  # None
