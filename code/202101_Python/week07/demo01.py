# author by Michealzou@126.com
# 2022/10/19 8:45
"""
    列表
"""
# 列表的创建
# 1.[]
list01 = []
# 2.list([])
list02 = list(["python", 123, 12.12, True])

# 1.增加元素
# 1.1.在末尾增加-append()
list02.append("孙悟空")
# 1.2.在指定位置增加-insert()
list02.insert(1, "八戒")
print(list02)
# ['python', '八戒', 123, 12.12, True, '孙悟空']
# 2.删除
# 2.1.删除指定元素-remove()
list02.remove("八戒")
# 2.2.删除指定下标-del list02[index]
del list02[2]

# 2.3.删除末尾(可以传下标删除指定，默认不传为最后一个)-pop()
list02.pop()
# 2.3.清空列表-clear()
list02.clear()
print(list02)
print("-----------")
# 3.修改元素
"""
    切片[start:stop:step]：方便增删改查
    start:表示切片开始的下标，包含
    stop:表示切片结束的下标，不包含
    step:步长，隔几个切片，默认为1
"""
list01 = ["悟空", 123, 100.1, False]
# 修改某个元素用下标
list01[1] = "八戒"
print(list01)
# 修改一组元素用切片
list01[2:4:] = [100, True, "白骨精"]
print(list01)  # ['悟空', '八戒', 100, True, '白骨精']

# 4.查询
# 4.1.查一个
print(list01[1])
# 4.2.切片  ['悟空', '八戒', 100, True, '白骨精']
print(list01[1:4:2])

print("-----------")
list01 = ["悟空", 123, 100.1, False]
# 5.遍历
for i in list01:
    print(i)

# 下标0,1,2,3
# len()- 表示列表的长度
for i in range(0, len(list01)):
    print(list01[i])

for i in range(-len(list01), 0):
    print(list01[i])

print("---------")
# 3,2,1,0
for i in range(len(list01)-1, -1, -1):
    print(list01[i])
