# author by Michealzou@126.com
# 2022/11/16 10:20
"""
    练习：记录函数被调用的次数
    1.在函数内部创建一个变量
    2.让变量每调用一次，这个变量就增加一个值
"""
count = 0
def fun01():
    global count
    count += 1


num = int(input("请输入循环的次数："))
for i in range(num):
    fun01()

print(count)
