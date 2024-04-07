"""
    列表的排序：
        1.列表.sort()-参数reverse=false,由小到大
        2.sorted(列表)-参数reverse=false,由小到大,返回新的列表
        场景：如果仍然使用原有的列表sort()，期望返回一个新的列表sorted()
"""
list01 = [1, 1.1, True, 100, 400, 35]
list01.sort(reverse=True)
print(list01)  # [400, 100, 35, 1.1, 1, True]
list02 = [12, 45, 23, 14, 200, 19]
list03 = sorted(list02, reverse=False)
print(list03)  # [12, 14, 19, 23, 45, 200]
