b = int(input("请输入第一个范围："))
c = int(input("请输入第二个范围："))
for a in range(b,c):
    x = a // 100
    y = a // 10 % 10
    z = a % 10
    if a == x ** 3 + y ** 3 + z ** 3:
        print(f'范围内的水仙花数有：{a}')