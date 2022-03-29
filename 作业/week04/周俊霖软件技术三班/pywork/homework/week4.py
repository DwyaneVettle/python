# author by aoman
# 2022/3/20 23:04
# 求100以内的偶数和
sum = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print('while循环求出的100以内偶数和：', sum)

sum1 = 0
for item in range(0,101):
    if item % 2 == 0:
        sum1 += item
print('for循环求出的100以内偶数和：', sum1)

# for循环打印99乘法表
for a in range(1, 10):
    for b in range(1, a+1):
        print(a, '*', b, '=', (a*b), end='\t')
    print()

