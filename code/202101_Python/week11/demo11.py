# author by Michealzou@126.com
# 2022/11/16 11:41
"""
    递归函数：在函数内部调用自己的
    条件：
        1.边界条件
        2.功能
"""
# 求某个数的阶乘 10! = 10*9*8*7.....*1
def factoral(num):
    if num == 1:
        return 1
    else:
        return num*factoral(num-1)


print(factoral(10))
