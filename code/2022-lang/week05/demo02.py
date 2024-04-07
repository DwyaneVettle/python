"""
    else语句：不仅可以和if配合使用，还可以和for循环一起使用
    表示当循环结束时，需要操作的业务
"""
for i in range(3):
    password = input("请输入密码：")
    if password == "123456":
        print("密码正确")
        break
    else:
        print("密码不正确")
else:
    print("你输入密码的次数已耗尽")
