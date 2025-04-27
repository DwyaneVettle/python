"""
    1.列表的特点：
        - 列表元素按顺序有序排列；
        - 索引映射唯一一个元素；
        - 列表可以存储重复数据；
        - 任意数据类型混存；
        - 根据需要动态分配和回收内存。
    2.列表索引：
        正向：从0开始到n-1结束
        反向：从-1开始到-n结束
    3.列表的增加：
        append()：在列表末尾添加一个元素
        extend()：在列表末尾添加多个元素
        insert()：在列表指定位置添加一个元素,后面的元素一次后移，下标+1
        +：列表拼接 创建新列表
        切片：列表拼接 创建新列表, 反向切片步长为-1
    4.列表的删除：
        remove():一次性删除一个元素，不存在的元素会抛出一场
        pop()：删除指定位置上的元素，不存在则会报索引一场
        clear():清空列表
        del：删除列表
    5.列表的修改
        1.为指定索引的元素赋予一个新值；
        2.为指定的切片赋予一个新值
    6.列表的查询：根据指定的索引来查询
    7.列表的遍历
"""
list01 = ["python", 123, 99.9, True]
print(id(list01))
# 列表元素增加
list01.append("java")
print(list01)
print(id(list01))  # 1834463461120
list01.extend(["c", "c++", "golang"])
print(list01)
list01.insert(1, "php")
print("list01= ",list01)  # ['python', 'php', 123, 99.9, True, 'java', 'c', 'c++', 'golang']
list02 = ["a", "b"]
list03 = list01 + list02
print(list03)
# 切片
list04 = list01[0:2:1]
print(list04)
list05 = list01[-1:-4:-1]
print(list05)
print("===========")

# 列表的删除
list06 = ["python", "java", "php", "html", "python", "html"]
list06.remove('python') # 如果删除的元素是重复，则默认删除第一个
print(list06)  # ['java', 'php', 'html', 'python', 'html']
# list06.remove("css")  # ValueError
# print(list06)
list06.pop(0)  # ['php', 'html', 'python', 'html']
list06.pop()  # 如果pop()不传递参数，默认删除的是最后一个元素
print(list06)  # ['php', 'html', 'python']
# list06.pop(4)  # IndexError
list06.clear()
print(list06)  # []，仍然在内存中占有空间
# 如果要手动把列表踢出内存，可以手动删除del
# 一般情况下不建议使用del手动删除列表，因为python内存机制可以根据对象身上
# 引用计数器删除，当引用计数器数量为0时，就会被内存删除
del list06
# print(list06)
print("===========")

# 列表修改
list06 = ["python", "java", "php", "html", "python", "html"]
# 将指定位置上的元素进行修改
list06[4] = "css"
print(list06)
# 切片
list06[1:5] = ["c++", "golang", "php"]
print(list06)  # ['python', 'c++', 'golang', 'php', 'html']
print("===========")

# 列表元素的查询 index()
# 1.根据元素查找
print(list06.index("python"))  # 0
print(list06.index("golang",2, 4))  # 在2-4索引之间查找golang, 2
# 2.根据下标查找
print(list06[-2])
print("===========")

# 列表的遍历-把列表的所有元素一一列出来
list07 = ["python", "java", "php", "html", "python", "html"]
# 判断元素有没有在列表中， in、not in
print("c++" in list07)  # False
print("c++" not in list07)  # True
# 遍历
for item in list07:
    print(item)

