# author by Michealzou@126.com
# 2022/5/23 14:20
# 多继承：Python支持多继承，格式：子类(父类1，父类2，父类3.。。。)
# 父类私有的属性和方法都不能继承
class Python:
    name = "python"

    def study_python(self):
        print("我再学Python")


class Java:
    __name = "java"

    def study_java(self):
        print("我在学Java")


# 实现多继承，继承多个类
# 如果多个父类有相同的属性或行为，优先继承第一个
class Student(Java, Python):

    def type(self):
        print("我是学生")


stu = Student()
stu.type()
print(stu.name)
stu.study_java()
stu.study_python()


# 继承两个类的相同属性