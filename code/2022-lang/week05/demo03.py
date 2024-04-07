"""
    1.列表的创建  []  list() list()方法内只有一个参数，且该参数是一个可迭代的对象
    迭代=遍历
    2.判断元素是否在列表中  in 、not in
    3.列表的新增
        append()：在列表末尾添加一个元素
        extend()：在列表末尾添加至少一个元素（列表添加列表）
        insert(index,ele)：在指定位置index插入元素ele
        切片
    4.列表的删除
        remove():一次删除一个元素，重复元素删除第一个
        pop():删除最后，传递下标的参数时，删除指定下标的元素
        clear()：清空列表，仍保留列表在内存中
        del :删除整个列表，在内存中删除整个列表
    5.列表的修改-通过下标进行修改
    6.列表的查询
"""
# 创建列表
list01 = []  # 空列表
list02 = [100, 12.12, True, 'hello', 100]
list03 = list("python")
print(type(list02))  # <class 'list'>
print(list02)  # [100, 12.12, True, 'hello', 100]

# 判断
print(100 not in list02)

# 遍历
for i in list02:
    print(i)

# 新增
list02 = [100, 12.12, True, 'hello', 100]
list02.append("python")
print(list02)
print("=======")
list04 = ["python"]
list02.extend(list04)
print(list02)
print("=======")
list02.insert(2, False)  # 在指定下标所在的位置新增
print(list02)
list02.insert(-3, "你好")  # 在指定下标所在位置的前面新增（下标-1的位置）
print(list02)  # [100, 12.12, False, True, 'hello', '你好', 100, 'python', 'python']
print(list02[2:6:1])
print(list02[-5:-2])  # 列表的反向切片是从左到右
# [False, True, 'hello', '你好',] - 反向
print(list02[-7:-3])

# 列表的删除
list05 = ["python", "java", "php", "c++", "python"]
list05.remove("python")
print(list05)  # ['java', 'php', 'c++', 'python']
list05.pop(2)
print(list05)  # ['java', 'php', 'python']
list05.pop()
print(list05)  # ['java', 'php']
list05.clear()
print(list05)  # []
del list05
# print(list05)  NameError

# 列表的修改
list05 = ["python", "java", "php", "c++", "python"]
list05[4] = "c"
print(list05)
list05[-3] = "javascript"
print(list05)


# 列表的查询
print(list05[1])
print(list05[-1])
