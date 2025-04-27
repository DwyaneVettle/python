"""
    递归函数：处理较复杂问题时，在函数内部调用自己本身的过程
    注意点：
        1.递归的公式-业务处理
        2.边界条件-如何终止
"""
# 求10的阶乘 1 x 2 x 3 ...x 10
def factorial(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(10))


# 练习：求斐波那契数列 0，1，1，2，3，5，8，13.....
# 规律： f(0)=0  f(1)=1  f(n)=f(n-1)+f(n-2)
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num = int(input("请输入一个数来获取斐波那契数列："))
for item in range(1, num + 1):
    print(fibonacci(item), end=" ")
