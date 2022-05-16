# author by Michealzou@126.com
# 2022/5/16 15:12
# 练习：创建学生类，属性信息私有，要求给学生的姓名，性别，年龄进行赋值并打印
class Student:
    __name = "zhangsan"
    __sex = "man"
    __age = 30

    def get_info(self):
        print(f"姓名:{self.__name},性别：{self.__sex},年龄：{self.__age}")

    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age

    def get(self):
        print(f"姓名:{self.name},性别：{self.sex},年龄：{self.age}")

# a = Student()
# a.get_info()
b = Student("lisi","nan",20)
b.get()
c = Student("wangwu","nv",18)
c.get()
