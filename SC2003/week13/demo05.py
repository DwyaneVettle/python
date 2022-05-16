# author by Michealzou@126.com
# 2022/5/16 16:00
# 构造函数和析构函数
"""
    构造函数是在创建对象的时候自动调用__init__()
    析构函数__del__()，通过getrefcount()函数来去观察的，只大于1，这个对象就
    在被引用，而等于0的时候，就会自动调用__del__()
"""
import sys
class Life:
    def __init__(self):
        print("对象被创建了。。。。")
    def __del__(self):
        print("对象被销毁了。。。。")

    def eat(self):
        print("吃饭睡觉打豆豆。。。。")

life = Life() # 创建对象调用__init__()
# getrefcount()打印的结果通常超过期望值，一般为2
print(sys.getrefcount(life))
life.eat()
print(sys.getrefcount(life))
