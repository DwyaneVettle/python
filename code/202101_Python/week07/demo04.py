# author by Michealzou@126.com
# 2022/10/19 10:55
"""
    列表生成式:
    前提：列表中的数据有一定的规律
    语法：
    [规律 for i in range()]
"""
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
list01 = [i for i in range(1, 10,1)]
print(list01)
# [1,4,9,16,25,36,49,64,81]
list02 = [i*i for i in range(1, 10, 1)]
print(list02)

# [2,4,6,8,10]
list03 = [i for i in range(2, 11, 2)]
list04 = [i*2 for i in range(1, 6, 1)]
