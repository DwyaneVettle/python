# author by Michealzou@126.com
# 2022/10/12 9:47
"""
    模拟ATM取钱输入密码，当密码三次输入都错误的时候，锁卡
    密码输入正确，提示密码正确
    break可以终端当前的程序,常在循环语句中配合if语句使用
    python的基础数据类型：整型(int)，浮点型(float)
                    布尔型(bool)，字符串(str)
                    int()
                    float()
                    str()
                    bool()
    while循环：
        1.定义一个初始化变量
        2.循环条件
        3.执行循环体
        4.初始化变量变化
"""
i = 1
# 定义初始化密码
init_pwd = "123456"
while i <= 3:
    # 接收用户输入的密码
    pwd = input("请输入密码：")
    if pwd == init_pwd:
        print("密码正确")
        break
    else:
        print("密码不正确")
    i = i + 1
else:
    print("你已锁卡，请联系管理员！")
