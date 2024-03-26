"""
    range()函数：表达指定的范围
        参数：
            start:范围的开始-包含
            end:范围的结束-不包含
            step:步长-元素的间隔
        range(end):表示从0开始到end结束，步长为1
        range(start,end):表示从start开始到end结束，步长为1
        range(start,end,step)：表示从start开始到end结束，步长为step
"""
for i in range(5):
    print(i)
print("====")
for i in range(5, 10):
    print(i)
print("====")
for i in range(5, 10, 2):
    print(i)
