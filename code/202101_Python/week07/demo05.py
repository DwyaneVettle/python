# author by Michealzou@126.com
# 2022/10/19 11:10
# 列表的内存
list01 = ["悟空", "八戒"]
list02 = list01
list01[0] = "如来"
print(list02[0])  # 如来

list01 = ["悟空", "八戒"]
list02 = list01
list01 = ["如来"]
print(list02[0])  # 悟空

print('--------')
list01 = [800, 1000]
list02 = list01[:]  # 创建一个新的列表
list01[0] = 900
print(list02[0])  # 800

print('--------')
list01 = [800, [1000, 500]]
list02 = list01
list01[1][0] = 900
print(list02[1][0])  # 900
