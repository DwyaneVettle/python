# author by Michealzou@126.com
# 2022/8/8 10:06
# 练习： 10以内偶数求平方，奇数不变
lst = [i**2 if i % 2 == 0 else i for i in range(1, 11)]

print(lst)