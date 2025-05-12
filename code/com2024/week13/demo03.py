"""
面向对象三大特征：
1.封装：将共有的属性、方法私有化
2.继承：子类继承父类的属性和方法，减少代码的复用
3.多态：同一个方法、不同对象的不同表现形式

封装：在需要进行私有化的属性和方法名字前加__
访问私有成员：
    私有属性可以在公共的方法通过self获取
"""
class Teacher:
    name = 'micheal'
    __age = '30'
    # 私有的属性和方法通过公共方法的self参数获取
    def get_age(self):
        self.__sleep()
        return self.__age

    def teach(self):
        print('教师可以教书')
    def __sleep(self):
        print('教师可以睡觉')

t01 = Teacher()
print(f'姓名{t01.name}')  # ,年龄{t01.age}
t01.teach()
# t01.__sleep()
r_age = t01.get_age()
print(r_age)

