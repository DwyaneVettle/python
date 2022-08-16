# author by Michealzou@126.com
# 2022/8/8 13:24
# 封装：隐藏对象的属性和实现细节，只对外部提供公共的访问方式（get、set方法）
# 私有属性的访问范围： 当前类中可以使用
class Student:
    def __init__(self, name):
        self.name = name
        self.__age = 0  # 私有属性的命名 __变量名

    # 为私有属性创建get(获取)、set(赋值)方法
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int):
            if age < 0:
                print("年龄不能为负数")
            elif age > 150:
                print("年龄不正确")
            else:
                self.__age = age  # 将形参age赋值给对象属性__age
        else:
            print("年龄必须是整数")

# 1.通过学生类创建学生对象
xiaoHong = Student('xiaohong')

# 2.通过get方法获取私有的成员属性
xiaoHong.set_age(32)
print(xiaoHong.get_age())