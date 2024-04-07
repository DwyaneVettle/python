"""
    将列表[54,25,12,42,35,17]中，大于30的数字存入另外一个列表
"""
list01 = [54, 25, 12, 42, 35, 17]
list02 = []
for i in list01:
    # print(i)
    if i > 30:
        list02.append(i)
print(list02)  # [54, 42, 35]
