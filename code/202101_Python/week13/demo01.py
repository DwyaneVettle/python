# author by Michealzou@126.com
# 2022/11/30 8:52
"""
    lambda args1,args2,args3.. : expression
    匿名函数：完成一个比较简单的功能
    返回指接收表达式结果
"""
# 需求：求两个数的乘积
# def mul(num1, num2):
#     return num1 * num2
#
#
# print(mul(10, 20))

ji = lambda num1, num2: num1 * num2
print(ji(10, 20))

# 练习：求两个数的最小值（匿名函数）
# def min01(num01, num02):
#     # if num01 > num02:
#     #     return num02
#     # else:
#     #     return num01
#     return min(num01, num02)
# min01(2, 3)
min02 = lambda num01, num02:  min(num01, num02)
print(min02(100,99))


