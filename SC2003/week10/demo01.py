# author by Michealzou@126.com
# 2022/4/25 14:14
# 控制台输入任意字符，存入集合中，直到""停止 while True:
set01 = set()
while True:
    str_input = input("请输入任意字符：")
    if str_input == "":
        break
    set01.add(str_input)

print(set01)
