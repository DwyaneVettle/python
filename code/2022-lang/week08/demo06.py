# 练习：定义一个函数，打印该函数调用的次数
count = 0
def fun01():
    global count
    count += 1

    
fun01()
fun01()
fun01()
fun01()
print(f"函数调用{count}次")
