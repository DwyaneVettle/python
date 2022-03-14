# zgf3513@163.com
# 2022/3/7 17:22
money = int(input("请输入购物金额："))
if money < 100:
    print(f"您消费{money}元，不打折")
elif 100 <= money <= 1000:
    print(f"您消费{money}元，打9.5折，折后为{money * 0.95}元")
elif 1000 < money <= 3000:
    print(f"您消费{money}元，打9.0折，折后为{money * 0.9}元")
elif 3000 < money <= 5000:
    print(f"您消费{money}元，打8.0折，折后为{money * 0.8}元")
else:
    print(f"您消费{money}元，打6.0，折后为{money * 0.6}元")
