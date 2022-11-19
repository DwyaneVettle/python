# author by Michealzou@126.com
# 2022/11/9 10:47
"""
    为什么要在函数中使用参数？
"""
# 定义函数
def weather():
    print("今天是：阴天")
    print("今天的温度：15℃")
    print("今天空气状况：差")
# 调用函数
weather()


def weather(day, temp, air):
    print(f"今天是：{day}")
    print(f"今天的温度：{temp}")
    print(f"今天空气状况：{air}")
# 调用函数
weather("晴天", "20℃", "差")
weather("下雨天", "10", "好")

