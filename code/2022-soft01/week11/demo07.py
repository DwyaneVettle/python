"""
    递归函数：
        在函数的内部调用本身的过程，把一个大型的问题变得非常简单
    1.定义递归的公式；2.边界条件
    递归公式是解释过程的归纳项，用于处理原问题和对原问题类似的问题
    边界条件是终止递归的调用
"""
# 阶乘 n*(n-1)*(n-2)...1
def factorail(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num*factorail(num-1)

print(factorail(100))

# 求斐波那契数列 0 1 1 2 3 5 8 13...
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
num = int(input('请输入一个正整数: '))
for i in range(1, num + 1):
    print(fibonacci(i), end=' ')
