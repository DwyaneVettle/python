"""
    解释流程控制
"""
price = int(input("请输入你购买的金额："))
if (price > 100):
    zhe = price * 0.8
    print(f"你的折后价是{zhe}元")
else:
    print(f"你的购买金额不能打折")
