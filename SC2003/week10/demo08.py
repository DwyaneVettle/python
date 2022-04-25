# author by Michealzou@126.com
# 2022/4/25 16:34
# 定义一个函数，可以动态的根据传入的时分秒来转换成秒
def get_seconds(hour=0, minute=0, second=0):
    # result = hour * 3600 + minute * 60 + second
    # print(result)
    return hour * 3600 + minute * 60 + second


print(get_seconds(1, 2, 3))
print(get_seconds(10, 10))
print(get_seconds(minute=10,second=10))
