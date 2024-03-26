"""
    在实际的开发中，常常会用到嵌套if
        语法：
            if 条件表达式1
                if 条件表达式1-1：
                    代码块1
                else:
                    代码块2
            else:
                代码块3

        练习：判断用户是否为会员，如果是满足300元打8折
"""
# answer = input("你是会员吗y/n：")
# if answer == 'y':
#     money = int(input("输入你的购物金额："))
#     if money >= 300:
#         print(f"你的购物金额打8折，折后价是{money * 0.8}")
#     else:
#         print("你的购物金额不满足打折！")
# else:
#     print("你不是会员不打折！")
"""
    练习：判断用户是否是学生，如果是，
        判断是2022级，学费6000元
        是2023级，学费8000元
        2021级，学费5000元
"""
answer = input("你是学生吗y/n：")
if answer == 'y':
    grade = input("请输入你的年级2021/2022/2023:")
    if grade == '2021':
        print("你的学费为5000元")
    elif grade == '2022':
        print("你的学费为6000元")
    elif grade == '2023':
        print("你的学费为8000元")
    else:
        print("你不是我校在校学生！")
else:
    print("你不是学生！")
