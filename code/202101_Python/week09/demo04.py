# author by Michealzou@126.com
# 2022/11/2 10:24
"""
    练习：
        输入学生信息，姓名、年龄、成绩、性别
        当输入空字符串的时候停止录入
        打印所有的信息
        [{姓名:name},{年龄:age},{成绩:score},{性别:sex}]

"""
list_student_info = []
while True:
    name = input("请输入学生姓名:")
    if name == "":
        break
    age = int(input("请输入年龄:"))
    score = input("请输入成绩:")
    sex = input("请输入性别:")
    dict_info = {"姓名": name, "年龄": age, "成绩": score, "性别": sex}
    list_student_info.append(dict_info)

for key in list_student_info:
    print("%s的年龄是%d,成绩是%s,性别是%s" % (dict_info["姓名"], dict_info["年龄"],dict_info["成绩"],dict_info["性别"]))


# {name:{年龄:age,成绩:score,性别:sex}}
list_student_info = {}
while True:
    name = input("请输入学生姓名:")
    if name == "":
        break
    age = int(input("请输入年龄:"))
    score = input("请输入成绩:")
    sex = input("请输入性别:")
    list_student_info[name] = {"年龄":age,"成绩":score,"性别":sex}

for key, dict_info in list_student_info:
    print("%s的年龄是%d,成绩是%s,性别是%s" % (name, dict_info["年龄"],dict_info["成绩"],dict_info["性别"]))
