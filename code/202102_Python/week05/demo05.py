# author by Michealzou@126.com
# 2022/10/4 9:42
"""
案例： 9：50
    会员和今晚都要根据用户输入进行匹配
  根据用户是否为超时会员
    如果是  购物金额大于100块，打9折
            购物金额大于200块，打8折
    如果不是会员  购物金额大于200块，打95折，
                其他不打折
"""
answer = input("您是会员吗？y/n")
money = float(input("请输入购物金额："))
if answer == 'y':
    if money >= 200:
        print("您的购物金额超过200元，打8折，折后价是" + str(money*0.8))
    elif money >= 100:
        print("您的购物金额大于100元小于200元，打9折，折后价是" + str(money * 0.9))
    else:
        print("您的购物金额不打折" + str(money))
else:
    if money >= 200:
        print("您的购物金额超过200元，打8折，折后价是" + str(money*0.95))
    else:
        print("您的购物金额不打折" + str(money))
