"""
创建学生类，要求数据成员有姓名、年龄、成绩、性别，并在控制台打印。
"""
class Student:
    def __init__(self, name, age, score, gender):
        self.name = name
        self.age = age
        self.score = score
        self.gender = gender

    # 方法
    def print_info(self):
        print(f"姓名：{self.name}，年龄：{self.age}，成绩：{self.score}，性别：{self.gender}")

# 创建对象
student01 = Student('张三', 20, 88, '男')
student02 = Student('李四', 30, 98, '女')
student03 = Student('王五', 40, 78, '男')
student01.print_info()
student02.print_info()
student03.print_info()

list01 = [
    Student('张三', 20, 88, '男'),
    Student('李四', 30, 98, '女')
]
s01 = list01[0]
s02 = list01[1]
s01.print_info()
s02.print_info()


