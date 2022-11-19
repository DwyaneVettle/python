# author by Michealzou@126.com
# 2022/11/15 9:48
"""
    参数传递
"""
# 位置参数的传递：实参个数与形参一一对应
def fun01(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)

# fun01(1, 2, 3, 4)
# # 关键字参数传递
# def fun02(a=0, b=0, c=0, d=0):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#
# fun02(b=3, c=5)

# 序列传递-拆分序列给形参
# 用*拆分序列
list01 = ["aa", "bb", "cc", "dd"]
fun01(*list01)

# 字典参数
# 拆分字典参数用**
dict01 = {"a": "123", "b": "234", "c": "345", "d": "456"}
fun01(**dict01)
