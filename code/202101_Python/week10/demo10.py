# author by Michealzou@126.com
# 2022/11/9 11:47
"""
定义计算四位整数，每位相加和的函数
1234 = 10
"""
# def sum(num):
#     # 拆分这个4位数
#
# num01 = int(input("请输入一个4位数："))
# sum(num01)

num = 1234
ge = num % 10
shi = num // 10 % 10
bai = num // 100 % 10
print(bai)