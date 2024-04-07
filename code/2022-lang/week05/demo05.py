person = []
while True:
    name = input("输入名字:")
    person.append(name)
    if name == "":
        break
for item in person:
    print(item)
