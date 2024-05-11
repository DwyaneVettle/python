"""
    静态方法：
        1.使用@staticmethod修饰
        2.第一个参数既不是self,也不是cls
        3.既可以被类调用，也可以被对象调用
    静态方法和类方法的区别：
        1.参数：类方法有参数cls，静态方法无参数
        2.成员访问：类方法可以访问成员，静态方法只能通过类来访问成员
        总结：静态方法更适合操作和类无关的事情
"""
class Test02:

    num = 10
    @staticmethod
    def static_method():
        print("这是类的静态方法。")
        print(f"num的值{ Test02.num }")


test02 = Test02()
test02.static_method()
Test02.static_method()
print("=========")
Test02.num = 3
print(Test02.num)
test02.num = 5
print(test02.num)

