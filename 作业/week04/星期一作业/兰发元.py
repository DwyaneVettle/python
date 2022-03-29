# author by hliy_ss@163.com
# 2022/3/17 22:50


# 九九乘法表
for i in range(1, 10):
    for a in range(1, i + 1):
        print(f"{i}*{a}={i*a}", end="\t")
    print()

A = 1
while A <= 9:
    B = 1
    while B <= A:
        print(f"{A}*{B}={A * B}", end="\t")
        B += 1
    A += 1
    print()


# 用for循环和while循环求100以内偶数的和

sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum = sum+i
    print(sum)


A = 1
B = 0
while A <= 100:
    if A % 2 == 0:
        B = B + A
    A = A + 1
print(B)
