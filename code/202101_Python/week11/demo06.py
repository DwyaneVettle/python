# author by Michealzou@126.com
# 2022/11/16 10:47
"""
    练习：给定时分秒，转换成总秒数
    时分秒不确定：时分、时秒、分秒、时分秒
"""
def total_sec(h=0, m=0, s=0):
    """
    这是一个求总秒数的函数
    :param h: 小时
    :param m: 分钟
    :param s:秒
    :return: 总秒数
    """
    return h*3600 + m*60 + s


print(total_sec(1, 1, 1))
print(total_sec(h=1, m=1))