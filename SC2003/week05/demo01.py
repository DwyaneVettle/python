# author by Michealzou@126.com
# 2022/3/21 14:04
# 求100以内的偶数之和
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
print(sum)

sum01 = 0
for j in range(1, 101):
    if j % 2 == 0:
        sum01 = sum01 + j
print(sum01)
# 打印99乘法表
for a in range(1, 10):
    for b in range(1, a + 1):
        print(f"{a} * {b} = {a*b}",end=" ")
    print()
