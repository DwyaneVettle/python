"""
    在控制台中循环录入商品信息(名称,单价)，如
    果名称输入空字符,则停止录入，将所有信息逐行打印出来。
"""
dict01 = {}
while True:
    names = input("请输入商品名称：")
    if names == "":
        break
    prices = input("请输入价格：")
    dict01[names] = prices
for name, price in dict01.items():
    print(f"{name}的价格是{price}")
