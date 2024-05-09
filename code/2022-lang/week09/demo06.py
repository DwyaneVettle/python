"""
    构造函数__init__()是在创建对象时调用的
    析构函数__del__()是在对象销毁时自动调用
    对象身上有引用计数器，当引用计数器为0就调用析构方法
    sys模块下有方法getrefcount()能统计对象的应用次数
"""
import sys
class Person:
    def __init__(self):
        print("对象被创建了。。。")

    def __del__(self):
        print("对象被销毁了。。。")

p01 = Person()
print(sys.getrefcount(p01))

