"""
    字典：可变的无序容器
    元素以key-value
    1.创建字典
        1.1 dict01 = {k1:v1,k2:v2....}
        1.2 dict02 = dict(k1=v2,k2=v2)
    2.字典查询
        []取值------>gdp['四川']
        get()方法-------->gdp.get('四川')
        - []如果字典中不存在指定的key，则抛出KeyError异常；
    3.字典元素的判断
            in  /  not in
    4.字典删除
        del 字典[key] -删除单个元素
        clear() - 清空字典
    5.新增、修改 ： 字典[key] = value

"""
# 创建字典
dict01 = {}
dict02 = {"name": '张三', 'age': 18, 'gender': '男', 'money': 99.99, '婚否': False}
dict03 = dict()
dict04 = dict(name="张三",age=20)

# 字典的查找
print(dict02['name'])
print(dict02.get('age'))
# print(dict02['sex'])  # KeyError
print(dict02.get('sex'))  # None

# 元素判断
print('name' in dict02)  # True
print('age' not in dict02)  # False

# 字典删除
del dict02['name']
print(dict02)
dict02.clear()
print(dict02)  # {}

# 新增、修改
dict04['name'] = '李四'
print(dict04)
dict04['gender'] = '女'
print(dict04)

print("============")
"""
    字典视图操作
        keys()-查找所有的key
        values()-查找所有的value
        items()-查找对应的k-v
"""
gpd = {'成都': '2500', '眉山': '180', '绵阳': '400', '宜宾': '350'}
keys = gpd.keys()
print(keys)
values = gpd.values()
print(values)
print(gpd.items())
# 遍历
for item in gpd:
    print(item, gpd[item])

for k, v in gpd.items():
    print(k, v)




