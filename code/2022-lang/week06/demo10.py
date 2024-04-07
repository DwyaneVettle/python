"""
    在控制台中循环录入学生信息(姓名,年龄,成绩,性别)，
    如果姓名输入空字符, 则停止录入，将所有信息逐行打印出来
"""
info = {}
while True:
    name = input("录入姓名：")
    if name == "":
        break
    age = input("录入年龄：")
    score = input("录入成绩：")
    gender = input("录入性别：")
    info[name] = [age, score, gender]
for key, value in info.items():
    print(f"{key}的年龄是{value[0]}，成绩是{value[1]}，性别是{value[2]}")
    #print(key)
    # print(value)
# 字典+字典  列表+字典
