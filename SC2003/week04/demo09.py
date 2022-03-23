# author by Michealzou@126.com
# 2022/3/21 13:17
i = 1
sum1 = 0
while i <= 100:
    if i % 2 == 0:
        sum1 = sum1 + i
    i = i + 1
print(sum1)
sum2 = 0
for i in range(0, 101):
    if i % 2 == 0:
        sum2 = sum2 + i
print(sum2)

for x in range(1, 10):
    for y in range(1, x + 1):
        print(f"{x} * {y} = {x*y}", end=" ")
    print()