# author by MiWuXianLi
# 2022/3/14 16:17
# 嵌套循环-打印直角三角形*
"""
语法：for i in 对象：-控制行
        for j in 对象：-控制列
             代码块
"""
for i in range(0,5): # 控制行-5行
    for j in range(i):
        print("*", end="")
    print()

# while循环
item = 1
while item <= 5:
    jtem = 1
    while jtem <= item:
        print("* ",end=" ")
        jtem += 1
    print(end="\n")
    item = item + 1