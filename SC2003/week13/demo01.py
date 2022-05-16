# author by Michealzou@126.com
# 2022/5/16 14:09
# 定义类，class 类名首字母大小
# 类：具有相同属性和特征的某一类别
class Car:
    # 定义属性-特征
    wheel = 4
    # 定义类的方法-行为
    def driver(self):
        print("开车...")

    def __init__(self,wheel,color):
         self.wheel = wheel
         self.color = color

# 创建对象，通过类名创建(构造函数)
# 对象：是类的具体实现
car01 = Car(5,"black")
print(car01.wheel)
car01.driver()

car02 = Car(10,"white")
print(id(car01) == id(car02))  # False
print(car02.wheel)
car02.driver()
