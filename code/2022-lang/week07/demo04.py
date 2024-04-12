# 在控制台中循环录入字符串，输入空字符串停止，打印所有不重复的文字
set01 = set()
while True:
    str01 = input("输入字符串：")
    if str01 == "":
        break
    set01.add(str01)
for i in set01:
    print(i)
