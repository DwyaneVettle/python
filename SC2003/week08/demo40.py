# author by Michealzou@126.com
# 2022/1/22 12:46
# 字典生成式

items = ['Fruits', 'Books', 'Others']
prices = [100, 101, 102]
s = {item.upper(): price for item, price in zip(items, prices)}
print(s)