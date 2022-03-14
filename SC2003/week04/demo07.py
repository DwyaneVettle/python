# author by Michealzou@126.com
# 2022/3/14 16:41
# break:终端当前循环
# else配合for或者while循环使用，表示在不喷到break的情况下执行else里的代码块
for i in range(3):
    pwd = int(input("请输入密码："))
    if pwd == 123456:
        print('密码正确！！')
        break
    else:
        print('密码错误！')
else:
    print("今日密码输入次数已经用完，请明天再试！")
