# author by Michealzou@126.com
# 2022/8/7 22:04
# 9.1
# 1.列表添加元素方法 append(任意对象)  追加的形式添加
lst01 = ['a', 'b', 1]

lst01.append(True)
print(lst01)

# 2.指定索引处插入元素 insert

lst01.insert(2, "c")

print(lst01)

# 3.删除列表中元素（开发中删除时需要先判断列表中是否有这个元素或索引）
# remove(元素)：删除元素1，当元素不存在时会报错（很少用）
# pop(index) ：将索引为3的元素删除
lst02 = ['a', 'b', 'c', 'a']
if 1 in lst02:
    lst02.remove(1)
lst02.pop(3)
print(lst02)

# 4.统计列表中某个元素出现的次数
lst03 = ['a', 'b', 'c', 'a', 'a']
# 统计a出现的次数
count_a = lst03.count('a')
print(count_a)

# 5.获取列表中某个元素第一次出现的索引
print(lst03.index('a'))
