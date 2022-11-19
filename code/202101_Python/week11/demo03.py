# author by Michealzou@126.com
# 2022/11/16 9:46
# 变量在函数中的作用域
"""
    Python中作用域的大小
        B>G>L>E
    global:定义全局作用域，必须先声明再赋值
"""

global g01
def fun01():
    # 在函数内部声明的变量是局部变量，只能在函数内部有作用
    l01 = "java"
    g01 = "c#"
    # print(l01)
    # print(g01)
    # print(l02)
    def fun02():
        l02 = "php"

fun01()
print(g01)

