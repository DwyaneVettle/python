"""
练习2：
在控制台中循环录入学生信息(姓名,年龄,成绩,性别)，
如果名称输入空字符, 则停止录入，将所有信息逐行打印出来。
"""
# student_info = {}
# while True:
#     name = input("输入学生姓名：")
#     if name == '':
#         break
#     age = input("输入年龄：")
#     score = input("输入成绩：")
#     sex = input("输入性别：")
#     student_info[name] = [age, score, sex]
# for name, list_info in  student_info.items():
#     print('%s的年龄是%s,成绩是%s,性别是%s' % (name, list_info[0], list_info[1], list_info[2]))

# 字典嵌套字典
# student_info = {}
# while True:
#     name = input("请输入学生姓名:")
#     if name == '':
#         break
#     age = input("请输入年龄:")
#     score = input("请输入成绩:")
#     sex = input("请输入性别:")
#     student_info[name] = {'age' : age, 'score' : score, 'sex' : sex}
# for name, dict_info in student_info.items():
#     print('%s的年龄是%s,成绩是%s,性别是%s' % (name, dict_info['age'], dict_info['score'], dict_info['sex']))
# 列表内嵌字典
student_info = []
while True:
    name = input("请输入学生姓名:")
    if name == '':
        break
    age = input("请输入年龄:")
    score = input("请输入成绩:")
    sex = input("请输入性别:")
    dict_info = {'name' : name, 'age' : age, 'score' : score, 'sex' : sex}
    student_info.append(dict_info)
for dict_info in student_info:
    print('%s的年龄是%s,成绩是%s,性别是%s' % (dict_info['name'], dict_info['age'], dict_info['score'], dict_info['sex']))