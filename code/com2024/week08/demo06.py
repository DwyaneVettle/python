"""
    练习1：在控制台中录入，
    西游记中你喜欢的人物，当输入空字符串，打印(一行一个)所有人物
"""
# 1.定义一个空的列表用于保存所有的人物
# list_person = []
# # 2.循环录入姓名
# while True:
#     str_name = input("输入你喜欢的西游记人物：")
#     if str_name == "":
#         break
#     # 把人物添加到列表中
#     list_person.append(str_name)
# for item in list_person:
#     print(item)

"""
    练习2：在控制台中录入，所有学生成绩，输入空字符串停止录入
    打印(一行一个)所有成绩，并打印最高分,打印最低分,打印平均分
"""
# stu_score = []
# while True:
#     score = int(input("请输入分数："))
#     if score == "":
#         break
#     stu_score.append(score)
# for item in stu_score:
#     print(item)
# print("最高分是：" + str(max(stu_score)))
# print("最低分是：" + str(min(stu_score)))
# print("平均分是：" + str(sum(stu_score) / len(stu_score)))
"""
    练习3： 在控制台中录入，所有学生姓名，如果姓名重复，则提示"姓名已经存在",
    不添加到列表中，如果录入空字符串，则倒叙打印所有学生。
"""