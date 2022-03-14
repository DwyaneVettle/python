# 2022/3/7 17:44
money = int(input("请输入购物金额："))
if money < 100:
    print("不打折")
elif 100 <= money <= 1000:
    print(f"打9.5折, 打折后为{money * 0.95}元")
elif 1001 <= money <= 3000:
    print(f"打9折, 打折后为{money * 0.9}元")
elif 3001 <= money <= 5000:
    print(f"打8折,打折后为{money * 0.8}元")
elif money > 5000:
    print(f"打6折,打折后为{money * 0.6}元")

