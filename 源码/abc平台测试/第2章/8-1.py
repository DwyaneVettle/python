# author by Michealzou@126.com
# 2022/8/8 13:17
class Animal:
    def __init__(self, name):
        self.name = name  # python中成员属性的定义语法
        self.color = 'white'

# 无参构造函数
cat = Animal('cat')
print("{} is {} ".format(cat.name, cat.color))

# 创建名为旺财狗的对象dog，并将对象属性color赋值成金色，输出name属性和color
# 属性的值

dog = Animal('dog')
dog.color = 'black'
# print(dog.age)
print("{} is {}".format(dog.name, dog.color))
