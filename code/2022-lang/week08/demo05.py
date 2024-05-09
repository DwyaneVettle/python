"""
    作用域
        局部作用域-函数内部有效
        外部嵌套作用域-函数嵌套
        全局作用域-global  .py
        内置模块作用域-builtins.py
        作用域提升：如果要想让函数内部的变量成为全局变量？
        使用关键字global来完成函数内部变量作用域的提升
        global的使用是先定义再赋值,但并不能将该变量传递到函数之外
        只能在各个函数内部使用global定义的变量
"""
# a = 200  # 全局变量,在整个.py文件内部有效
# def fun01():
#     a = 100  # 函数外部嵌套
#     print(a)
#     def fun02():
#         a = 300  # 局部变量-只能在函数内部有效
#         print(a)
#
#     fun02()
#
# print(a)
# fun01()


def fun03():
    global a
    a = 100
    print(a)
def fun04():
    print(a)
fun03()
fun04()
