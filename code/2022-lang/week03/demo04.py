"""
    判断单分支：
        if 条件表达式:
            代码块
        只有条件表达式成立，才执行代码块
    练习：
        用户输入购买货品的金额，如果金额大于1000元，给用户打8折，并输出折后价
        buy_money = int(input("输入购买的金额:"))
        if buy_money > 1000:
                print(f"你的金额满足打折条件，折后价为{buy_money * 0.8}")

        双分支语法：
            if 条件表达式:
                代码块1
            else:
                代码块2


"""
money = 1000
sal = int(input("请输入你要取的金额："))
if money >= sal:
    print(f"你的取款金额是{sal},你的余额还剩{money - sal}")
else:
    print("你的取款金额大于余额!")

