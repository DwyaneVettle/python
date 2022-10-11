# author by Michealzou@126.com
# 2022/10/11 10:03
"""
    输出3行4列的矩阵
    *
    for i in ..:行
        for j in .. : 列
"""
for i in range(1, 4):  # 控制行3
    for j in range(1, 5):
        # end = ''在print()语句里使用,常用参数\t(不换行),\n(默认换行)
        print('*', end='\t')
    print()
