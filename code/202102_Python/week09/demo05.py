# author by Michealzou@126.com
# 2022/11/1 11:22
"""
    集合：不可变、不重复的序列
    相当于是没有v的字典
"""
# 1.创建-set()
set01 = set("abc")
set02 = {"刘备", "关羽", "张飞"}
print(type(set02))  # <class 'set'>
# 1.添加-add(),如果往集合中添加已有元素，会删除元素，并添加到末尾
set02.add("刘备")
print(set02)
set02.add("小乔")
print(set02)  # {'刘备', '张飞', '关羽', '小乔'}
print("--------")
# 2.删除-pop()删除任意一个，remove()删除指定元素
set02.pop()
print(set02)
# remove()删除指定元素，没有该元素会报KeyError
# set02.remove("大乔") # KeyError
print(set02)
# discard()删除指定元素，没有该元素，do nothing
set02.discard("大乔")
print("--------")
# 3.遍历
set02 = {"刘备", "关羽", "张飞"}
for item in set02:
    print(item)
