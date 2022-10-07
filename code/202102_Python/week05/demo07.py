# author by Michealzou@126.com
# 2022/10/4 10:24
"""
    range()用于生成一个可迭代的序列
    range(stop)-生成一个(0,stop)，步长step默认为1
    range(start,stop)-生成一个(start,stop)，步长默认为1
    range(start,stop,step)-生成一个(start,stop)，步长为step
    stop不包含其中
"""
for i in range(2, 10, 2):
    print(i)
lst = list(range(0, 11, 2))
print(lst)

# sum()求和
print(sum(range(1, 6)))
