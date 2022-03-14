# 2022/3/13 23:33
money = int(input('输入你的金额：'))
if 100 <= money <= 1000:
    print("你的折扣为：95折")
elif 1001 <= money <= 3000:
    print("你的折扣为：9折")
elif 3001 <= money <= 5000:
    print("你的折扣为：8折")
