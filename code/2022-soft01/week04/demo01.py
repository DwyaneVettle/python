"""
    break:中断当前循环，不会继续循环
    continue：中断循环，开始下一个循环
    for、while能配合else语句使用
"""
for i in range(3):
    password = input("请输入密码：")
    if password == '123456':
        print("密码正确")
        break
    else:
        print("密码不正确")
else:
    print("你输入的密码错误3次，被锁卡")
# i = 0
# while i < 3:
#     password = input("请输入密码：")
#     if password == '123456':
#         print("密码正确")
#         break
#     else:
#         print("密码不正确")
#     i += 1

# 1-50之间5的倍数
# for i in range(1, 51):
#     if i % 5 != 0:
#         continue
#     print(i)
