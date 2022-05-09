# author by Michealzou@126.com
# 2022/5/9 15:22
""""
学生信息系统：实现对学生的增加、删除、修改、查询
需求：根据菜单栏的序号实现功能
"""
# 1.创建容器放学生信息
stu_info = []
# 2.创建菜单栏，根据菜单栏的选项实现增删改查的功能
def print_menu():
    print("学生管理系统")
    print("1.增加学生信息：")
    print("2.删除学生信息：")
    print("3.修改学生信息：")
    print("4.查询学生信息：")
    print("0.退出系统：")


# 3.定义增加信息的方法，增加学生姓名，性别，电话
def add_stu_info():
    # 接收用户输入的信息
    stu_name = input("请输入姓名：")
    stu_sex = input("请输入性别：")
    stu_tel = input("请输入电话号码：")
    # 创建字典，将字段和用户输入的信息对应
    new_stu = dict()
    new_stu['name'] = stu_name
    new_stu['sex'] = stu_sex
    new_stu['tel'] = stu_tel
    stu_info.append(new_stu)


# 4.定义删除信息的方法
def del_stu_info(student):
    del_num = int(input("请输入删除的编号：")) - 1
    del student[del_num]


# 5.定义修改信息的方法
def modify_stu_info():
    # 根据学生的编号来修改
    stu_id = int(input("请输入学生编号")) - 1
    new_name = input("请输入修改后的姓名：")
    new_sex = input("请输入修改后的性别：")
    new_tel = input("请输入修改后的电话：")
    stu_info[stu_id]['name'] = new_name
    stu_info[stu_id]['sex'] = new_sex
    stu_info[stu_id]['tel'] = new_tel


# 6.定义查询信息的方法
def show_stu_info():
    print("学生信息如下：")
    print("编号   姓名   性别   电话号码")
    i = 1
    for info in stu_info:
        print(f"{i},{info['name']},{info['sex']},{info['tel']}")
        i += 1



# 7.主程序
def main():
    while True:
        # 打印菜单，根据菜单编号来实现业务
        print_menu()
        key = int(input("请输入菜单编号："))
        if key == 1:
            add_stu_info()
        elif key == 2:
            del_stu_info(stu_info)
        elif key == 3:
            modify_stu_info()
        elif key == 4:
            show_stu_info()
        elif key == 0:
            mes = input("你确定退出吗？yes&no")
            if mes == 'yse':
                break
            else:
                print("输入错误，请重新输入")


# 8.测试
# add_stu_info()
# show_stu_info()
if __name__ == '__main__':
    main()
