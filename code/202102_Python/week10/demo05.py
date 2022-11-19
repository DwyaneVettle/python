# author by Michealzou@126.com
# 2022/11/8 10:23
# 定义天气函数
def weather():
    print("今天天气：阴天")
    print("今天温度：15℃")
    print("空气状况:差")

weather()


def my_weather(today, temp, air):
    """
    定义天气的函数
    :param today:  今天的天气，例：晴天
    :param temp:  今天的温度，例：15℃
    :param air:   今天的天气状况，例：优
    :return:
    """
    print(f"今天天气：{today}")
    print(f"今天温度：{temp}")
    print(f"空气状况:{air}")


my_weather("晴天", "15℃", "差")
my_weather("阴天", "10℃", "中")
