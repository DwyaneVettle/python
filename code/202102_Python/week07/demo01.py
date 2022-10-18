# author by Michealzou@126.com
# 2022/10/18 8:42
# 1.创建
list01 = []
list02 = list([])
print(list02)

list03 = [123, 100.2, "悟空", True]
list04 = list("我是齐天大圣孙悟空")

# 2.增加元素
# append-在列表的末尾追加元素
print(list03.append("马城"))
print(list03)
# list05 = list03.append("马城")
# print(list05)
# insert()-在指定的位置去插入
list03.insert(1, 100)

# 删除
print(list03)  # [123, 100, 100.0, '悟空', True, '马城']
# 1.指定元素删除remove()
# print(list03.remove(False))  # ValueError
list03.remove(100.2)
print(list03)  # [123, 100, '悟空', True, '马城']
# 2.删除某个下标元素del
del list03[1]
print(list03)  # [123, '悟空', True, '马城']
# 3.pop()-指定删除末尾的元素
list03.pop()
print(list03)  # [123, '悟空', True]
# 4.clear()-清空列表
list03.clear()
print(list03)  # []

# 3.修改列表
list01 = [123, 100.2, "悟空", True]
# list01[0] = 321
"""
    [start:stop:step]
    start:表示切片的开始位置-包含
    stop:表示切片结束的位置-不包含
    step:表示切片的步长，默认为1
"""
list01[1:4:1] = [123, 200.2, '悟空', True, False]
print("-----------")
print(list01)
print("-----------")
list01[1] = 200.2
print(list01)  # [123, 200.2, '悟空', True]
# 切片：方便增删改查
list01[1: 4:] = [1, 2, 3, "hello", False]
print(list01)  # [123, 1, 2, 3, 'hello', False]


# 4.查询
# 1.查某一个元素-下标
print(list01[1])
# 2.切片
"""
    [start:stop:step]
    start:表示切片的开始位置-包含
    stop:表示切片结束的位置-不包含
    step:表示切片的步长，默认为1
"""
print(list01[1:5])
print(list01[-5:-1])  # [1, 2, 3, 'hello']


# 5.遍历
for item in list01:
    print(item)
# [123, 1, 2, 3, 'hello', False]
# 倒叙获取列表元素，切片步长为-1
# 不建议采用
for item in list01[:: -1]:
    print(item)

# 5，4，3，2，1，0  len()
for item in range(len(list01) - 1, -1, -1):
    print(list01[item])

list01 = [123, 100.2, "悟空", True]
print(list01[1: 3:1])
print(list01[-3:-1])