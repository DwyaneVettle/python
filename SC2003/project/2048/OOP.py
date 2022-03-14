# author by Michealzou@126.com
# 2022/3/3 16:52
class Animal:
    def move(self):
        pass

class Rabbit(Animal):
    def move(self):
        print("兔子可以蹦蹦跳跳")

class Snail(Animal):
    def move(self):
        print("蜗牛可以爬行")

# 在函数test()中调用了对象obj的move()方法
def test(obj):
    obj.move()

rabbit = Rabbit()
test(rabbit)
snail = Snail()
test(snail)