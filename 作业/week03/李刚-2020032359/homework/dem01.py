# 2022/3/7 17:02
for i in range(100,1000):
    g=i%10
    s=i//10%10
    b=i//100
    if g**3+s**3+b**3==i:
        print(i)