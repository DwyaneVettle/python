"""
    构造方法：__init__()
        是创建类时默认就存在的方法，具有一个参数self
        作用：初始化对象时调用
        注意：在python中构造函数只有一个，区别于Java
    析构方法：__del__()
        是销毁对象调用的方法
        python垃圾回收主要是通过引用计数器来判断的，引用计数器是一种
        内存管理的方式，它通过记录一个值被引用的次数来确认是否回收，
        如果大于1，那么该对象不会被回收，如果为0就会自动调用析构
        方法进行回收
        查看引用计数器的方法
        1.导入sys模块 import sys
        2.sys.getrefcount()
        一般情况下不需要我们手动生成析构方法，因为垃圾回收机制
        会根据引用计数器来自动回收对象·
"""
# 引入系统sys模块
import sys
class Infomation:
    def __init__(self, name, age):
       self.name = name
       self.age = age
       print('创建对象时自动调用构造方法。')

    def __del__(self):
        print('销毁对象时调用该方法。')

    def info(self):
        print(f'{self.name}的年龄是{self.age}岁')


info = Infomation('张三', 18)
info.__del__()  # 调用析构方法
# 获取对象的引用计数器
print(sys.getrefcount(info))
info.__del__()  # 调用析构方法
print(sys.getrefcount(info))