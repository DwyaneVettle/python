"""
    练习：
    判断购物金额是否大于300，并且是否是会员，如果是，则打八折，并输入打折后的金额
    否则，不打折，输出原价
"""
price = int(input("请输入购物金额："))
is_member = False
if price > 300 and is_member == True:
    print(f"你购物金额打折后{price * 0.8}")
else:
    print(f"你购物金额不打折{price}")
