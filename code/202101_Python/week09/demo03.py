# author by Michealzou@126.com
# 2022/11/2 9:47
"""
    练习：
        输入学生信息，姓名、年龄、成绩、性别
        当输入空字符串的时候停止录入
        打印所有的信息
        {姓名:[年龄、成绩、性别]}
        [{姓名:name},{年龄:age}]
"""
dict_student_info = {}
while True:
    name = input("请输入学生姓名:")
    if name == "":
        break
    age = int(input("请输入年龄:"))
    score = input("请输入成绩:")
    sex = input("请输入性别:")
    dict_student_info[name] = [age, score, sex]

for key, value in dict_student_info.items():
    print("%s的年龄是%d,成绩是%s,性别是%s" % (key, value[0], value[1], value[2]))
