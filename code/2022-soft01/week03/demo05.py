"""
    双分支：
        if 条件表达式:
            代码块1
        else:
            代码块2
"""
num = int(input("请输入一个数："))
if num % 2 == 0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")
