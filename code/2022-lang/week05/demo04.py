"""
    内建函数：不需要对象调用，直接使用即可
    - len()：返回序列的长度
    - max()：返回序列中的最大值
    - min()：返回序列中的最小值
    - sum()：返回序列所有元素的和（必须为数值）
    - sorted(): 返回列表的排序，默认从小到大，reverse=True为降序
"""
list01 = [1, 2, 3, 4, 5]
print(len(list01))
print(max(list01))
print(min(list01))
print(sum(list01))
list02 = [3, 5, 6, 2, 1]
print(sorted(list02, reverse=True))

