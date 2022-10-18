# author by Michealzou@126.com
# 2022/10/12 9:10
"""
    模拟ATM取钱输入密码，当密码三次输入都错误的时候，锁卡
    密码输入正确，提示密码正确
    break可以终端当前的程序,常在循环语句中配合if语句使用
"""
# 初始化密码
init_pwd = "123456"
for i in range(3):
    # 1.接收用户输入的密码
    pwd = input("请输入密码：")
    # print(type(pwd))  字符串类型
    # 判断用户输入的密码是否正确
    if pwd == init_pwd:
        print("密码正确")
        break
    else:
        print("密码不正确")
# 当else语句和for，while一起使用时，没有碰到break语句，就会执行
# else语句的代码
else:
    print("你已锁卡，请联系管理员！")
