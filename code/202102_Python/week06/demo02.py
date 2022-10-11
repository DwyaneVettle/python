# author by Michealzou@126.com
# 2022/10/11 9:02
"""
    模拟去银行取钱，输入密码
    加入密码123456提示成功，
    输入超过三次提示锁卡
    break：终止当前的判断,不再继续执行下面的代码，和if配合使用
"""
# 1.接收用户输入的密码，用input()接收的全部是字符串
# for i in range(3):
#     pwd = input("请输入密码：")
#     # print(type(pwd))
#     if pwd == '123456':
#         print("密码正确")
#         break
#     else:
#         print("密码不正确")
# # for循环也可以配合else循环语句执行，当for配置else时，没有遇到break语句，
# # 就会执行else语句
# else:
#     print("三次输入均错误，已被锁卡，请联系管理员!")



# 将上面的代码改造成while循环
i = 0
while i < 3:
    pwd = input("请输入密码：")
    # print(type(pwd))
    if pwd == '123456':
        print("密码正确")
        break
    else:
        print("密码不正确")
        i += 1
else:
    print("三次输入均错误，已被锁卡，请联系管理员!")
