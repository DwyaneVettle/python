"""
使用自定义函数，完成对程序的模块化
学生信息包含：姓名、性别、手机号
该系统具有的功能：添加、删除、修改、显示、退出系统
设计思路：
提示用户选择功操作
获取用户选择的功能
根据用户的选择，分别调用不同的函数
"""
# 初始化一个列表，用来保存学生所有的信息
stu_info = []
# 功能菜单的打印
def print_menu():
    print('=' * 30)
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.显示所有学生信息')
    print('0.退出系统')
    print('=' * 30)

# 添加学生信息
def add_stu_info():
    # 接收用户输入的学生信息-姓名、性别、手机号
    new_name = input('请输入学生姓名：')
    new_sex = input('请输入学生性别：')
    new_phone = input('请输入电话号码：')
    # 列表嵌套字典，将学生信息保存到字典中
    new_info = dict()
    new_info['name'] = new_name
    new_info['sex'] = new_sex
    new_info['phone'] = new_phone
    # 将字典中学生信息添加到列表中
    stu_info.append(new_info)


# 删除学生信息-参数student是一个学生对象
def del_stu_info(student):
    # 提示用户输入学生对应的序号删除
    deL_num = int(input('请输入学生对应的编号删除：'))
    del student[deL_num - 1]
    print('删除成功！')


# 修改学生信息
def modify_stu_info():
    # 判断列表中是否有学生信息
    if len(stu_info) != 0:
        # 获取学生序号来修改
        stu_id = int(input('请输入学生的序号：'))
        new_name = input('请输入学生姓名：')
        new_sex = input('请输入学生性别：')
        new_phone = input('请输入电话号码：')
        stu_info[stu_id - 1]['name'] = new_name
        stu_info[stu_id - 1]['sex'] = new_sex
        stu_info[stu_id - 1]['phone'] = new_phone
    else:
        print('学生信息列表为空，请先添加后再修改！')


# 显示所有学生信息
def show_stu_info():
    print("学生信息如下：")
    print("=" * 30)
    print("序号\t姓名\t性别\t电话")
    # 初始化序号
    i = 1
    for temp_info in stu_info:
        print("%d\t%s\t%s\t%s" % (i, temp_info['name'], temp_info['sex'], temp_info['phone']))
        i += 1


# 主函数
def main():
    # 循环打印菜单，获取用户选择的功能
    while True:
        print_menu()
        key = input('请输入功能菜单序号：')
        # 根据用户选择的功能，分别调用不同的函数
        if key == '1':
            add_stu_info()
        elif key == '2':
            del_stu_info(stu_info)
        elif key == '3':
            modify_stu_info()
        elif key == '4':
            show_stu_info()
        elif key == '0':
            quit_confirm = input('真的对出系统吗？yes or no：')
            if quit_confirm == 'yes':
                break
            else:
                print('继续使用系统！')
                print_menu()
        else:
            print('你输入的功能序号有误，请重新输入！')


if __name__ == '__main__':
    main()
