# author by Michealzou@126.com
# 2022/8/8 13:40
# pyhton中既支持单继承，又支持多层继承，还支持多继承
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print('Animal eat food')

class Dog(Animal):
    def eat(self):
        print("eat dog food")

class God:
    def eat(self):
        print("God eat peach")

    def fly(self):
        print("God can fly")

class XTQ(God, Dog):  # 多继承(C3算法)
# 调用所有父类的eat()方法

    def eat(self):
        Dog.eat(self)
        God.eat(self)  # 多继承调用父类方法专用
        Animal.eat(self)

    def bark(self):
        print("Howl")

xtq = XTQ('Howling dog')
xtq.eat()