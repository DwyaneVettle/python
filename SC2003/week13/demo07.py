# author by Michealzou@126.com
# 2022/5/16 16:47
"""
静态方法：@staticmethod定义
既可以由对象调用，又可以被类来调用
静态方法内没有参数
类方法和静态方法的区别：
    类方法有一个参数cls，使用这个参数可以直接访问类中的成员
    静态方法没有参数，无法使用参数来访问类成员
    静态方法更适合用于做和类无关的操作
"""
class Test:
    num = 10  # 类属性
    # 静态方法
    @staticmethod
    def static():
        print(f"类属性num的值为：{Test.num}")

test = Test()
test.static()
Test.static()


