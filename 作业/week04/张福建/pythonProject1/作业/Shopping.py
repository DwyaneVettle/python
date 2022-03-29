# 2022/3/12 17:48
money = int(input(""))  # 请输入购物金额：
if money < 100:
    print(money)  # 您消费多少元  不打折
elif 100 <= money <= 1000:
    print(money * 0.95)  # 您消费多少元，打95折，折后为多少元
elif 1000 < money <= 3000:
    print(money * 0.9)  # 您消费多少元，打9折，折后为多少元
elif 3000 < money <= 5000:
    print(money * 0.8)  # 您消费多少元，打8折，折后为多少元
else:
    print(f"{money}{money * 0.6}")  # 您消费多少元，打6折，折后为多少元
