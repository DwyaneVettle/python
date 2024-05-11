"""
    为什么方法要重写：
        当父类的方法不满足子类的需求时
    方法名字相同，参数个数或方法体不同
    当子类重写了父类的方法后，仍希望使用父类的属性和方法，可以使用关键字super
    调用父类的方法
"""
class Animal:
    def eat(self):
        print("动物会吃东西。。。")


class Dog(Animal):
    name = "中华田园犬"
    def eat(self):
        print(f"{ self.name }吃肉")
        super().eat()


dog = Dog()
dog.eat()
