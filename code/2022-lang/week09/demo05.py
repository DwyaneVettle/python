
class Student:

    def __init__(self, name, age, score, gender):
        self.name = name
        self.age = age
        self.score = score
        self.gender = gender

    def print_info(self):
        print(f"我是{self.name},年龄是{self.age},成绩是{self.score},性别是{self.gender}")


stu01 = Student("张三", 20, 90, "男")
stu02 = Student("李四", 22, 98, "女")
stu01.print_info()
stu02.print_info()
