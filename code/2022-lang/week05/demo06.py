stu_score = []
while True:
    score = input("输入成绩：")
    if score == "":
        break
    stu_score.append(int(score))
for item in stu_score:
    print(item)
print("最高分：", str(max(stu_score)))
print("最低分：", str(min(stu_score)))
print("平均分：", str(sum(stu_score) / len(stu_score)))
