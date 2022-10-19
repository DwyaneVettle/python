# author by Michealzou@126.com
# 2022/10/19 11:35
"""
    将列表[54,25,12,42,35,17]中，
    大于30的数字存入另外一个列表，并画出内存图
"""
list01 = [54, 25, 12, 42, 35, 17]
list02 = []
for item in list01:
    # print(item)
    if item > 30:
        list02.append(item)
for i in list02:
    print(i)
