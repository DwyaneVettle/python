# author by Michealzou@126.com
# 2022/10/4 11:41
"""
案例：打印100-1000的水仙花数
    花 = ge**3 + shi ** 3 + bai ** 3
    153  3 -> 153 % 10
        5  ->  153 // 10 % 10
        1 -> 153 // 100
"""
for item in range(100, 1000):
    # print(item)
    # 提取个十百位上的数字
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    if ge ** 3 + shi ** 3 + bai ** 3 == item:
        print(item)
