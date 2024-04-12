"""
    元组：一个不可变的序列-一旦创建就不能增删改
        元素可以是任何的数据类型
"""
# 1.创建元组 (), tuple(可迭代的序列)
tup01 = ()
tup02 = (10, True, "hello", 12.12, 10)
tup03 = tuple("python")
print(tup02.count(10))  # 返回元素对应的个数
print(tup02.index(10))  # 返回元素的下标

# 2.遍历
for i in tup02:
    print(i)

print(tup02 * 2)
