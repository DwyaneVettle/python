# author by Michealzou@126.com
# 2022/11/15 11:13
"""
    递归函数：函数处理问题的同时，在函数内部调用自己
    作用：减少代码量，将复杂的问题简单化
    两个点：1.边界条件，如果没有=死循环
            2.处理什么问题
    求100阶乘
    1*2*3*4*。。。*100
    num*num-1
    num-1*num-2
"""
def factorial(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return num*factorial(num-1)

print(factorial(10))
