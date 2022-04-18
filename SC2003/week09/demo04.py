# author by Michealzou@126.com
# 2022/4/18 16:17
# 固定集合:不重复不可变类型的容器
# 不能增删改，其他方法使用和集合一样
set01 = frozenset([31, 31, 28, 31, 30])
print(set01)
for item in set01:
    print(item)
