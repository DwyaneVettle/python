"""
    在控制台中循环录入学生信息(姓名,年龄,成绩,性别)，如果名称输入空字符,
    则停止录入，将所有信息逐行打印出来。
"""
stu = {}
while True:
    name = input("请输入学生的姓名：")
    if name == "":
        break
    age = int(input("请输入年龄:"))
    score = int(input("请输入成绩:"))
    sex = input("请输入性别:")
    stu[name] = [age, score, sex]
for name, list01 in stu.items():
    print(f'{name}的年龄是{list01[0]},成绩是{list01[1]},性别是{list01[2]}')

"""
    {
    "张无忌":{"age":28,"score":100,"sex":"男"},
    }    
"""
stu = {}
while True:
    name = input("请输入学生的姓名：")
    if name == "":
        break
    age = int(input("请输入年龄:"))
    score = int(input("请输入成绩:"))
    sex = input("请输入性别:")
    stu[name] = {"age": age, "score": score, "sex": sex}
for name, dict01 in stu.items():
    print(f'{name}的年龄是{dict01["age"]},成绩是{dict01["score"]},性别是{dict01["sex"]}')

"""
    [
        {"name":"张无忌","age":28,"score":100,"sex":"男"},
    ]
"""
stu = []
while True:
    name = input("请输入学生的姓名：")
    if name == "":
        break
    age = int(input("请输入年龄:"))
    score = int(input("请输入成绩:"))
    sex = input("请输入性别:")
    dict02 = {"name": name, "age": age, "score": score, "sex": sex}
    stu.append(dict02)
for stu_info in stu:
    print(
        "%s的年龄是%d,成绩是%d,性别是%s" % (stu_info["name"], stu_info["age"], stu_info["score"], stu_info["sex"]))
    # 获取第一个学生信息
stu_info = stu[0]
print("第一个录入的是：%s,年龄是%d,成绩是%d,性别是%s" % (
stu_info["name"], stu_info["age"], stu_info["score"], stu_info["sex"]))
