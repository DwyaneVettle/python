# author by Michealzou@126.com
# 2022/4/11 16:30
# 字典生成式:s = {item: price for item, price in zip(items, prices)}
# upper()将元素转换成大写
# zip()打包，将参数建立对应的关系
list01 = ["书籍", "水果", "家电"]
price = [100, 200 ,300]
dict01 = {item:price for item, price in zip(list01, price)}
print(dict01)

