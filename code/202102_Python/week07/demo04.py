# author by Michealzou@126.com
# 2022/10/18 11:00
"""
    列表生成式
        [规律 for i in range()]
"""
# 1.生成一个1-10之间的列表
list01 = [i*i for i in range(1, 11)]
print(list01)
# 2.生成2，4，6，8，10
list02 = [i for i in range(2,11,2)]
print(list02)

list02 = [i*2 for i in range(1, 6)]
print(list02)
