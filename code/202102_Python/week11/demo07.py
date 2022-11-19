# author by Michealzou@126.com
# 2022/11/15 10:50
"""
    练习：数值相加的函数练习
        数值个数不定
"""
def sum01(*args):
    # 求和的初始化变量
    # result = 0
    # for i in args:
    #     result += i
    # return result
    return sum(args)

print(sum01(1, 2, 3, 4, 5, 6, 22, 34))
