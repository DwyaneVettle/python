"""
    python作用域：LEGB
        局部作用域、全局作用域、py模块的作用域、内置模块作用域
        在函数内部的变量只能在函数内部有作用
        如果要在函数内部提升变量的作用域-将局部变量提升为全局变量
        使用global关键字定义变量
        注意：先使用global定义变量，再进行赋值
"""
# 在函数外部定义的变量-全局变量,在整个py文件中都能找到
g01 = 200
def fun01():
    l01 = 100  # 局部变量
    global l02
    l02 = 300
    print(l01)
    print(g01)
# print(l01)  NameError: name 'l01' is not defined
fun01()
print(l02)
print(g01)

