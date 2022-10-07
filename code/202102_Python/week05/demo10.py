# author by Michealzou@126.com
# 2022/10/4 11:02
# 练习：计算6! 1*2*3*4*5*6
ji = 1
num = 1
while num <= 6:
    ji = ji * num
    num += 1
print(ji)

count = 6
res = 1
while True:
    res = res * count
    count -= 1
    if count == 1:
        break
print(res)
