"""
    字典：以k-v结构存储的可变序列
    1.字典的创建：{k1:v1,k2:v2...} ,dict()
    2.字典的查询：[key],  get(key)
    3.字典的判断：in ,not in
    4.字典的删除： del 字典名[key] ，clear()清空字典
    5.字典的新增和修改：[key]=value
    6.字典视图的操作：
            keys()：所有的key
            values()：所有的值
            items()：所有的k-v键值对,返回k,v的列表
"""
# 1.创建字典
gdp = {"成都": 23000, "眉山": 2300, "绵阳": 4000}
person = dict(name="tom", age=18, gender="男")
print(gdp)
print(person)
print(type(person))  # <class 'dict'>
# 2.字典的查询
print(gdp["成都"])
# print(gdp["雅安"])  # KeyError
print(gdp.get("眉山"))
# 3.字典的判断-只能判断key，不能判断value
print("雅安" in gdp)  # False
print("23000" in gdp)  # False
print("23000" not in gdp)  # True
# 4.字典的删除
del gdp["绵阳"]
print(gdp)
gdp.clear()
print(gdp)
# 字典的新增和修改
person["name"] = "micheal"
print(person)
person['height'] = 180
print(person)
# 字典的视图操作
print(person.keys())
print(person.values())
print(person.items())
for i in person.items():
    print(i)
