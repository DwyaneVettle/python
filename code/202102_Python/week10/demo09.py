# author by Michealzou@126.com
# 2022/11/8 11:27
"""
    练习：
        用户输入一个4位数，定义函数求各个位置上数之和
        1234 = 1+2+3+4=10
"""
# num = "1234"
# print(int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]))
def each_unit_sum(num):
    ge = num % 10
    shi = num // 10 % 10
    bai = num // 100 % 10
    qian = num // 1000
    return ge + shi + bai + qian

num = int(input("请输入一个4位数："))
re = each_unit_sum(num)
print(re)
