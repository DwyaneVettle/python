# author by Michealzou@126.com
# 2022/3/7 17:12
# 输入成绩，大于90为优，80-90为良，70-79为中，70以下为差
score = int(input("请输入成绩："))
if score > 90:
    print("您的成绩为优")
elif 80 <= score <= 90:
    print('您的成绩为良')
elif 70 <= score <= 79:
    print('您的成绩为中')
elif 0 > score:
    print('您的成绩不合法')
else:
    print('您的成绩为差')
