# author by Michealzou@126.com
# 2022/3/28 13:54
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


factorial(10)