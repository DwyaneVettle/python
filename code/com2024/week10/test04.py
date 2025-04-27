"""
    列表：可变类型，有序，可重复
    字典：可变，k不可重复，v可以重复，无序
    集合：列表+字典  可变，无序，相当于只有k没有v的字典，所以不能出现重复的值
    特点：元素的不重复性，创建时可以重复，但是最终使用时只有一个相同的值
    1.创建：
        set01 = {}
        set01 = set()
    2.增加：
        set01.add(1)
    3.删除：
        集合名.discard(元素)
        集合名.remove(元素)
        集合名.pop()			# 删除任意一个
    4.遍历：
        for循环遍历
"""
# 创建
set01 = {1, 2, 3, 4}
set02 = set([5, 6, 7, 8])  # 无序 {8, 5, 6, 7}
print(set01, set02, type(set01))  # <class 'set'>
set03 = {1, 1, 1, 1}
set04 = {1, 1, 2, 2}
print(set03)  # {1}
print(set04)  # {1, 2}
# 增加
set01 = {1, 2, 3, 4}
set01.add(5)
print(set01)  # {1, 2, 3, 4, 5}
# set01.add(set02)
# print(set01)
# 删除
set01.discard(1)
print(set01)  # {2, 3, 4, 5}
set01.remove(5)
print(set01)  # {2, 3, 4}
set01.pop()
print(set01)  # {3, 4}
# 查找
set05 = {'a', 'b', 'c', 'd'}
for i in set05:
    print(i)
# set05[0] = 'e'
# print(set05)
set06 = {'a', 100, 99.9, True}
print(set06)

