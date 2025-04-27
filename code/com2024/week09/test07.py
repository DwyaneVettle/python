"""
字典的特点：
- 字典中所有的元素都是一个key-value对，key不允许重复，value可以重复；
- 字典中的元素是无序的；
- 字典中的key必须是不可变对象；
- 字典也可以根据需要动态伸缩；
- 字典会浪费较大的内存，是一种使用空间换时间的数据结构。
字典生成式：
    {k:v for k,v in zip(key,value)}
"""
gdp = {'成都': '2500', '眉山': '2500', '绵阳': '400', '成都': '350'}
print(gdp)
list01 = [100, 200, 300]

print(type(gdp))  # <class 'dict'>

print("-----------")
# {k:v for k,v in zip(key,value)}
list01 = ['name', 'gender', 'age']
list02 = ['micheal', '男', 20]
dict01 = {k:v for k, v in zip(list01, list02)}
print(dict01)

dict02 = {item:item*item for item in range(1, 11)}
print(dict02)

