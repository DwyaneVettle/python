# author by Michealzou@126.com
# 2022/10/5 9:31
"""
练习：
    接收用户输入的一个正整数
    判断这个数是双数还是单数
"""
# 1.接收用户输入的数据
num = int(input("请输入一个正整数："))
# 2.判断
if num % 2 != 0:
    print(f"{num}是一个单数")
else:
    print(f"{num}是一个双数")
