"""
    在控制台中循环录入商品信息(名称,单价)，如果名称输入
    空字符,则停止录入，将所有信息逐行打印出来
    {名称:单价}
"""
info = {}
while True:
    name = input("录入商品信息：")
    if name == "":
        break
    price = input("录入商品单价：")
    info[name] = price
for key, value in info.items():
    print(f"{key}的单价是{value}")

