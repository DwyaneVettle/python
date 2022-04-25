# author by Michealzou@126.com
# 2022/4/25 15:09
# 打印直接三角形
# for i in range(1, 6):  # 控制行-5行
#     for j in range(i):
#         print("*", end = " ")
#     print()
def rectangle(r_count, c_count, char):
    """
    打印三角形
    :param r_count: 控制行的
    :param c_count: 控制列
    :param char: 打印三角形的字符
    :return:
    """
    for r in range(r_count, c_count):
        for c in range(r):
            print(char, end=" ")
        print()

rectangle(1,10,"%")
