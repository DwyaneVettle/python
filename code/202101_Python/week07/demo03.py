# author by Michealzou@126.com
# 2022/10/19 10:38
"""
    在控制台中录入，所有学生成绩，输入空字符串，
    打印(一行一个)所有成绩，
    并打印最高分,打印最低分,打印平均分
    max()
    min()
    sum()
"""
list01 = []
while True:
    score = input("请输入学生的成绩：")
    if score == "":
        break
    list01.append(score)
for i in list01:
    print(i)
print("最大值为：" + max(list01))
print("最小值为：" + min(list01))
print("平均值为：" + str(sum(list01) / len(list01)))
