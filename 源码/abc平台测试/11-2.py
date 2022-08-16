# author by Michealzou@126.com
# 2022/8/8 9:59
# 1.需要用range()产生一个1~9连续整数的列表
lst = list(range(1, 10))

print(lst)

# 2.需要产生一个1~9连续整数平方的列表
lst02 = []

for i in range(1, 10):
    lst02.append(i**2)

print(lst02)