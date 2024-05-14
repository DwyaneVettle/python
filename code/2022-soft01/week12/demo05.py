"""
    构造方法：__init__() 用于创建对象
        python中构造函数只能有一个
        如果想要通过无参构造创建对象，可以在构造函数内对参数设置默认值
    析构方法：用于销毁对象调用
            __del__()
            一般情况下，对象不需要手动销毁，python的垃圾回收机制通过引用计数器来
            管理对象，当引用计数器0的时候，该对象就会被当作垃圾回收
        引用计数器可以通过sys模块来获取
"""
import sys
class Infomation:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name}的年龄是{self.age}岁")

    def __del__(self):
        print("对象被销毁了。。。")


infomation = Infomation()
infomation.name = "张三"
infomation.age = 18
infomation.info()
print(sys.getrefcount(infomation))  # 2
# 对象被创建后的计数器的值为2，由于返回引用计数器的值的时候就会增加一个临时引用，
# 但实际的值是1

