"""
    静态方法：
        1.静态方法没有self参数，通过@staticmethod修饰
        2.静态方法需要通过“类名.方法/属性”访问类成员
        3.静态方法既可以由对象调用，也可以通过类直接调用
        4.静态方法更适合操作和类无关的事情
"""
class Test02:

    num = 10
    @staticmethod
    def static_method():
        print(f"num属性的值是{Test02.num}")

test02 = Test02()
test02.static_method()
print(test02.num)
Test02.static_method()

