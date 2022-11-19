# author by Michealzou@126.com
# 2022/11/15 11:26
"""
    求斐波那契数:当前数=前面01+前面02
    1,1,2,3,5,8,13....
    f(0) = 0 f(1)=1 f(n) = f(n-1) + f(n-2) n>=2
"""
# n表示几位
def fibonacci(n):
    if n == 1 or n== 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)

num = int(input("请输入位数求斐波那契数："))
for i in range(18, num+1):
    print(fibonacci(i), end=" ")