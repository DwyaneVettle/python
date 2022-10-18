# author by Michealzou@126.com
# 2022/10/12 11:09
"""
    99乘法表
        1.每一行的个数=列数
        外循环控制行，内循环控制列
        9,9
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, "*", j, "=", i*j,end="\t")
    print()

