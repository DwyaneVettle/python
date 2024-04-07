"""
    列表生成式：
        元素之间有规律的前提下可以使用
        list01 = [规则 for i in 可迭代对象]
"""
list01 = [i for i in range(0, 11, 1)]
print(list01)
# [1,4,9,16,25]
list02 = [i*i for i in range(1, 6)]
print(list02)
list03 = [i*2 for i in "python"]
print(list03)
