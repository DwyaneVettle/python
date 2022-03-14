# author Basui
# 2022/3/13 23:12
#1.打印水仙花数100-1000 及是各个位数之间相加等于本身 1*1*1+5*5*5+3*3*3=153
for a in range(100,1000):
    ge = a % 10
    shi = a // 10 % 10
    bai = a // 100
    if ge ** 3 + shi ** 3 + bai ** 3 == a:
        print(a)
