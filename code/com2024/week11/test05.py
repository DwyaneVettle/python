"""
    函数作用域：函数内部变量的有效范围
    Python函数变量范围：内部作用<嵌套作用<全局作用<内置模块
"""
# 局部作用域-变量只能在函数内部有效
def fun01():
    num01 = 10  # 局部变量
    return num01
# print(num01)
print(fun01())

# 嵌套作用
def fun02():
    num02 = 20
    def fun03():
        num02 = 20
        num03 = 30
        print(num03)
    print(num02)

fun02()
fun02()

# 全局变量-在函数外部定义的变量
str01  = 'hello'
def fun04():
    print(str01)
fun04()

def fun05():
    print(str01)
fun05()


# 如果要想在函数内部定义全局变量，那么需要使用关键字global
# global定义的变量需要先定义再赋值
def fun06():
    global num06
    num06 = 100
    print(num06)
fun06()

def fun07():
    print(num06)

fun07()

# 练习：记录一个函数的调用次数。
# 初始化全局变量
count = 0
def fun_count():
    global count
    count += 1

fun_count()
fun_count()
fun_count()
fun_count()
fun_count()

print("fun_count函数调用了%d" % count)






