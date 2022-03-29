# 2022/3/15 21:14
# for循环

a = 0
for b in range(0, 101, 2):
    a += b
print(a)

# while循环
c = 0
d = 0
while d <= 100:
    c += d
    d += 2
print(c)
# 99乘法表
for i in range(1, 10):
    for n in range(1, i - 1):
        print(n, '*', i, '=', (i * n), end='\t')
    print("")
