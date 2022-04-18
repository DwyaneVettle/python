# author by Michealzou@126.com
# 2022/4/18 15:15
# 集合：不重复不可变类型的容器
# 1.集合的创建：set()
set01 = set()
print(set01)
set02 = set("abc")
print(set02)
list01 = [1, 2, 3, 4]
set03 = {1, 2, 3, 4}
print(set03)

# 2.增加add()，删除
set03 = {1, 2, 3, 4}
set03.add(5)
print(set03)
# set04 = {7, 8, 9}
# set03.add(set04)
# print(set03)  # TypeError: unhashable type: 'set'
# 删除 discard(),remove(),pop()
set03.discard(2)
print(set03)
set03.remove(5)
print(set03)
set03.pop()  # 默认删除集合里的第一个元素
print(set03)
set03.pop()
print(set03)
set03.clear()
print(set03)
# 3.遍历
set03 = {1, 2, 3, 4}
for item in set03:
    print(item)
