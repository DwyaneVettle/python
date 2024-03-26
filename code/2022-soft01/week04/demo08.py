"""
    在控制台中录入，所有学生姓名，如果姓名重复，则提示"姓名已经存在",
    不添加到列表中，如果录入空字符串，则倒序打印所有学生。
"""
stu_list = []
while True:
    stu = input("输入学生姓名：")
    if stu == "":
        break
    if stu not in stu_list:
        stu_list.append(stu)
    else:
        print("姓名已经存在")

for item in range(-1, -len(stu_list) - 1, -1):
    print(stu_list[item])
