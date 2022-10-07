# author by Michealzou@126.com
# 2022/10/5 10:04
"""
练习：
    超市购物：
        100-200  95
        201-500  9
        501-800  85
        801-1200 8
        1200<    6
"""
money = float(input("请输入您的购物金额："))
if 100 <= money <= 200:
    print(f"您的购物金额为{money}，折后价为" + str(money * 0.95))
elif 201 <= money <= 500:
    print(f"您的购物金额为{money}，折后价为" + str(money * 0.9))
elif 501 <= money <= 800:
    print(f"您的购物金额为{money}，折后价为" + str(money * 0.85))
elif 801 <= money <= 1200:
    print(f"您的购物金额为{money}，折后价为" + str(money * 0.8))
else:
    print(f"您的购物金额为{money}，折后价为" + str(money * 0.6))

