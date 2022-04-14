# author by Michealzou@126.com
# 2022/4/11 16:07
# 字典的视图操作
"""
1.keys()获取字典的所有的Key
2.values()获取字典所有的value
3.items()获取字典所有的k-v映射关系
"""
dict01 = dict(班长="zhangsan", 学习委员="lisi", 体育委员="wangwu")
keys = dict01.keys()
print(type(keys))  # dict_keys
values = dict01.values()
print(type(values))  # dict_values
items = dict01.items()
print(items)  # 元组

# 字典的遍历
for i in dict01:
    print(i, dict01[i])


