"""
    双分支：
        if 条件表达式 :
            条件执行体1
        else :
            条件执行体2
        如果条件表达式满足，就执行条件执行体1
        条件表达式不满足.....就执行条件执行2

"""
grade = int(input("请输入成绩："))
if grade >= 90:
    print("优秀")
else:
    print("不优秀")

# 练习：接收用户输入的整数，判断这个数是奇数还是偶数
num = int(input("请输入一个整数："))
# if num % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")
if num % 2 != 0:
    print("奇数")
else:
    print("偶数")
