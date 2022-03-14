# peng xin wen
# 2022/3/13 23:04
#1.打印水仙花数100-1000 及是各个位数之间相加等于本身 1*1*1+5*5*5+3*3*3=153
def total(num):
    gw = num % 10
    sw = (num // 10) % 10
    bw = num // 100

    return gw ** 3 + sw **3 + bw **3

for i in range(100,1000):
    if i == total(i):
        print(i,'是水仙花数')