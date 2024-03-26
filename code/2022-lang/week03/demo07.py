"""
    双重判断:
        if 条件表达式1:
            if 条件表达式2:
                代码块1
            else:
                代码块2
        else:
            代码块3
    逻辑：
        会员？ 打折
                原价
"""
answer = input("你是会员吗？y/n：")
money = int(input("请输入你的购物金额（大于300元打9折）："))
if answer == 'y':
    if money > 300:
        print(f"你的会员折后价为{money * 0.9}")
    else:
        print("你购买的金额不享受会员价")
else:
    print(f"你的应支付金额为{money}")
