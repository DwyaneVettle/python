# author by Michealzou@126.com
# 2022/8/5 11:55
# 6.6.
"""
使用while循环打印九九乘法表
"""
row = 1
while row <= 9:  # 行数
    col = 1

# ********** Begin *********

    while col <= row:  # 控制列()
        print("{}*{}={}".format(col, row, row*col), end="\t")
        col += 1

# ********** End *********
    print()
    row += 1