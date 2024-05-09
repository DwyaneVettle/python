"""
    面向对象的语言都拥有三大特性：封装、继承、多态
    封装：当属性和方法不能随便被访问时，我们可以对类的成员进行封装
    public protect private  -- java
    __属性名  __方法   -- python
    访问：
        私有属性：可以在公共的方法中通过指代类本身的默认参数self进行访问
        类外部可以通过公共的方法间接获取类的私有属性
        私有方法：可以在公共的方法内部通过self访问私有方法
"""


class PersonInfo:
    __weight = 50

    def __info(self):
        print(f"我的体重是：{self.__weight}")

    def get_weight(self):
        print(f"我的体重是{self.__weight}公斤")
        self.__info()


stu = PersonInfo()
stu.get_weight()


