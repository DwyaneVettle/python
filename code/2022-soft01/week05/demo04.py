"""
    字典：{k1:v1,k2:v2}
    可变序列
    1.创建字典：{k1:v1,k2:v2}  dict(k1=v1,k2=v2)
    2.字典的获取：[k]  get(k)
    3.字典的判断：in 、 not in
    4.字典的删除： del dict[key]、 clear()清空字典
    5.字典的新增和修改：通过指定的key来新增和修改
    6.字典的视图操作：
        keys():获取字典所有的Key
        values()：获取字典所有的value
        items()：获取字典所有的k-v
"""
# 创建字典
dict01 = {"name": "abc", "age": 18, "sex": "男"}
print(type(dict01))  # <class 'dict'>
print(dict01)  # {'name': 'abc', 'age': 18, 'sex': '男'}
dict02 = dict(name="test", age=20, sex="女")
print(dict02)  # {'name': 'test', 'age': 20, 'sex': '女'}
dict03 = {}  # 空字典
print(type(dict03))  # <class 'dict'>

# 字典的查询
gdp = {"成都": 10000, "眉山": 2000, "绵阳": 4000, "乐山": 3000}
print(gdp["成都"])
print(gdp.get("眉山"))
print(gdp.get("雅安"))  # None
# print(gdp["雅安"])  KeyError


# 字典的判断
gdp = {"成都": 10000, "眉山": 2000, "绵阳": 4000, "乐山": 3000}
print("雅安" in gdp)  # False
print("雅安" not in gdp)  # True
# 字典的删除
del gdp["乐山"]
print(gdp)  # {'成都': 10000, '眉山': 2000, '绵阳': 4000}
gdp.clear()
print(gdp)  # {}

# 新增和修改
gdp01 = {"成都": 10000, "眉山": 2000, "绵阳": 4000, "乐山": 3000}
gdp01["雅安"] = 1000
print(gdp01)
gdp01["成都"] = 12000
print(gdp01)

# 视图操作
print(gdp01.keys())  # dict_keys(['成都', '眉山', '绵阳', '乐山', '雅安'])
print(gdp01.values())  # dict_values([12000, 2000, 4000, 3000, 1000])
print(gdp01.items())  # dict_items([('成都', 12000), ('眉山', 2000), ('绵阳', 4000), ('乐山', 3000), ('雅安', 1000)])


# 字典的遍历-key
gdp01 = {"成都": 10000, "眉山": 2000, "绵阳": 4000, "乐山": 3000}
for item in gdp01:
    print(item, gdp01[item])

# 字典的特点：重复的key会导致前面被后面的取代
gdp01 = {"成都": 10000, "成都": 2000, "绵阳": 4000, "乐山": 3000}
print(gdp01)  # {'成都': 2000, '绵阳': 4000, '乐山': 3000}
