# 2022/3/9 11:01

for num in range(100, 1000):
    x = num // 100  # 百位数
    y = num // 10 % 10  # 十位数
    z = num % 10  # 个位数
    if num == x ** 3 + y ** 3 + z ** 3:
        print(num)

       
