# author by Michealzou@126.com
# 2022/10/4 9:32
"""
    嵌套if表达式
    if 表达式1:
        if 表达式1-1：
            代码块1
        else:
            代码块2
    else:
        代码块3
    案例根据用户输入的数值判断是单数还是双数
    如果这个数同时能被4整除，那么输出你中奖了
"""
num = int(input("请输入一个数值："))
if num % 2 == 0:
    print("这个数是一个双数")
    if num % 4 == 0:
        print("你中奖了！")
    else:
        print("谢谢回顾！")
else:
    print("这个数是一个单数")
