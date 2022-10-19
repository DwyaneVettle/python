# author by Michealzou@126.com
# 2022/10/19 10:04
"""
    在控制台中录入，西游记中你喜欢的人物，
    当输入空字符串，打印(一行一个)所有人物
"""
person_info = []
while True:
    person = input("请输入西游记中你喜欢的人物：")
    if person == "":
        break
    person_info.append(person)

for i in person_info:
    print(i)
