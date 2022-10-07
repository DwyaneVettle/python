# author by Michealzou@126.com
# 2022/10/4 9:16
"""
案例：
    根据学生的得分进行判断
    1.90-100 优
    2.80-89  良
    3.70-79  差
    4.60-69  及格
    5.<60  不及格
"""
score = float(input("请输入你的分数："))
if 90 <= score <= 100:
    print("你的成绩为优")
elif 80 <= score <= 89:
    print("你的成绩为良")
elif 70 <= score <= 79:
    print("你的成绩为差")
elif 60 <= score <= 69:
    print("你的成绩为及格")
elif score < 0 or score > 100:
    print("你输入的成绩不合法")
else:
    print("你的成绩为不及格")
