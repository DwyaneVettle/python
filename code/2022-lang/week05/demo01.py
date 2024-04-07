"""
    break:终止当前循环，不再进行下次循环
    continue:终止当前循环，继续下次循环
"""
# 用户输入密码，当输入到123456不再输入，并提示密码正确
# while True:
#     password = input("请输入密码：")
#     if password == "123456":
#         print("密码正确")
#         break  # break后的语句不再执行
#     else:
#         print("密码不正确")
# 用户输入密码，当输入到123456不再输入，并提示密码正确-输入不能超过3次
# for i in range(3):
#     password = input("请输入密码：")
#     if password == "123456":
#         print("密码正确")
#         break
#     else:
#         print("密码不正确")
# i = 0
# while i < 3:
#     password = input("输入密码：")
#     if password == "123456":
#         print("密码正确")
#         break
#     else:
#         print("密码不正确")

# 练习：遍历0-100之间的所有数，遇到5的倍数时不输出，其他输出到控制台
for i in range(0, 101):
    if i % 5 == 0:
        continue
    print(i)


