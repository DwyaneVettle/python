# author by Michealzou@126.com
# 2022/10/12 10:35
"""
    输出3行4列的矩形 *
    for i in ..:
        for j in ...:
    外循环控制行，内循环控制列
"""
for i in range(1, 10):  # 行
    for j in range(1, i + 1):
        # print()方法默认换行
        # end="",\n--表示换行（默认）,\t--tab不换行
        print("*", end="\t")
    print(end="\n")
