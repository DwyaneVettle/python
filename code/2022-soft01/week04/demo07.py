"""
    在控制台中录入，所有学生成绩，输入空字符串，
    打印(一行一个)所有成绩，并打印最高分,打印最低分,打印平均分
"""
stu_score = []
while True:
    score = input("请输入成绩：")
    if score == "":
        break
    stu_score.append(int(score))
for item in stu_score:
    print(item)

print("最高分为:" + str(max(stu_score)))
print("最低分为:" + str(min(stu_score)))
print("平均分为:" + str(sum(stu_score) / len(stu_score)))

