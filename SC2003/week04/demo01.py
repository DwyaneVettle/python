# author by Michealzou@126.com
# 2022/3/14 14:51
# pass语句：表示什么都不做，流程控制语句中的过渡
money = int(input("请输入金额："))
if money > 100:
    print("折后金额为：",money * 0.5)
elif money < 100:
    pass
