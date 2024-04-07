# 根据用户输入的月份数，输出当月有多少天
# month = int(input("请输入月份："))
# if 1 > month or month > 12:
#     print("输入的月份有误")
# elif month == 2:
#     print("当月有28天")
# elif month in (1, 3, 5, 7, 8, 10, 12):
#     print("当月有31天")
# else:
#     print("当月有30天")


month = int(input("请输入月份："))
if 1 > month or month > 12:
    print("输入的月份有误")
else:
    day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    print(f"{month}月有{day_of_month[month - 1]}天")
