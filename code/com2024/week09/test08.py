"""
练习1：
在控制台中循环录入商品信息(名称,单价)，
如果名称输入空字符,则停止录入，将所有信息逐行打印出来
"""
# 初始化字典
info = {}
while True:
    name = input("请输入商品信息：")
    if name == '':
        break
    price = input('请输入商品价格：')
    info[name] = price
for k, v in info.items():
    print("%s的价格是%s" % (k, v))
