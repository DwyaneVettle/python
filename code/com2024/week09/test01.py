"""
练习3： 在控制台中录入，所有学生姓名，如果姓名重复，则提示"姓名已经存在",
不添加到列表中，如果录入空字符串，则倒叙打印所有学生。
for item in range(-1,-len()-1,-1)
"""
# 初始化保存学生的列表
students = []
while True:
    name = input("请输入学生姓名：")
    if name == '':
        break
    if name in students:
        print("姓名已经存在")
    else:
        students.append(name)
print(students)
for item in range(-1, -len(students)-1, -1):
    print(students[item])
