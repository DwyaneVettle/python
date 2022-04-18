# author by Michealzou@126.com
# 2022/4/18 16:57
# 函数:将业务封装，实现分而治之
# def 函数名()
def add():
    num1 = int(input("请输入num1:"))
    num2 = int(input("请输入num2:"))
    result = num1 + num2
    print(result)
# 调用函数，直接通过函数名来调用就可以
add()

# 练习：将月份天数的练习函数化
# def month():
#     input_month = int(input("请输入月份："))
#     if input_month < 1 or input_month > 12:
#         print("您输入的月份无效")
#     else:
#         day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#         print(day[input_month - 1])
#
# month()