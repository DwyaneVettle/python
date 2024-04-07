list_stu = []
while True:
    name = input("输入姓名：")
    if name == "":
        break
    elif name not in list_stu:
        list_stu.append(name)
    else:
        print("姓名已经存在了")
# 1 2 3 -1 -2 -3
for i in range(-1, -len(list_stu) - 1, -1):
    print(list_stu[i])

