"""
    python的排序：
        sort():默认由小到大的排序，reverse=True-由大到小排序
        sorted():内置函数，默认由小到大的排序，reverse=True-由大到小排序
        sorted()返回一个新的列表
"""
list01 = [20, 48, 12, 8, 34]
list01.sort(reverse=True)
print(list01)
list02 = [20, 48, 12, 8, 34]
list03 = sorted(list02, reverse=True)
print(list03)
