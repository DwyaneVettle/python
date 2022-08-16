# author by Michealzou@126.com
# 2022/8/8 14:16
class Student:
    count = 0

    def __init__(self):
          self.name = "Micheal"
          Student.count += 1
          print("__init__")

    def __del__(self):
         print("__del__")

    def __str__(self):
         print("__str__")

s = Student()
s2 = Student()
print(Student.count)


