# author by Michealzou@126.com
# 2022/3/28 16:41
# 删除列表
list01 = ['python', 'java', 'php', 'html', 'js']
# del：删除列表中指定位置的元素,如果直接删除列表，那么列表就会被GC
# del list01
del list01[-1]
print(list01)

# remove():删除某一个元素，但是列表中如果有同名的元素，则只删除第一个
list02 = ['python', 'java', 'php', 'html', 'js', 'python']
list02.remove('python')
list02.remove('php')
# list02.remove('ruby')  ValueError
print(list02)

# pop():删除元素，没有传参的情况下删除的是最后一个元素,是以下标作为参数
list03 = [1, 2, 3, 4, 5, 'aa']
list03.pop(2)
list03.pop()
# list03.pop(6)
print(list03)

# clear():清除列表所有元素，但是列表名仍然存在
list03.clear()
print(list03)