"""
类方法：
比普通方法多一个参数self的方法是类的实例方法，只能通过由类创建的对象来调用
如果需要类来调用自己的属性和方法，那么需要编写类方法
1.使用@classmethod来标识该方法
2.类方法中的第一个参数为cls，而不是self
3.类方法既可以由类调用，也可以使用对象来调用
作用:可以修改类的属性，以及如何使用类方法修改类的属性
"""
class Apple:
    count = 0

    def add_one(self):
        self.count = 1

    @classmethod
    def add_two(cls):
        cls.count = 2

# 需求：调用这两个方法来增加苹果的数量
apple = Apple()
apple.add_one()
print(Apple.count)
Apple.add_two()
print(Apple.count)
