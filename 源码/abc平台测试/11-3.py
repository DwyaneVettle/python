# author by Michealzou@126.com
# 2022/8/8 10:03
# 1.使用列表生成式产生一个10以内奇数平方的列表
lst01 = [i**2 for i in range(1, 10, 2)]

print(lst01)

# 2.使用列表生成式产生20以内能被3整除数的平方的列表
lst02 = []

for i in range(1, 21):
    if i % 3 == 0:
        lst02.append(i**2)

print(lst02)
