# author by Michealzou@126.com
# 2022/4/25 16:49
# 在方法区中存储函数代码,不执行函数体
def fun01(a):
    a = 100

num01 = 1
# 因为调用函数，所以开辟一块内存空间，叫做栈帧
# 用于存储在函数内部定义的变量(包含参数).
fun01(num01)
# 函数执行完毕后，栈帧立即释放(其中定义的变量也会销毁).
print(num01) #1

def fun02(a):
    # 改变的是传入的可变对象
    a[0] = 100

list01 = [1]
fun02(list01)
print(list01[0]) # 100

def fun03(a):
    # 改变的是fun03栈帧中变量a的指向
    a = 100

list01 = [1]
fun03(list01)
print(list01[0])# 1