# 2022/3/12 17:47
# 打印水仙花数
# 一个 n 位数，每个位上的数字的 n 次幂之和等于它本身 n>= 3
num = 1000    # 范围
for i in range(100, num):
    arr = str(i)
    res = 0
    for j in range(len(arr)):
        res += int(arr[j])**len(arr)
    if res == i:
        print(i)