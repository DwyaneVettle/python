"""
练习:在控制台中录入多个人的多个喜好,输入空字符停止.
例如:请输入姓名：
    请输入第1个喜好：
    请输入第2个喜好：
    ...
    请输入姓名：
    ...
   最后在控制台打印所有人的所有喜好.
[
    {“无忌”:[赵敏,周芷若,小赵]}
]
"""
person_hobby = []
while True:
    name = input("输入姓名：")
    if name == '':
        break
    dict_person = {name: []}
    person_hobby.append(dict_person)
    while True:
        hobby = input("请输入喜好：")
        if hobby == '':
            break
        dict_person[name].append(hobby)
print(person_hobby)