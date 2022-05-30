# author by Michealzou@126.com
# 2022/5/23 14:51
# 方法的重写：当父类方法中的功能不能满足自身的需求的时候，就可以重写这个方法，添加自己想要的功能
class Felines:
    name = "猫科动物"
    def speciality(self):
        print("猫科动物会爬树。。。。")


class Cat(Felines):
    name = "小猫咪"
    def speciality(self):
        print(f"{self.name}会抓老鼠....")
        print(f"{self.name}也会爬树....")
        # 如果在方法重写中，仍然坚持要使用父类保留的属性和方法，关键字super()
        super().speciality()
        print(super().name)


cat01 = Cat()
cat01.speciality()

