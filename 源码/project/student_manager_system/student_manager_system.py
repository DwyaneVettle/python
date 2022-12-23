# author by Michealzou@126.com
# 2022/12/6 8:58
"""
    学生信息管理系统
        功能：学生信息添加、删除、修改、查询、退出程序
        学生信息：姓名、性别、手机号
        思路：1.提示用户选择某一功能
            2.根据用户的功能选项调用不同的函数
            3.增删改查的函数具有实现的功能
"""
# 创建一个列表存放学生的信息
stu_info = []
# 1.创建功能选项
def print_menu():
    print("=" * 30)
    print("学生信息管理系统")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.显示学生信息")
    print("5.退出程序")
    print("=" * 30)

# 1.添加功能-根据用户输入信息添加到容器
def add_stu_info():
    """
    学生信息：姓名、手机号、性别
    :return:
    """
    # 接收用户输入的信息
    new_name = input("请输入用户的姓名：")
    new_sex = input("请输入用户的性别：")
    new_phone = input("请输入用户的电话号码：")
    # 保存用户添加的学生信息 - 保存到什么容器？列表[]、字典{}、元组()、集合set()
    # [姓名,性别,电话号码,姓名,性别,电话号码]
    # {"name":"new_name,"sex":"new_sex","phone":"new_phone"}
    # 创建一个字典存放单个学生信息-k不能重复
    new_info = dict()
    new_info["name"] = new_name
    new_info["sex"] = new_sex
    new_info["phone"] = new_phone
    stu_info.append(new_info)

# 2.删除学生信息
def del_stu_info(student):
    """
    删除学生信息-删除的列表中的字典
    :param student: 列表
    :return:
    """
    del_num = int(input("请输入要删除的是第几个学生的序号："))
    del student[del_num - 1]

# 3.修改学生信息
def modify_stu_info():
    """
    修改学生信息
    :return:
    """
    if len(stu_info) != 0:
        # 1.接收用户输入的学生序号以及修改之后的信息
        stu_id = int(input("请输入要修改学生的序号："))
        new_name = input("请输入修改后的学生姓名：")
        new_sex = input("请输入修改后的学生性别：")
        new_phone = input("请输入修改后的学生电话：")
        # 2.把修改后的值存放到字典中-通过列表索引-字典对应的key
        stu_info[stu_id - 1]["name"] = new_name
        stu_info[stu_id - 1]["sex"] = new_sex
        stu_info[stu_id - 1]["phone"] = new_phone
    else:
        print("列表中没有学生信息，请添加后再操作！")

# 4.显示学生信息到控制台
def show_stu_info():
    print("学生信息如下：")
    print("=" * 30)
    print("序号    姓名    性别    手机号")
    i = 1
    for temp_info in stu_info:
        print("%d   %s    %s    %s" % (i, temp_info["name"],
                                       temp_info["sex"],
                                       temp_info["phone"]))
        i += 1


# 主函数
def main():
    while True:
        # 1.打印目录
        print_menu()
        key = input("请输入要操作的功能：")
        # 2.判断用户输入的功能，调用不同的函数
        if key == "1":
            add_stu_info()
        elif key == "2":
            del_stu_info(stu_info)
        elif key == "3":
            modify_stu_info()
        elif key == "4":
            show_stu_info()
        elif key == "5":
            quit_confirm = input("您真的要退出吗？(y/n):")
            if quit_confirm == "y":
                break
            else:
                print("你没有结束程序")


if __name__ == '__main__':
    main()
