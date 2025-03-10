"""
    print()输出函数，用于将结果输出到控制台
    input()函数用于接收用户输入的值，并可以保存到变量中
    input()接收过来的值都是字符串类型
    练习：
        在控制台接收两个用户输入的值，保存到变量，并求它们的和
"""
# name = input("请输入你的名字:")
# print(f"我的名字是{name}")

# 测试：用Input()接收变量并保存，获取这个变量的数据类型
age = input("请输入你的年龄:")
print(age, type(age))  # 20 <class 'str'>

price = input("请输入商品价格:")
print(price, type(price))  # 99.999 <class 'str'>

bool01 = input("请输入布尔值:")
print(bool01, type(bool01))  # True <class 'str'>
