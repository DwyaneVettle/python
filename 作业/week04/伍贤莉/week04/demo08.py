# author by MiWuXianLi
# 2022/3/14 16:50
# continue :表示结束当前循环，但继续下一次的循环
# 列出1-100之间3的倍数的数字
for item in range(1, 101):
    if item % 3 != 0:
        continue
    print(item)