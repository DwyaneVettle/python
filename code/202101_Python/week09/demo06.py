# author by Michealzou@126.com
# 2022/11/2 11:41
# 字典的Key是唯一的
# 如果key重复，那么最后一个取代前面相同Key的值
dict01 = {"name": "zhangsan", "name": "lisi"}
print(dict01)  # {'name': 'lisi'}

# 字典生成式
# {1:1,2:4,3:9  ...10:100}
# dict01 = {}
# for i in range(1, 11):
#     dict01[i] = i*i
# print(dict01)
dict01 = {i: i*i for i in range(1, 11) if i > 5}
print(dict01)/66
