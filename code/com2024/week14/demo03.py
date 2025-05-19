"""
    多继承：一个子类可以继承多个父类
    语法：class 子类(父类1,父类2...)
    在多继承关系中，第一个继承的父类具有较高的优先级
    父类具有相同的属性或方法时，第一个继承的父类具有优先获取的权力
"""
class English:
    name = '英语'
    def know_english(self):
        print('会英语')

class Math:
    name = '数学'
    def know_math(self):
        print('会数学')

class Student(Math, English):
    def study(self):
        print('学生的任务是学习。')


stu = Student()
stu.know_english()
stu.know_math()
print(stu.name)
