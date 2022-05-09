# author by Michealzou@126.com
# 2022/5/9 12:50
def fun01():
    # 局部变量
    global name
    name = 'python'
    # 内部访问
    print(name)

fun01()
# 外部访问局部变量报错
print(name)


def fun02():
    print(name)
# 其他函数也能访问全局变量
fun02()

