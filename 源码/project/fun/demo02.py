# author by Michealzou@126.com
# 2022/4/19 9:17
def add(num1, num2):
    result = num1 + num2
    # print(result)
    return  result

num1 = int(input("请输入第一个数值："))
num2 = int(input("请输入第二个数值："))
num = add(num1, num2)
print("两数之和是："+ str(num))
