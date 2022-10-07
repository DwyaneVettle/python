# author by Michealzou@126.com
# 2022/10/4 8:51
"""
    条件判断双分支：如果... 不满足...就....
    if 条件表达式1:
        代码块1
    else:
        代码块2
"""
# 案例：根据用户输入的数值判断是单数还是双数
# input()接收到的是一个字符串
num = input("请输入一个数值：")
num01 = int(num)
if num01 % 2 == 0:
    print(f"{num}是一个双数")
else:
    print(f"{num}是一个单数")
