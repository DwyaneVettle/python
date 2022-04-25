# author by Michealzou@126.com
# 2022/4/19 9:18
def weather():
    print("日期：4月20日")
    print("温度：10-28℃")
    print("空气状况：良")


weather()


def m_weather(today, temp, air):
    """
    :param today:
    :param temp:
    :param air:
    """
    print(f"日期：{today}")
    print(f"温度：{temp}")
    print(f"空气质量：{air}")


m_weather("4月20号", "20℃", "优")


def print_rectangle(r_count, c_count, char):
    """
        打印三角形
    :param r_count: 行数
    :param c_count: 列数
    :param char: 填充的字符　
    """
    for r in range(r_count, c_count):
        # 内层循环控制列　
        for c in range(r):
            print(char, end=" ")
        print()


print_rectangle(c_count=5, r_count=1, char="*")
