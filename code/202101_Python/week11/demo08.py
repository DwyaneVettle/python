# author by Michealzou@126.com
# 2022/11/16 11:37
"""
    定义一个数值相加的函数
    需求：数的个数不确定
"""
def add(*num):
    # result = 0
    # for i in num:
    #     result += i
    # return result
    return sum(num)



print(add(1, 2, 100, 5000, 10000))