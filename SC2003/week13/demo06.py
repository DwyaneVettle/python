# author by Michealzou@126.com
# 2022/5/16 16:26
"""
定义类方法:@classmethod
既可以由对象来调用，也可以由类来调用
类方法的参数不是self,而是cls，表示类的本身
作用：修改类的属性，在实例方法中没有办法修改属性的值。在类方法中可以将属性的值进行修改。
"""
class Test:


    @classmethod
    def use_class(cls):
        print("这是一个类方法")

test = Test()
test.use_class()
Test.use_class()


class Apple:
    count = 0  # 定义属性
    # 定义实例方法
    def add_noe(self):
        self.count = 1

    @classmethod
    def add_two(cls):
        cls.count = 2

apple = Apple()
apple.add_noe()
print(Apple.count)
print(apple.count)  # apple对象找到的是实例方法中的count值，这个count是和类同名的一个属性
apple.add_two()
print(Apple.count)