# author by Michealzou@126.com
# 2022/11/2 8:47
"""
    字典：以k-v结构存储的可变序列
    key:value,key:value
    一般Key都是string
"""
# 1.创建
dict01 = {"成都": 2000, "眉山": 150, "自贡": 200}
dict02 = dict(one=1, two=2)
print(dict02)
print(type(dict01))  # <class 'dict'>

# 2.查询-通过[Key]查找value
print(dict01["成都"])  # 2000
print(dict01.get("眉山"))

# 3.新增-通过增加key赋值value
dict01["凉山"] = 500
print(dict01)
print("-----------")
# 4.删除
# pop()指定key删除
# del
dict01.pop("凉山")
# del dict01["成都"]
# 当Key不存在是会报KeyError
# del dict01["绵阳"]
print(dict01)  # {'眉山': 150, '自贡': 200}
# clear()清空字典
dict01.clear()
print(dict01)
print("-----------")
dict01 = {"成都": 2000, "眉山": 150, "自贡": 200}
# 5.遍历
# 5.1.遍历key
for key in dict01.keys():
    print(key)
    print(dict01[key])
print("-----------")
# 5.2.value
for value in dict01.values():
    print(value)
print("-----------")
# 5.3.key,value -items()
for k, v in dict01.items():
    print(k)
    print(v)
