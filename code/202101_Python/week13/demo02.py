# author by Michealzou@126.com
# 2022/11/30 9:27
"""
    使用函数实现一个学生信息管理系统
    学生信息：姓名、性别、手机号
    实现功能：添加、删除、修改、显示、退出系统
    思路：
        1.提示用户根据功能的序号选择功能
        2.系统获取用户选择的功能
        3.有增删改查退出的函数
        4.根据用户的功能选择选项调用不同的函数
"""
# 创建列表用于保存所有学生的信息
stu_info = []
# 1.功能菜单打印
def print_menu():
    print("=" * 30)
    print("学生信息管理系统")
    print("1.添加学生信息（姓名/性别/手机号）:")
    print("2.删除学生信息:")
    print("3.修改学生信息:")
    print("4.显示学生信息:")
    print("0.退出程序:")
    print("=" * 30)

# 2.添加学生信息
def add_stu_indo():
    # 用input()接收用户添加的值
    new_name = input("请输入学生的姓名：")
    new_sex = input("请输入学生性别（男/女）：")
    new_phone = input("请输入学生电话号码：")
    # 存储信息---思考：用什么来存储？
    """
        用字典接收单个学生的信息
        用列表存储所有的学生
        dic = {name:new_name,sex:new_sex,phone:new_phone}
        lst = [dic01,dic02]
    """
    new_info = dict()

    new_info["name"] = new_name
    new_info["sex"] = new_sex
    new_info["phone"] = new_phone
    stu_info.append(new_info)

# 3.删除学生信息
def del_stu_info(student):
    del_num = int(input("请输入要删除学生的序号："))
    del student[del_num-1]


# 4.修改学生信息
def modify_stu_info():
    """
    根据用户输入的学生序号修改信息（列表）
    :return:
    """
    # 4.1.接收用户输入的学生序号和更改后的学生信息
    stu_id = int(input("请输入学生对应的序号："))
    new_name = input("请输入学生的姓名：")
    new_sex = input("请输入学生性别（男/女）：")
    new_phone = input("请输入学生电话号码：")
    # 先获取序号，根据序号找到对一个保存学生信息列表的个数（列表的下标）
    # 找到列表下标之后就找到了保存单个学生的字典
    # 根据字典的k，修改字典的v
    stu_info[stu_id - 1]['name'] = new_name
    stu_info[stu_id - 1]['sex'] = new_sex
    stu_info[stu_id - 1]['phone'] = new_phone

# 5.显示学生信息
def show_stu_info():
    print("学生信息如下：")
    print("=" * 30)
    # 序号用于删除和修改，定义一个初始值1，根据学生信息累加
    # 列表遍历出来的学生信息，遍历一个累加初始值
    print("序号    姓名     性别      电话号码")
    i = 1
    # 遍历学生信息列表
    for dict_info in stu_info:
        print("%d    %s    %s     %s" % (i, dict_info["name"],
                    dict_info["sex"], dict_info["phone"]))
        i += 1

# 主程序--根据用户的选择调用不同的函数
def main():
    """
    10分钟完成主程序功能
    0退出，1添加，2删除，3修改，4查询
    :return:
    """
    # 死循环保证用户可以一直选择
    while True:
        # 1.打印目录，供给用户选择
        print_menu()
        # 2.接收用户输入的功能选项，判断选项，调用不同的函数
        key = input("请输入你要选择的功能序号：")
        if key == "1":
            add_stu_indo()
        elif key == "2":
            del_stu_info(stu_info)
        elif key == "3":
            modify_stu_info()
        elif key == "4":
            show_stu_info()
        elif key == "0":
            confirm = input("您是否要退出y/n：")
            if confirm == "y":
                break
            elif confirm == "n":
                print_menu()
            else:
                print("您输入有误")

# 程序的入口，避免导包的时候主程序之间的干扰
if __name__ == '__main__':
    main()




