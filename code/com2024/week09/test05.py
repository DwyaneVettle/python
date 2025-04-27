"""
列表综合练习：
1.将列表[54,25,12,42,35,17]中，大于30的数字存入另外一个列表中
2.在控制台中录入５个数字，打印最大值（不使用max）
3.在列表中[54, 25, 12, 42, 35, 17]，选出最大值(不使用max)
"""
#  1.将列表[54,25,12,42,35,17]中，大于30的数字存入另外一个列表中
# list01 = [54,25,12,42,35,17]
# list02 = []
# for item in list01:
#     if item > 30:
#         list02.append(item)
# print(list02)
# 2.在控制台中录入５个数字，打印最大值（不使用max）
# max_num = 0
# for i in range(5):
#     number = int(input("请输入第%d个数字：" % (i + 1)))
#     if max_num < number:
#         max_num = number
# print(max_num)

# 3.在列表中[54, 25, 12, 42, 35, 17]，选出最大值(不使用max)
list01 = [54, 25, 12, 42, 35, 17]
max_num = list01[0]  # 假设列表里的第一个元素为最大值
for item in list01:
    if max_num < item:
        max_num = item
print(max_num)


