# author by Michealzou@126.com
# 2022/10/18 10:08
# 在控制台中录入，西游记中你喜欢的人物，当输入空字符串，打印(一行一个)所有人物
xiyouji = []
while True:
    str01 = input("人物：")
    if str01 == "":
        break
    xiyouji.append(str01)

for i in xiyouji:
    print(i)
