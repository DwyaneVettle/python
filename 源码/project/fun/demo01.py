# author by Michealzou@126.com
# 2022/4/19 9:15
# 函数返回值
def fun01(acount):
    print("fun01()执行了")
    return 20
	# print("fun01()又执行了") # return后的语句不会执行

re = fun01(10)
print(re)

# 无返回值函数
def fun02(a):
    print("fun02()执行了")


re02 = fun02(100)
print(re02)
