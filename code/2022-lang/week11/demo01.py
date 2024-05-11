"""
    学生管理系统
    项目计划：
        	1.完成数据模型类StudentModel
        	2.创建逻辑控制类StudentManagerController
		    3.完成数据：学生列表 __stu_list
		    4.行为：获取列表 stu_list,
		    5.添加学生方法 add_student
		    6.根据编号删除学生remove_student
		    7.根据编号修改学生update_student
		    8.在界面视图类中，根据编号删除学生.
		    9.在界面视图类中，根据编号修改学生信息.
"""
"""
    学生模型-初始化学生对象
    编号id，姓名name，年龄age，成绩score
"""


class StudentModel:
    def __init__(self, id, name, age, score):
        self.id = id
        self.name = name
        self.age = age
        self.score = score


"""
    逻辑控制类-操作增上改查的业务逻辑
"""


class StudentManagerController:
    # 初始化一个类变量，表示初始化的编号，用于每次添加学生增加的一个号码，只在类的内部使用
    __init_id = 1000

    # 初始化学生列表
    def __init__(self):
        self.__stu_list = []

    # 存储学生对象的列表
    # def get_stu_list(self):
    #     return self.__stu_list
    @property
    def stu_list(self):
        return self.__stu_list

    # 提取id自动加一的公共方法
    def __generate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def add_student(self, stu_info):
        """
            添加学生信息
        """
        stu_info.id = self.__generate_id()
        self.__stu_list.append(stu_info)

    def remove_student(self, id):
        """
            删除学生信息
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
            else:
                return "没有该学生信息"


    def update_student(self, stu_info):
        """
            根据id修改其对应的对象
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
            else:
                return "无学生信息可修改"

    def order_by_score(self):
        """
            根据成绩排序
        """
        for i in range(len(self.__stu_list) - 1):
            for j in range(i + 1, len(self.__stu_list)):
                if self.__stu_list[i].score > self.__stu_list[j].score:
                    self.__stu_list[i], self.__stu_list[j] = \
                        self.__stu_list[j], self.__stu_list[i]

"""
    测试添加学生的方法
"""
# s01 = StudentModel(0, "张三", 18, 98)
# manager = StudentManagerController()
# manager.add_student(s01)
# for item in manager.stu_list:
#     print(item.name, item.age)

"""
    测试删除学生
"""
# manager = StudentManagerController()
# s01 = StudentModel(1001, "张三", 18, 98)
# manager.add_student(s01)
# manager.remove_student(s01.id)
# print(manager.stu_list)

"""
    视图处理：    
"""
class StudentManagerView:
    def __init__(self):
        self.__manager = StudentManagerController

    def __display_menu(self):
        print("1.添加学生")
        print("2.显示学生")
        print("3.删除学生")
        print("4.修改学生")
        print("5.根据成绩排序显示学生信息")

    def __select_menu(self):
        item = input("请输入对应功能的编号：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_student(self.__manager.stu_list)
        elif item == "3":
            self.__delete_srudent()
        elif item == "4":
            self.modify_student()
        elif item == "5":
            self.__output_student_by_score()


    # 主视图入口
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        name = input("请输入姓名：")
        age = input("请输入年龄：")
        score = input("请输入成绩：")
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_student(self, list_output):
        for item in list_output:
            print(item.id, item.name, item.age, item.score)

    def __delete_srudent(self):
        id = input("输入学生编号：")
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def modify_student(self):
        id = int(input("输入id"))
        name = input("输入姓名：")
        age = input("输入年龄：")
        score = input("输入成绩：")
        stu = StudentModel(id, name, age, score)
        self.__manager.add_student(stu)

    def __output_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_student(self.__manager.stu_list)


view = StudentManagerView
view.main()
