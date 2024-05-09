"""
    练习：创建汽车类，属性wheels、方法drive、stop
    创建对象：
        对象名 = 类名()
        对象名.属性
        对象名.方法()
"""


class Car:
    def __init__(self, wheels):
        self.wheels = wheels

    def drive(self):
        print(self, "车可以开")

    def stop(self):
        print("车可以停")


new_car = Car(4)
print(new_car.wheels)
new_car.drive()
new_car.stop()
