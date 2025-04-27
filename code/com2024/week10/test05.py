"""
    数学运算：
        1.交集&：返回共同元素
        2.并集|：返回不重复元素
        3.补集-：返回只属于前者的元素
        4.补集^:返回不同的元素
        5.子集<:判断一个集合的所有元素是否完全在另一个集合中
        6.超集>:判断一个集合是否具有另一个集合的所有元素
        7. 相同或不同== !=：判断一个集合中的所有元素是否和另一个集合相同
"""
set01 = {1, 2, 3, 4}
set02 = {3, 4, 5, 6}
print(set01 & set02)  # {3, 4}
print(set01 | set02)  # {1, 2, 3, 4, 5, 6}
print(set01 - set02)  # {1, 2}
print(set01 ^ set02)  # {1, 2, 5, 6}
print(set01 > set02)  # False
print(set01 < set02)  # False
set03 = {1, 2}
print(set01 > set03)  # True
print(set01 == set03) # False
print(set01 != set03) # True
