"""
    从键盘录入密码，最多录入3次，如果正确就结束循环
    假设：密码123456
"""
for i in range(0, 3):
    password = input("输入密码：")
    if password == "123456":
        print("密码正确")
        break
    else:
        print("密码不正确")
else:
    print("三次密码皆输入错误，你的次数已经用完")
# 以上逻辑改造为while循环
# i = 0
# while i < 3:
#     password = input("输入密码:")
#     if password == '123456':
#         break
#     i += 1