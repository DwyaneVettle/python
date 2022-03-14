# 2022/3/13 23:24
print("水仙花数：")
for n in range (100, 1000):
    a = n % 10
    b = n//10 % 10
    c = n//100
    if n == a**3+b**3+c**3:
        print(n)
