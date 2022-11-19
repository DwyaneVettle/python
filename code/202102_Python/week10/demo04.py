# author by Michealzou@126.com
# 2022/11/8 9:42
"""
    def 定义函数 defined
    函数：增加代码的复用性
"""


def attack():
    print("直拳")
    print("勾拳")
    print("佛山无影脚")


# 调用函数 方法名()
attack()
attack()
attack()
attack()
attack()
print("-------")


# 可拓展性
def attack_repeat(count):
    for i in range(count):
        print("直拳")
        print("勾拳")
        print("佛山无影脚")


attack_repeat(1)
