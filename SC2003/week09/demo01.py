# author by Michealzou@126.com
# 2022/4/18 14:23
# 元组的练习：
"""
需求：根据用户输入的月份打印出这个月有多少天
"""
# input_month = int(input("请输入月份："))
# if input_month < 1 or input_month > 12:
#     print("您输入的月份无效")
# elif input_month == 2:
#     print(f"{input_month}月有28天")
# elif input_month == 1 or input_month == 3 or input_month == 5 or input_month == 7 or input_month == 8 or input_month == 10 or input_month == 12:
#     print(f"{input_month}月有31天")
# else:
#     print(f"{input_month}月有30天")

# 用元组优化以上代码
# 1.用月份优化的方式
# input_month = int(input("请输入月份："))
# if input_month < 1 or input_month > 12:
#     print("您输入的月份无效")
# elif input_month == 2:
#     print(f"{input_month}月有28天")
# elif input_month in (1,3,5,7,8,10,12):
#     print(f"{input_month}月有31天")
# else:
#     print(f"{input_month}月有30天")

# 2.将天数放元组中进行输入
input_month = int(input("请输入月份："))
if input_month < 1 or input_month > 12:
    print("您输入的月份无效")
else:
    day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    print(day[input_month - 1])
