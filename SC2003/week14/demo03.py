# author by Michealzou@126.com
# 2022/5/23 15:12
import demo01 as a
import time
import random
from demo01 import Java as b
# 多态：当一些对象具有某一共同特征时，那么就可以把这些对象看作为同一类
class Animal:
    def move(self):
        pass

class Person(Animal):
    def move(self):
        print("人也可以爬行...")

# 公共的测试方法,在函数test()调用对象obj的move()方法
def test(obj):
    obj.move()


class Xiyi(Animal):
    def move(self):
        print("蜥蜴也可以爬行。。。")

person = Person()
test(person)  # 接收Person类的对象

xiyi = Xiyi()
test(xiyi)

a.Python.study_python()
b.study_java()