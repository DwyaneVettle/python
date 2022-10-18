# author by Michealzou@126.com
# 2022/10/18 10:40
# 在控制台中录入，所有学生成绩，输入空字符串，打印(一行一个)所有成绩，
# 并打印最高分,打印最低分,打印平均分
score = []
while True:
    s = int(input("请输入成绩："))
    if s == "":
        break
    score.append(s)
for i in score:
    print(i)
print("--------------")
"""
    max():找到列表最大值，前提列表是数字
    min():最小值
    sum():求和
"""
print(max(score))
print(sum(score) / len(score))
