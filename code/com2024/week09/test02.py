"""
    列表的排序：
        1. sort() 方法：默认从小到大的方式排序，可以指定属性reverse=True，从大到小排序
        2.sorted() 方法：返回一个新的列表，不会改变原来的列表,reverse=True也能实现从大到小的排序
"""
# 1.sort()方法
list01 = [3, 45, 89, 56, 7, 90, 123, 456, 789, 0]
list01.sort()
print(list01)
list01.sort(reverse=True)
print(list01)
# sorted()
list02 = [3, 45, 89, 56, 7, 90, 123, 456, 789, 0]
list03 = sorted(list02)
print(list03)
list04 = sorted(list02, reverse=True)
print(list04)

