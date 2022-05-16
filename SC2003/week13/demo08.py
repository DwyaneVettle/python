# author by Michealzou@126.com
# 2022/5/16 17:03
# 继承，单继承，多继承
# class 子类(父类)：
class Amphibian:
    type = "两栖动物"

    def features(self):
        print("幼年用鳃呼吸。。。")
        print("成年用肺呼吸。。。")


class Frog(Amphibian):
    def attr(self):
        print(f"青蛙是{self.type}")
        print("长得漂亮。。。")

class Dog:
    pass

linwa = Frog()
linwa.attr()
print(linwa.type)
print(linwa.features())
# 验证创建对象是否为某一类型,是返回True,不是则返回False
print(isinstance(linwa,Frog))
# 验证两个类之间是否有继承关系，有返回True,没有则返回False
print(issubclass(Dog,Amphibian))