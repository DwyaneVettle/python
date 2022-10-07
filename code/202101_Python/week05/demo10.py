# author by Michealzou@126.com
# 2022/10/5 11:29
"""
条件的初始值
while 条件表达式:
    循环体
    变化条件
"""
# 0-9
# 1.定义条件初始值
num = 1
# 2.做条件判断
while num < 10:
    # 执行的循环体
    print(num)
    # 3.定义条件变换的规则
    num = num + 1


"""
    练习：0-4之间正整数的和
    1.定义初始化变量 i = 0 he = 0
    2.定义循环条件 <=4
    3.执行循环体 he = he + i / i = i + 1
    4.打印和he
"""
i = 0
he = 0
while i <= 4:
    he += i
    i += 1
    print(he)
