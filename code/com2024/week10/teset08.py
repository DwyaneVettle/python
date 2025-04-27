"""
    固定集合：不可改变的集合，不能增加/删除元素
    创建：frozenset()
"""
set01 = frozenset([1, 2, 3, 4, 5])
set02 = frozenset([1, 2, 3, 6, 7])
print(set01 & set02)  # frozenset({1, 2, 3})
