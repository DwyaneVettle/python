# author by Michealzou@126.com
# 2022/8/8 13:11
# 类：把具有相同属性和相似行为的一些对象抽象出的一个概念
class Animal:
    def __init__(self):
        # 构造函数中的self指的是当前类的对象
        print("this is construction methods")

# 通过类的构造方法来创建对象p,dog,cat
dog = Animal()  # 无参数构造函数
cat = Animal()