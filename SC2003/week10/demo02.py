# author by Michealzou@126.com
# 2022/4/25 14:27
# 1,用形参和实参的方式来做加法函数运算
def add(num01, num02):
    result = num01 + num02
    return result


num01 = int(input("请输入数字1："))
num02 = int(input("请输入数字2："))
num = add(num01, num02)
print(f"{num01}+{num02}的和"+ str(num))
