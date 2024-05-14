# 练习： 编写Animal 属性x2 方法x2 --> 创建对象
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name}能吃很多东西.")
    def sleep(self):
        print(f"{self.name}很会睡")

# 定义对象
cat = Animal("加菲猫", 5)
print(cat.name, cat.age)
cat.sleep()
cat.eat()
dog = Animal("小狗", 3)
print(dog.age, dog.name)
dog.eat()
dog.sleep()
