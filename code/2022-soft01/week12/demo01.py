"""
    面向对象：一切皆为对象
        对象：现实中可以描述的事物，归属于某一个类别的个体
        类：从具体书屋中抽取共同的特点，并形成一个类别
        类是创建对象的模板，对象是类的具体化
        对象：属性  方法
    类：
        定义类：class 类名:  (类名的定义和Java相同，驼峰命名法)
                 属性名 = 属性值
                 def 方法名(self):
                    方法体
    对象：
        定义对象：对象名 = 类名()
        构造方法：def __init__(self):
        self == this 指代当前对象
        对象名.属性
        对象名.方法
"""
class Car:
    wheels = 4  # 属性
    def drive(self):  # 方法
        print("汽车可以驾驶...")
    def stop(self):
        print("汽车可以停车...")
    # 构造方法
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

car01 = Car(1000, "大众")
print(car01.wheels)
car01.stop()
car01.drive()



