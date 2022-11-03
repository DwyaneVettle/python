# author by Michealzou@126.com
# 2022/11/2 9:20
"""
    用户录入商品信息和价格，录入空字符串停止录入
    打印所有的信息
    {"商品": 价格}
"""
dict_commodity_info = {}
while True:
    name = input("请输入商品名称:")
    if name == "":
        break
    price = input("请输入商品价格:")
    dict_commodity_info[name] = price

for key, value in dict_commodity_info.items():
    print("%s的价格是%s" % (key, value))

