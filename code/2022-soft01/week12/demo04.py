"""
    练习：
    创建学生类，要求数据成员有姓名、
    年龄、成绩、性别，并创建多个对象打印
    到控制台
"""
class Student:
    def __init__(self, name, age, score, gender):
        self.name = name
        self.age = age
        self.score = score
        self.gender = gender
    def print_info(self):
        print(f"{self.name}的年龄是{self.age}岁，考试成绩为{self.score},"
              f"性别为{self.gender}")

list01 = [
    Student("张三", 20, 90, "男"),
    Student("李四", 22, 99, "女")
]
list01[0].name = "王五"
list01[0].print_info()
list01[1].print_info()

