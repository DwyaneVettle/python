# author by Michealzou@126.com
# 2022/5/9 12:54
def factorial(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(10))


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input('请输入一个正整数: '))
for i in range(1, num + 1):
    print(fibonacci(i), end=' ')
