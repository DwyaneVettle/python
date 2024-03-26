"""
    多分枝结构：
        if 条件表达式1:
            代码块1
        elif 条件表达式2:
            代码块2
        elif 条件表达式3:
            代码块3
        ...
        else:
            代码块n

    练习：根据学生的分数判断期末评定
        90-100：优
        80-89:良
        70-79：中
        60-69：差
        0-59：不及格

"""
score = int(input("请输入你的期末分数："))
if 90 <= score <= 100:
    print("你的成绩为优")
elif 80 <= score <= 89:
    print("你的成绩为良")
elif 70 <= score <= 79:
    print("你的成绩为中")
elif 60 <= score <= 69:
    print("你的成绩为差")
elif 0 <= score <= 59:
    print("你的成绩为不及格")
else:
    print("你输入的分数不合法")
