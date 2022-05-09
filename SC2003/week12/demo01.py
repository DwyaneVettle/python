# author by Michealzou@126.com
# 2022/5/9 14:12
# 变量的作用域
"""
1.局部变量：只在函数内部生效，当函数调用创建，结束调用，变量销毁，
    能很好的管理内存
2.全局变量：能在整个py文件中生效，独立与函数的内存空间，不会随着函数调用结束而销毁
    生命全局变量，使用global关键字
"""


def fun01():
    # 局部变量
    name = 'python'
    # 函数内部打印
    print(name)


fun01()


# 函数外部打印局部变量，变量已经被销毁
# print(name)  NameError: name 'name' is not defined


def fun02():
    # 生命全局变量不能直接复制
    global name01
    name01 = 'python'
    print(name01)


fun02()
print(name01)


def fun03():
    print(name01)


fun03()
