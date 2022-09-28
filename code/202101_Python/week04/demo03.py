# author by Michealzou@126.com
# 2022/9/28 10:01
"""
    input()表示接收用户输入的值，并可以保存到变量中，以方便下一步使用
    print()-输出
    input()接收到的值属于字符串类型，如果要做运算，必须转换成需要的类型
"""
# name = input("请输入您的姓名：")
# print("我的姓名是：" + name)

"""
    练习:接收用户的输入的两个数字，然后用这两个数字做加法运算
"""
from decimal import Decimal
num01 = float(input("请输入数字1："))
num02 = float(input("请输入数字2："))
print(Decimal(str(num01)) + Decimal(str(num02)))



