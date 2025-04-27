"""
    range()函数：用于生成一个可以迭代的序列：
    可迭代：字符串、列表、元素、字典、集合。。
    配合循环语句使用
    range(start, stop, step)
    start:表示生成序列的起始值，包含，默认值0
    stop:表示生成序列的终止值，不包含
    step:表示生成序列的步长，默认值1
    说明：
        1.只有两个参数，表示开始和结束，步长默认为1不写
        2.只有一个参数，表示从0开始到该参数前一个结束，步长默认值不写
"""
# 生成一个从0到9的序列
# for i in range(0, 10, 1):
#     print(i)
# for i in range(0, 10):
#     print(i)
# for i in range(10):
#     print(i)
# 0 2 4 6 8 10
for i in range(0, 11, 2):
    print(i)
