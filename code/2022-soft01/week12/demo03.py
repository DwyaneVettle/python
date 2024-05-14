"""
    面向对象的语言三大特性：封装  继承  多态
    封装：类中定义的方法和属性默认是共有的，该类所派生的对象可以任意访问共有成员
        将类中的成员进行封装之后，对象就不能轻易的访问到了
        方法： __属性名
              __方法名
        访问： 在公共方法中，__属性名/方法名

"""
class PersonInfo:
    __weight = 60
    name = ""
    def __info(self):
        print(f"{self.name}的体重是{self.__weight}公斤")
    # 在公共方法中访问私有成员
    def get_info(self):
        self.__info()
        print(f"体重是{self.__weight}公斤")

zhangsan = PersonInfo()
zhangsan.name = "张三"
print(zhangsan.name)
zhangsan.get_info()

