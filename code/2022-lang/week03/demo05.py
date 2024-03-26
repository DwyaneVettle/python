"""
多分支：
            if 条件表达式1:
                代码块1
            elif 条件表达式2:
                代码块2
            elif 条件表达式n:
                代码块n
            else:
                代码块
        练习：
            接收学生输入的分数
            如果分数在90-100之间，输出优
            80-89之间，输出良
            70-79--中
            60-69--差
            0-59--不及格

"""
score = int(input("请输入分数："))
if 90 <= score <= 100:
    print("你的成绩为优")
elif 80 <= score <= 89:
    print("你的成绩为良")
elif 70 <= score <= 79:
    print("你的成绩为中等")
elif 60 <= score <= 69:
    print("你的成绩为差")
elif 0 <= score <= 59:
    print("你的成绩为不及格")
else:
    print("你的成绩无效")
