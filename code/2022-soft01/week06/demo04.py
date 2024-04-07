"""
    集合：不可变类型不能重复的可变序列-相当于只有key，没有value的字典
            乱序排列-无序
    1.创建集合： set(可变序列)  {}
    2.增加元素：add()
    3.集合删除：discard() remove() - 删除指定元素(元素不存在，不影响原有结构)
                pop()-删除任意一个
"""
# 创建集合
set01 = set("python")
set02 = {1, 2, 3}
print(set02, set02)
print(type(set01), type(set02))  # <class 'set'> <class 'set'>
set03 = {1, 1, 2, 3, 2, 3, 1, "python", True}
print(set03)  # {1, 2, 3, 'python'}
set02.add(100)
print(set02)  # {1, 2, 3, 100}
print("=========")
set02.discard(101)  # 如果元素不存在，不影响原有结构
print(set02)
set02.remove(100)
print(set02)
set02.pop()
print(set02)
# 遍历集合
for item in set01:
    print(item)
