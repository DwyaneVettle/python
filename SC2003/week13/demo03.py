# author by Michealzou@126.com
# 2022/5/16 14:53
# 访问控制权限，封装性,__定义私有属性或方法
class PersonInfo:
    # 当有__定义的属性时，对象不能轻易访问
    __weight = 60

    def __info(self):
        print("个人信息。。")

    def get_weight(self):
        print(f"我的体重是{self.__weight}")
        self.__info()


a = PersonInfo()
# print(a.__weight)
a.get_weight()

