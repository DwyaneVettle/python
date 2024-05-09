# 练习：记录一个函数的调用次数
count = 0
def fun01():
    global count
    count += 1

fun01()
fun01()
fun01()
fun01()
print(f"调用{count}次")