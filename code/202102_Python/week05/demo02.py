# author by Michealzou@126.com
# 2022/10/4 9:01
# 根据用户输入的用户名密码进行验证，如果用户名等于admin,密码等于123456，验证通过
username = input("请输入用户名:")
passwd = input("请输入密码:")
sex = input("请输入性别:")
if username == "admin" and passwd == "123456" or sex == 'man':
    print("验证成功！")
else:
    print("验证失败！")
