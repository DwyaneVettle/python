"""
    python函数的内存图
"""
# 在方法区中存储函数代码，不执行函数体
def fun01(a):
    a = 100
    print(a)  # 100

# num01在栈帧中保存
num01 = 1
# 调用函数，在栈开辟一块内存空间
# 用于存储在函数内部定义的变量
fun01(num01)
# 函数执行完毕后，栈帧随机释放了，所以在函数内部定义的变量
# 也会销毁
print(num01)  # 1
# print(a)  报错


def fun02(a):
    # 改变的是传入的可变对象
    a[0] = 100

list01 = [1]
fun02(list01)
print(list01[0])  # 100


def fun03(a):
    # 改变的是fun03的栈帧中的变量a的指向
    a = 100

list01 = [1]
fun03(list01)
print(list01[0])  # 1

