"""
    列表表达式：
        [列表规则 for i in 可迭代序列]
    快速生成一个列表
"""
list01 = [i for i in range(1, 10, 1)]
print(list01)
# 1 2 9 16 25 36 49 64 81
list02 = [i * i for i in range(1, 10)]
print(list02)
# 2, 4, 6, 8, 10
list03 = [i * 2 for i in range(1, 6)]
print(list03)
print(list03 * 2)  # [2, 4, 6, 8, 10, 2, 4, 6, 8, 10]

list04 = [i*2 for i in "python"]
print(list04)

