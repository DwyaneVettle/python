# author by Michealzou@126.com
# 2022/11/8 11:14
"""
    定义函数，用户输入两个数，求两数之和
"""


# def two_num_sum():
#     num01 = int(input("请输入num01:"))
#     num02 = int(input("请输入num02:"))
#     print(num01 + num02)
#
# two_num_sum()

def two_num_sum(num01, num02):
    return num01 + num02


num01 = int(input("请输入num01:"))
num02 = int(input("请输入num02:"))
re = two_num_sum(num01, num02)
print(re)
