# author by Michealzou@126.com
# 2022/4/11 14:52
# 字典
"""
1、创建
key:value,key2:value2
1.1.{}
1.2.dict()
字典是一个可变的序列
特点：1.key是唯一的，而value可以重复
"""
dict01 = {"班长": "谢涛", "学习委员": "王宾彬", "体育委员": "李刚", "文艺委员": "雒倩"}
dict02 = dict(sex="男", age=20, weight=110, name="李刚")
print(dict01)
print(dict02)

"""
2、字典的查询
2.1.通过字典名[key]
2.2.字典名.get(key)
只能通过key来获取value，如果没有对应的Key，会报KeyError
"""
dict03 = dict(四川=1000, 北京=2000, 上海=3000, 重庆=2500, 天津=1000)
sc = dict03["四川"]
print(sc)
print(dict03.get("上海"))
# print(dict03[1000]) KeyError: 1000

# 3、字典元素的判断:in & not in
print("湖北" in dict03)
print("云南" not in dict03)

# 4、字典的删除:1.del 字典名[key] ; 2.字典名.clear()清空字典
dict04 = {"name": "刘德华", "age": 50, "sex": "man"}
# 4.1.del 传入key进行删除，并且会删除key所映射的value
del dict04["sex"]
print(dict04)
# 4.2.clear()
dict04.clear()
print(dict04)

# 5.字典的增加-传入key:value
dict05 = {"name": "刘德华", "age": 50, "sex": "man"}
dict05["score"] = 99
print(dict05)

# 6.字典的修改
dict05["name"] = "张学友"
print(dict05)
