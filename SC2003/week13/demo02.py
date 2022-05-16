# author by Michealzou@126.com
# 2022/5/16 14:31
# 定义类
class Animal:
    # 定义属性
    weight = 100
    height = 120
    # 定义的行为
    def eat(self):
        print("吃的行为。。。")

    def sleep(self):
        print("睡觉的行为")

# 创建对象 对象名 = 类名() ,对象名.属性;对象名.行为()
cat = Animal()
print(cat.height)
print(cat.weight)
cat.eat()
cat.sleep()
