# author by Michealzou@126.com
# 2022/3/14 14:21
# 2.做一个超市购物判断：100-1000-95，1001-3000-9，3001-5000-8
# 5000-6
money = int(input("请输入你的购买金额"))
if money > 100:
    if 100 <= money <= 1000:
        print("您的折后金额为：",money * 0.95)
    elif 1000 < money <= 3000:
        print("您的折后金额为：", money * 0.9)
    elif 3000 < money <= 5000:
        print("您的折后金额为：", money * 0.8)
    else:
        print("您的折后金额为：", money * 0.6)
