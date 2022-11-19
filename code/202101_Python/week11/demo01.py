# author by Michealzou@126.com
# 2022/11/16 8:39
# author by Michealzou@126.com
# 2022/10/5 9:51
def score_check(score):
    if 90 <= score <= 100:
        return "优"
    elif 80 <= score <= 89:
        return "良"
    elif 70 <= score <= 79:
        return "中"
    elif 60 <= score <= 69:
        return "差"
    elif score > 100 or score < 0:
        return "您输入的成绩不合格！"
    else:
        return "不及格"

check = score_check(190)
print(check)
