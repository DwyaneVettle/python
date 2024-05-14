"""
    类方法：@classmethod修饰
        1.第一个参数是cls，而不是self
        2.类方法可以由对象调用，也可以直接由类调用
        3.类方法可以修改属性，以及如何使用类方法修改类属性
"""
class Test:

    @classmethod
    def use_classmethod(cls):
        print("这是一个类方法。。。")

test = Test()
test.use_classmethod()
Test.use_classmethod()



class Apple:

    count = 0
    def add_one(self):
        self.count = 1
    @classmethod
    def add_two(cls):
        cls.count = 2

apple = Apple()
apple.add_one()
print(Apple.count)  # 0
print(apple.count)  # 1
Apple.add_two()
print(Apple.count)  # 2
print(apple.count)  # 1
