# author by Michealzou@126.com
# 2022/3/28 16:10
# 列表的添加
list01 = ['python', 'java', 'php', 'html', 'js']
# 1.append():在末尾添加一个元素
list01.append('c++')
print(list01)
# 2.extend():在末尾至少添加一个元素,如果是多个，那必须是另一个列表
list02 = ['c', '仓颉', '易']
list01.extend(list02)
print(list01)
# 3.insert():将元素插入到指定位置,第一个参数为索引值，第二个参数为插入元素
list01.insert(1, 'golang')
print(list01)
