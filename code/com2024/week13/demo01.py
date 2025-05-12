"""
1.类与对象的思想：
    类：某一类具有相同特征事物的集合 如：人类、汽车类、动物类
    对象：某一类事物中所具有独立特征的个体，如：张三、李四、王五
面向对象思想：将现实世界的事物抽象成程序中的类和对象，然后使用类和对象来描述现实世界中的事物及事物之间的相互关系
类是对象的模板，对象是类的实例
2.类的定义：class 类名：
            代码块
    注意：类名首字母要大写，多个单词用驼峰命名法
每个类都有自己默认的构造函数`__init__()`,当创建对象的时候，就会调用该函数，可以省略
在构造函数中有一个默认的参数self，它代表类的实例对象，相当于Java中的this关键字

3.对象的定义：对象名 = 类名()
    注意：对象名首字母要小写，多个单词用驼峰命名法
    属性/方法：对象.属性/方法()
"""
# 定义类
class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    # 属性-特征
    name = '张三'
    age = 20
    gender = '男'
    # 行为/方法
    def study(self):
        print('学生以学习为天职！')

# 定义学生对象
stu = Student('李四', 20, '男')
print('姓名：', stu.name)
print('年龄：', stu.age)
print('性别：', stu.gender)
stu.study()

"""
    练习：定义一个汽车类：
    要求属性wheels、color、brand、price
        方法：diver()、stop()
    创建一个汽车对象
"""
class Car:
    def __init__(self, wheels, color, brand, price):
        self.wheels = wheels
        self.color = color
        self.brand = brand
        self.price = price

        def driver(self):
            print('汽车可以驾驶')
        def stop(self):
            print('汽车可以停车')
# 创建一个汽车对象
car01 = Car(4, '白色', '奔驰', 1000000)
car02 = Car(4, '黑色', '宝马', 2000000)
print('汽车1：', car01.wheels, car01.color, car01.brand, car01.price)
print('汽车2：', car02.wheels, car02.color, car02.brand, car02.price)