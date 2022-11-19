# author by Michealzou@126.com
# 2022/11/9 9:26
# 在控制台中循环录入字符串，输入空字符串停止，打印所有不重复的文字
# 1.初始化空集合
set01 = set()
# 2.循环录入
while True:
    str01 = input("请输入字符串：")
    # 3.停止的条件
    if str01 == "":
        break
    # 4.存放字符串
    set01.add(str01)
for i in set01:
    print(i)
