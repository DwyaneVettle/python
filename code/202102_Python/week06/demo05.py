# author by Michealzou@126.com
# 2022/10/11 10:40
# 双重循环，当内循环为偶数的时候配合break或continue终端程序
for i in range(1, 4):
    for j in range(1, 11):
        # print(j)
        if j % 2 == 0:
            # break
            continue
        print(j)

