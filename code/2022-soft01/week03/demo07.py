"""
    超市打折：
        如果100-300 95折
        301-500 9折
        501-800 8折
        801-1200 7折
        1201以上 6折
"""
money = int(input("请输入购物金额："))
if 100 <= money <= 300:
    print(f"你的购物打九五折，折后价是{money * 0.95}")
elif 301 <= money <= 500:
    print(f"你的购物打九折，折后价是{money * 0.9}")
elif 501 <= money <= 800:
    print(f"你的购物打八折，折后价是{money * 0.8}")
elif 801 <= money <= 1200:
    print(f"你的购物打七折，折后价是{money * 0.7}")
elif money >= 1201:
    print(f"你的购物打六折，折后价是{money * 0.6}")
else:
    print("你的购物金额不打折")
