# author by Michealzou@126.com
# 2022/10/5 10:33
"""
    是否为会员：
        是会员：100以上 9  200以上 8
        非会员： 200以上 95  其他不打折
    1.判断是否会员
    2.根据会员与否判断金额大小
"""
answer = input("您是否为会员y/n:")
money = float(input("请输入您的购物金额："))
if answer == 'y':
    if 100 <= money < 200:
        print("您的折后价为：" + str(money * 0.9))
    elif money >= 200:
        print("您的折后价为：" + str(money * 0.8))
    else:
        print("您的购物没有折扣")
else:
    if money >= 200:
        print("您的折后价为：" + str(money * 0.95))
    else:
        print("您的购物没有折扣")

