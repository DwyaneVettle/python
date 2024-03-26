"""
    列表：一个由一系列对象组成的容器
    特点：1.可以增删改；2.可以迭代；3.可以存储任何类型的数据；4.可以存储重复的元素
    1.列表的创建：[]  list(可迭代的对象)
    2.列表的新增：
        append():在末尾追加元素
        insert(index,ele)：在指定位置处增加元素
    3.列表的删除：
        pop()：删除末尾的元素或指定下标
        remove()：删除指定的一个元素，如果该元素重复，只删除第一个
        clear()：清空列表，内存仍然保留该列表
        del 列表名：直接将列表从内存中移除
    4.列表的修改：
        找到指定下标重新赋值
        切片:可以不匹配个数
    5.列表的查询：
        [下标]
        index()-1.通过指定元素找到下标；2.通过区间的下标找到对应元素
                3.在区间下标内找指定元素
"""
list01 = [1, 1.1, True, "python", "python"]
list02 = list("python")
# 创建空列表
list03 = []
list04 = list()

print(list01, type(list01))  # [1, 1.1, True, 'python'] <class 'list'>
print(list02)  # ['p', 'y', 't', 'h', 'o', 'n']
# 通过下标获取元素
print(list01[0], list01[-1])

print("=======")
# 新增
list01.append("hello")
print(list01)
list01.insert(1, False)
print(list01)

print("=======")
# 删除
list01.pop(3)
print(list01)
list01.remove("python")
print(list01)
list01.clear()
print(list01)
del list01
# print(list01)

print("=======")
# 修改
list05 = [1, 1.1, True, "python", "hello"]
list05[-2] = "java"
print(list05)
list05[1:3] = ["php", "c#", "rust"]
print(list05)


print("=======")
# 查找
list06 = list(["java", "python", "c++", "javascript", "python"])
# print(list06[5])  IndexError
print(list06[1], list06[-5])
print(list06.index("javascript", 1, 4))  # 1-4下标找javascript对应的下标

