# 在控制台中录入，西游记中你喜欢的人物，当输入空字符串，打印(一行一个)所有人物
list_person = []
while True:
    person = input("请输入你喜欢的西游记人物：")
    list_person.append(person)
    if person == "":
        break
for item in list_person:
    print(item)
