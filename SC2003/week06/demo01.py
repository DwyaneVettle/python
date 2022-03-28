# author by Michealzou@126.com
# 2022/3/28 14:19
# 列表的创建
"""
    1.直接以中括号的方式创建
    2.list()函数创建
    列表可以放n个元素,任何类型都可以放，元素之间用逗号隔开
"""
list01 = ['python', 123, 10.12, True, 'p', 'y', 't', 'h', 'o', 'n']
list02 = list(['hello', 100, 50.0, False])

print(list02)
list03 = ['python', 123, 10.12, True, 'p', 'y', 't', 'h', 'o', 'n']
list01 = ['你好', 123]
print(list01)
print(id(list01))
print(id(list03))
