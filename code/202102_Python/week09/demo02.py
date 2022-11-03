# author by Michealzou@126.com
# 2022/11/1 9:08
"""
    输入商品信息（名称、单价），当输入空字符串
    停止录入，打印所有的商品信息
    名称:单价
"""
# 1.创建空字典保存商品信息
dict_commodity_info = {}
# 2.循环录入商品信息
while True:
    # 3.接收用户输入的商品
    name = input("请输入商品名称：")
    if name == "":
        break
    # 4.输入商品单价
    price = int(input("请输入商品单价:"))
    dict_commodity_info[name] = price

# 5.遍历
for k, v in dict_commodity_info.items():
    print("%s的单价是%d" % (k, v))



