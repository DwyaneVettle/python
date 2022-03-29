# author by MiWuXianLi
# 2022/3/20 13:51
# 求100以内的偶数和
sum01 = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        sum01 += i
    i += 1
print('while循环求出的100以内偶数和：', sum01)

sum02 = 0
for item in range(0,101):
    if item % 2 == 0:
        sum02 += item
print('for循环求出的100以内偶数和：', sum02)
