"""
    固定集合：不可变的集合
    创建：frozenset(可迭代对象)
    运算和集合一样，只是元素不可改变
"""
set01 = frozenset("python")
print(set01, type(set01))  # <class 'frozenset'>
set02 = frozenset("hello")
print(set01 & set02)
print(set01 | set02)
