# author by Michealzou@126.com
# 2022/4/11 16:55
# 元组
"""
元组是一个不可变的序列，不能增删改
一旦创建就不能修改
"""
# 1.元组的创建
# 元组的元素可以是任意类型
# 1.1.()
a = (10, 20)
print(id(a))  # tuple
# 1.2.tuple(列表)
b = tuple([100, 200])
print(type(b))  # tuple
a = (10, 20, 30)
print(id(a))

c =tuple({10, 20})
print(c)

d = (1)
print(type(d))  # int
# 如果元组里只有一个元素，需要在这个元素后面加上逗号,如果没有逗号就是一个普通类型的数据
e = (1,)
print(type(e))  # tuple

# 2.元组的查询--索引[]；切片
# 元组的元素也对应了下标，使用方式和列表一样
tuple01 = ("name", "sex", "age", "height")
print(tuple01[2])
s = tuple01[1:3:1]
print(s)
y = tuple01[-2:-4:-1]
print(y)

# 遍历
for i in tuple01:
    print(i)
