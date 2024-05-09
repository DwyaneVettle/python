"""
    递归函数：在函数的内部调用函数本身
    递归函数必须有一个边界条件用于结束递归调用
"""
# 求10的阶乘
def jiecheng(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num * jiecheng(num - 1)

print(jiecheng(10))

# 练习：斐波那契数列 0，1，1，2，3，5，8，13。。。
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
num = int(input("输入一个正整数："))
for i in range(1, num + 1):
    print(fibonacci(i))
