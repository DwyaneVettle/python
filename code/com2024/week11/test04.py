"""
练习：定义函数，根据小时分钟秒，计算总秒数
要求：可以计算小时-->秒，也可以分钟-->秒
可以计算小时+分钟-->秒，也可以计算小时+秒-->秒
"""
# 已缺省传参定义函数
def get_total_second(hour = 0, minute = 0, second = 0):
    return hour * 3600 + minute * 60 + second

# 小时 分钟 秒
print(get_total_second(1, 1, 50))
# 分钟
print(get_total_second(minute=50))
# 小时 分钟
print(get_total_second(hour=1, minute=50))
# 小时  秒
print(get_total_second(hour=1, second=25))

# 练习：定义求数值相加的函数，需求：数值的个数不确定
def add(*args):
    # # 初始化求和变量：
    # result = 0
    # for item in args:
    #     result += item
    # return result
    return sum(args)

print(add(1, 2, 3, 4))
print(add(1, 2))
