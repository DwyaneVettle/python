"""
    可变集合：类型固定、不重复的可变容器 -- 集合相当于是没有值的字典
        使用场景：操作交并补集的运算
        删除元素的两个方法：remove(ele)删除集合中指定的元素，如果没有则抛出ValueError
                        discard(ele)删除集合中的元素，如果没有则do nothing
"""
# 1.创建集合 set(),{}
set01 = set("python")
set02 = {1, 2, 3, 4}
print(set02)  # {1, 2, 3, 4}

# 2.add()添加元素
set02.add(5)
set02.add(4)
print(set02)

# 3.删除元素-remove(ele) discard() pop()
set02.remove(4)
print(set02)
set02.discard(5)
print(set02)
# set02.remove(10)  # KeyError
set02.discard(10)
set02.pop()
print(set02)

# 遍历集合中所有的元素
for i in set02:
    print(i)

# 修改-update()在集合后追加元素，参数是一个可迭代对象
set02.update([11, 12, 13])
print(set02)

# print(set02[2])  # TypeError
