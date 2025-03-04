def sum(num01, num02):
    return num01 + num02
def mul(num01, num02):
    return num01 - num02
def div(num01, num02):
    return num01 / num02
def mod(num01, num02):
    return num01 * num02
def main():
    while True:
        print("1.加法运算")
        print("2.减法运算")
        print("3.乘法运算")
        print("4.除法运算")
        print("5.退出程序")
        num = int(input("请选择对应的计算功能"))
        if num == 1:
            num01 = int(input("请输入第一个数"))
            num02 = int(input("请输入第二个数"))
            sum = sum(num01, num02)
            print("两数之和为：", sum)
        elif num == 2:
            num01 = int(input("请输入第一个数"))
            num02 = int(input("请输入第二个数"))
            mul01 = mul(num01, num02)
            print("两数之差为：", mul01)
        elif num == 3:
            num01 = int(input("请输入第一个数"))
            num02 = int(input("请输入第二个数"))
            mod01 = mod(num01, num02)
            print("两数之积为：", mod01)
        elif num == 4:
            num01 = int(input("请输入第一个数"))
            num02 = int(input("请输入第二个数"))
            div01 = div(num01, num02)
            print("两数之商为：", div01)
        elif num == 5:
            print("退出程序")
            break
