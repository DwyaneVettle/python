"""
面向对象三大特征：
1.封装：对属性和方法的私有化
2.继承：子类继承父类的属性和方法
3.多态：一个类可以创建多种形态-鸭子语言（形似于鸭子的特性，都统一的看作是鸭子）
多态：同一个函数会根据参数的类型去调用不同的方法，从而产生不同结果形态
"""
class Animal:
    def move(self):
        print('动物可以移动')

class Rabbit(Animal):
    def move(self):
        print('兔子可以蹦蹦跳跳')

class Snail(Animal):
    def move(self):
        print('蜗牛可以爬行')

# 创建test函数，调用obj的move方法
def test(obj):
    obj.move()

rabbit = Rabbit()
snail = Snail()
test(rabbit)
test(snail)
