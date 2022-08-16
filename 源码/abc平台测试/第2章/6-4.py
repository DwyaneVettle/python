# author by Michealzou@126.com
# 2022/8/8 13:01
# python 值拷贝（浅拷贝，深拷贝）
# 1.浅拷贝(地址的引用传递)，将lst拷贝给对象a，并将lst第一个元素置为99

lst01 = [1, 2, 3, 4]

a = lst01
lst01[0] = 99

print(lst01)  # id()一样则地址一样（就是同一个对象）
print(a)

# 2.深拷贝(创建新对象，地址不一样),将lst2深拷贝给对象b，并将lst2第一个元素置为66
lst02 = [2, 4, 6, 8]

b = lst02[:]
b = lst02.copy()
lst02[0] = 66

print(lst02)
print(b)
