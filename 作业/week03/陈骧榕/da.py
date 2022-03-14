# cxr
# 2022/3/14 12:16
num = 1000    # 范围
for i in range(100, num):
    arr = str(i)
    res = 0
    for j in range(len(arr)):
        res += int(arr[j])**len(arr)
    if res == i:
        print(i)
