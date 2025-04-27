"""
    continue:用于中断当前循环，继续下一次循环
    # for循环
    for...in...:
        ......
        if ...:
            continue
"""
# for i in range(0, 10):
#     # 当循环到3的时候跳出当前循环，继续下次循环
#     if i == 3:
#         continue
#     print(i)
# 练习：打印0-50所有5的倍数的数字
# for item in range(0, 51):
#     if item % 5 == 0:
#         print(item)
# 使用continue语句
for item in range(0, 51):
    if item % 5 != 0:
        continue
    print(item)
