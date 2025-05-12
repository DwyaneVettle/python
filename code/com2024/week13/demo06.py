"""
静态方法：没有参数的实例方法，主要完成和类无关的操作
1.没有self和cls参数，使用@staticmethod修改
2.静态方法可以由类和对象来调用
"""
class Example:
    num = 10
    @staticmethod
    def static_method():
        print('获取数量', Example.num)
        print('这是静态方法')

example = Example()
example.static_method()
Example.static_method()
