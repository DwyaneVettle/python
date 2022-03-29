# 2022/3/16 9:44
# for循环求100以内偶数的和
b = 0
for a in range(0,101,2):
    b += a
    print(b)

print('===============================')

# while循环求100以内偶数的和
c = 0
d = 0
while d <= 100:
    c += d
    d += 2
print(c)

print('==================================')

# 嵌套for循环打印九九乘法表
for e in range(1,10):
    for f in range(1,e+1):
        print(f,"*", e,"=",(f*e),end="\t")
    print("")
