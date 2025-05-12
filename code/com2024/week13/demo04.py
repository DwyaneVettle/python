"""
练习：模拟银行支取款项
    现有ICBC总行1000000元，成都支行和眉山支行分别支取了20000元
    和10000元，计算总行剩余的金额
    用面向对象的思想来解决
在类方法中要想获得属性的值，可以将这个方法由普通方法升级为类方法
在该方法上添加注解@classmethod
类方法可以直接通过类名获取属性和方法
"""
class ICBC:
    # 初始化总行的金额
    total_money = 1000000
    # 构造方法
    def __init__(self, name, money):
        self.name = name
        self.money =money
        ICBC.total_money -= money

    # 获取余额的方法
    @classmethod
    def print_total_money(cls):
        print(f'总行还剩{ICBC.total_money}')

c = ICBC('成都支行', 20000)
m = ICBC('眉山支行', 10000)
print('总行还剩%d元' % ICBC.total_money)




