# author by Michealzou@126.com
# 2022/10/5 9:51
"""
多分支：
    if 条件表达式1:
        代码块1
    elif 条件表达式2:
        代码块2
    elif 条件表达式N:
        代码块N
    else:
        代码块N+1
案例：
    根据学生输入的分数进行判断：
        1.90-100 优
        2.80-89  良
        3.70-79  中
        4.60-69  及格
        5.60以下  不及格
"""
score = float(input("请输入您的分数:"))
if 90 <= score <= 100:
    print(f"您的成绩为{score},为优")
elif 80 <= score <= 89:
    print(f"您的成绩为{score},为良")
elif 70 <= score <= 79:
    print(f"您的成绩为{score},为中")
elif 60 <= score <= 69:
    print(f"您的成绩为{score},为及格")
elif score > 100 or score < 0:
    print("您输入的成绩不合格！")
else:
    print(f"您的成绩为{score},为不及格")
