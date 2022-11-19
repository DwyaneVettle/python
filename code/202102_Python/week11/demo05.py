# author by Michealzou@126.com
# 2022/11/15 9:53
"""
    根据给定时分秒--转换成总秒数
    时--> 秒
    时分-->秒
    时分秒-->秒
    时秒-->秒
    分秒-->秒
"""

# 关键字实参传递值
# 1.定义形参的初始值
def get_total_sec(h=0, m=0, s=0):
    return h * 3600 + m * 60 + s


total_sec01 = get_total_sec(100, 10, 20)
print(total_sec01)

total_sec02 = get_total_sec(h=100, s=10)
print(total_sec02)
