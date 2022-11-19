# author by Michealzou@126.com
# 2022/11/9 11:01
"""
    返回值
    :return 返回值
    将函数的结果返回给用户
    return表示把结果返回了出去，它后面的代码不会被执行
"""
def fun01():
    """
    练习返回值
    :return:
    """
    print(1+1)
    return 20
    # print("python")
re = fun01()
print(re)

# 当函数没有返回值的时候，仍然用返回变量接收，那么得到的结果是None
def fun02():
    print(1+1)

re = fun02()
print(re)  # None
