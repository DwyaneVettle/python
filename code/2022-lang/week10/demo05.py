"""
    多态：
        多种形态
    鸭子语言-生下来走路像鸭子，那么这就是鸭子这一类
    不关注对象类型，而关注对象具有的形态
"""
class Animal:
    def move(self):
        print("动物会移动")


class Rabbit(Animal):
    def move(self):
        print("兔子会蹦蹦跳跳")

class Snail(Animal):
    def move(self):
        print("蜗牛会爬行")

# 在函数test俄中调用obj的move方法
def test(obj):
    obj.move()
    
rabbit = Rabbit()
snail = Snail()

test(rabbit)
test(snail)
