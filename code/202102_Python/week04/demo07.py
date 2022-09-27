# author by Michealzou@126.com
# 2022/9/27 11:50
"""
    单分支
        if 条件表达式:
            代码块
    如条件表达式成立，就执行代码块
"""
money = 10000
# 1.输入金额取钱
jine = int(input("请输入取款余额："))
# 2.判断余额是否充足，如果不充足就提示余额不足
if jine > money:
    print("余额不足")
# 3.取钱后显示余额
print("你的余额还有：" + str(money - jine))
