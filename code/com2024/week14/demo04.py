"""
`方法重写：当子类不满足父类的需求时，可以通过重写方法来扩展需求
 当方法重写后，调用该方法时自动调用子类本身的方法
 如果重写了方法后子类仍然希望调用父类的方法，可以使用super()
"""
class Felines:
    def feature(self):
        print('猫科动物特长是爬树。')

class Cat(Felines):
    name = '猫'
    def feature(self):
        print('猫可以抓老鼠')
        print(f'{self.name}也会爬树。')
        super().feature()

cat = Cat()
cat.feature()

