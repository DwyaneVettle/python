# author by Michealzou@126.com
# 2022/8/7 22:44
# 10.2
# python字典 类似于其他语言中的map {key:value,key2:value2}
# 1.字典的定义方式
dic = {"uname": "admin", "pwd": "123"}

# 2.根据键获取值(字典中的键就是索引  dict【key】),get()方法获取
print(dic.get('pwd'))  # 开发中建议使用

# 3.更新字典中的键值对
dic['pwd'] = "666"  # 键相同，值会覆盖
print(dic)

# 4.获取字典中所有的键key的列表,获取所有的值
keys = dic.keys()
values = dic.values()
print(keys, values)

# 5.字典的删除方法
del dic['uname']  # del object 通用的删除
print(dic)