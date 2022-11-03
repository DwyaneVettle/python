# author by Michealzou@126.com
# 2022/11/1 9:37
"""
    案例：
    录入学生信息（姓名、年龄、成绩、性别）
    当录入空字符串时，停止录入，
    并打印所有信息
    {姓名: [年龄，成绩，性别]}
"""
# 1.创建字典保存数据
list_student_info = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    list_student_info[name] = [age, score, sex]

for name, dict_info in list_student_info.items():
    print("%s的年龄%d,成绩是%d,性别是%s" % (name, dict_info[0], dict_info[1], dict_info[2]))


"""
   { 姓名: {age:年龄，score:成绩，sex:性别}}
"""
list_student_info = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    list_student_info[name] = {"age": age, "score": score, "sex": sex}

for name, dict_info in list_student_info.items():
    print("%s的年龄%d,成绩是%d,性别是%s" % (name, dict_info["age"], dict_info["score"], dict_info["sex"]))

"""
[
   { name:姓名,age:年龄,score:成绩,sex:性别}
]
"""
list_student_info = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    dict_info = {"name":name, "age": age, "score": score, "sex": sex}
    list_student_info.append(dict_info)

for dict_info in list_student_info:
    print("%s的年龄%d,成绩是%d,性别是%s" % (dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))

