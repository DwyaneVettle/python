"""
    在python中，输出是通过print()在控制台输出的
    有时也会在控制台接收用户输入的值进行保存并在后续使用
    用到的函数input()
    注意：input()接收并保存的对象是一个字符串类型
    练习：用input接收用户输入的两个值做加法运算
"""
# name = input("请输入你的名字：")
# print(type(name))
num01 = int(input("请输入数字1："))
num02 = int(input("请输入数字2："))
print(num01 + num02)
