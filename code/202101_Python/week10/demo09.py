# author by Michealzou@126.com
# 2022/11/9 11:15
"""
    练习：定义函数，用户输入两个数，求这两个数之和
"""
def sum(num01,num02):
    """
    求两数之和
    :param num01: 数字1
    :param num02: 数字2
    :return: 两数相加
    """
    return num01 + num02

num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
re = sum(num1, num2)
print(re)