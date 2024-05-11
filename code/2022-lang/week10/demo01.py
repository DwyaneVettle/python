"""
    类方法：
        1.右@classmethod来修饰
        2.第一个参数是cls，而不是self
        3.类方法可以由类直接调用，也可以由对象调用
        4.类方法可以作为修改属性的值使用
"""


class Test01:
    @classmethod
    def use_classmethod(cls):
        print("这是一个类方法。")


test01 = Test01()
test01.use_classmethod()
Test01.use_classmethod()


class Apple:
    count = 0

    def add_one(self):
        self.count = 1

    @classmethod
    def add_two(cls):
        cls.count = 2


apple = Apple()
# apple.add_one()
# print(Apple.count)
Apple.add_two()
print(Apple.count)
print(apple.count)
