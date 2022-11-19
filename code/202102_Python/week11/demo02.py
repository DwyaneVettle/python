# author by Michealzou@126.com
# 2022/11/15 9:21
# 全局作用域：整个py文件中有用
l02 = "hello"
def fun01():
    # 局部作用域：只在函数内部游泳
    l01 = 100
    # 定义全局变量的关键字global
    global l02
    l02 = 100 # 局部变量
    print(l01)

fun01()
print(l02)  # 100
