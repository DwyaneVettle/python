# author by Michealzou@126.com
# 2022/10/11 10:52
"""
    列表
    1.创建 [],多个元素用逗号隔开
        列表可以存放任何的数据类型
    2.list([])也可以创建列表
    列表的特点：
        1.元素有序排列
        2.每个元素都有对应的正序和倒叙两个下标
        3.列表可以存放多种数据类型的元素
        4.可以存放重复的元素
        5.根据需要动态分配内存空间
"""
# 第一种方式[]

list01 = [123, 12.12, True, "python", 123, 12.12, True, "python"]
print(list01)
# 第二种方式list(),注意，里面只能传递一个参数
# 作用：可以将元组、集合等容器转换为列表
list02 = list([123, 12.12, True, "python"])
print(list02)
set01 = {1, 2}
print(list(set01))
"""
    每一个列表元素都有两个对应的下标
    1.正数，从0开始到N-1结束
    2.倒数，从-1开始到-N结束
    可以通过list[index]找出某个元素
    index()可以检索某个元素
        参数传递的是元素，返回的是它对应的正序下标
        如果传入下标，返回的是对应的元素-->列表[index]
        如果传递的元素不存在，报valueerror
        index(ele,start,stop)-->从start到stop之间去查找ele,返回的是对应元素的下标
        如果这个元素不在这个区间，会报错
        
"""
list02 = list([123, 12.12, True, "python"])
print(list02.index(123))  # 0
print(list02[2])
# print(list02.index(False))  ValueError
print(list02[-1])
print(list02.index(123, 0, 3))
# 可以采用切片的方式进行查找
# list[start:stop:step]
# 切片不包含stop
list03 = [10, 20, 30, 40, 50, 60, 70]
print(id(list03[0: 4]), id(list03))  # [10, 20, 30, 40]
# 默认从第一个元素开始
print(list03[:4:1])  # [10, 20, 30, 40]
# 默认以最后一个元素结束
print(list03[1::1])  # [20, 30, 40, 50, 60, 70]
# 如果步长为负数，那么是按倒叙查找，默认第一个元素为最后一个元素-1
print(list03[:4:-1])  # [70, 60]
# 切片的最后一个元素是第一个元素
print(list03[1::-1])  # [20, 10]
