# author by Michealzou@126.com
# 2022/5/23 15:34
class Person:

    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    def teach(self,other,skill):
        print(self.name,"教",other.name,skill)

    def work(self,money):
        print(self.name,"上班挣",money)


zwj = Person("张无忌")
zm = Person("赵敏")
zwj.teach(zm, "九阳神功")
zm.teach(zwj, "化妆")
zwj.work(1000)
zm.work(6000)