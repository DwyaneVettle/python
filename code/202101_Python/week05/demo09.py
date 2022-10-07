# author by Michealzou@126.com
# 2022/10/5 11:16
"""
range()
    range(stop)-从0开始到stop-1结束，默认步长为1
    range(start,stop)-从start开始到stop-1结束，默认步长为1
    range(start,stop,step)-从start开始到stop-1结束，步长为step
    生成一个可迭代对象
"""
for item in range(1, 10, 2):
    print(item)

lst = list(range(1, 10, 2))
print(lst)

# sum-求和
print(sum(range(1, 10, 2)))
