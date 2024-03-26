"""
    字典的生成式：
        s = {item.upper(): price for item, price in zip(items, prices)}
"""
items = ["apple", "banana", "pear"]
prices = [12, 10, 8]
dict01 = {item.upper(): price for item, price in zip(items, prices)}
print(dict01)
dict02 = {i: i*i for i in range(1, 10)}
print(dict02)

