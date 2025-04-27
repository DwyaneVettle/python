"""
    列表生成式：
    [i*i for i in range(1, 10)]
    i*i表示列表元素的表达式
    i是自定义变量
    range(1, 10)是可迭代对象，表示1到9的整数
"""
list01 = [i * i for i in range(1, 10)]
print(list01)
list02 = [i * 2 for i in range(1, 10)]
print(list02)
