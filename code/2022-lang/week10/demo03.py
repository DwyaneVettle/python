"""
    继承：
        Java：单继承 1子-1父  子类 extends 父类
        Python：单继承 1子-1父 / 多继承 1子-多父  子类(父类1，父类2...)
    子类继承父类之后，就拥有了父类的方法和属性(私有属性/私有方法除外)
    isinstance(o,t)-用于检测o的类型是不是t
    issubclass(子类,父类)-用于检测继承关系
    在多继承情况下，父类有相同的属性名，那么子类先继承谁就得到这个父类的属性
"""
# 单继承 子类(父类)
class Amphibians:
    name = "两栖动物"
    __age = 10
    def features(self):
        print("幼年用鳃呼吸。")
        print("成年用肺呼吸。")


class Frog(Amphibians):
    def attr(self):
        print(f"青蛙是{ self.name }。")
        print("它的叫声呱呱叫。")


# 创建青蛙对象
frog = Frog()
frog.attr()
frog.features()
print(isinstance(frog, Amphibians))  # True
print(issubclass(Frog, Amphibians))  # True

print("==============")

# 多继承- 子类(父类A，父类B...)
class Python:
    name = "Python"
    def learn_python(self):
        print(f"我在学{ self.name }")


class Java:
    name = "java"
    def learn_java(self):
        print(f"我在学{ self.name }")


class Student(Java, Python):
    name = "student"
    def study(self):
        print("我在学习")


s = Student()
s.learn_java()
s.learn_python()
s.study()
print(s.name)  # student
