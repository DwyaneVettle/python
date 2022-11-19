# author by Michealzou@126.com
# 2022/11/15 9:34
# 练习：统计函数的调用次数
count = 0
def fun01():
    count = 1
    count += 1
    print(count)


fun01()
fun01()
fun01()
fun01()
print("调用了" + str(count) + "次")
