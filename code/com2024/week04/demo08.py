# 在控制台接收两个用户输入的值，保存到变量，并求它们的和
# input接收的数据都是字符串类型，所以做数学运算时需要转换类型
num01 = input("请输输入第一个数：")
num02 = input("请输输入第二个数：")
num03 = int(num01) + int(num02)
num04 = num01 + num02
print(num03)
print(num04)
