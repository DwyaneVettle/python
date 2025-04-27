"""
    练习：根据用户输入的月份数（1-12），打印这个月有多少天
"""
# 第一种方式：把月份放到元组中
month = int(input("请输入月份:"))
# if month < 1 or month > 12:
#     print("您输入的月份有误！")
# elif month in (1, 3, 5, 7, 8, 10, 12):
#     print("这个月有31天")
# elif month in (4, 6, 9, 11):
#     print("这个月有20天")
# else:
#     print("这个月有28天")
# 第二种：把天数放到元组中
if month < 1 or month > 12:
    print("您输入的月份有误！")
else:
    days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    print("这个月有%d天" % days[month - 1])
