"""
    继承：通过子类继承父类的方法和属性，可以直接使用
        作用：减少代码的编写量，增加代码的可读性
        python支持单继承和多继承
        子类继承父类后，子类就拥有了父类的成员属性和方法
    1.单继承：class子类(父类):
"""
class Amphibian:
    name = '两栖动物'
    def features(self):
        print('幼年用鳃呼吸。')
        print('成年用肺呼吸。')

class Frog(Amphibian):
    def attr(self):
        print(f'青蛙是{self.name}')
        print('青蛙呱呱呱')

frog = Frog()
print(frog.name)
frog.features()
print("==================")
frog.attr()

