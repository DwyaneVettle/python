"""
    在控制台中录入５个数字，打印最大值（不使用max）
"""
# 不用列表
# max = 0
# for i in range(0, 5):
#     number = int(input(f"输入数值{i+1}:"))
#     if number > max:
#         max = number
# print(f"最大数值为{max}")

# 使用列表
# list01 = []
# for i in range(0, 5):
#     number = int(input(f"输入数值{i + 1}:"))
#     list01.append(number)
# print("最大数为：" + str(max(list01)))

# 在列表中[54, 25, 12, 42, 35, 17]，选出最大值(不使用max)
list01 = [54, 25, 12, 42, 35, 17]
max = 0
for i in list01:
    if i > max:
        max = i
print(max)
