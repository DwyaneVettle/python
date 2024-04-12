#  c第五章 Python字典与元组

## 1.字典

### 1.1.什么是字典

​	**字典**是Python内置数据结构之一，与列表一样是一个可变序列。它以键值对(key-value)的方式储存，是一个无序的序列。格式如下：

```python
dictionary = {'key1':value1, 'key2':value2, 'key3':value3}
其中：dectionary是字典名，字典元素用{}来包裹，key:value之间用冒号分隔，每个键值对之间用逗号隔开
```

![image-20220121205913624](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202403260915008.png)

​	**字典的实现原理和查字典类似，查字典是根据部首或拼音查找对应页码，Python中字典是根据key查找value所在的位置。**

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171706683.png" alt="image-20220121205913624" style="zoom:50%;" />

![image-20221031203836986](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171706684.png)

### 1.2.创建字典

​	创建字典和创建列表一样，有两种方式：

- 使用花括号的方式：

```python
gdp = {'四川': 5000, '湖北': 4500, '福建': 4400, '北京': 3000}
print(gdp)
print(type(gdp))
```

- 使用内置函数dict():

```python
student = dict(name='micheal', age=20)
print(student)
```

- 创建空字典：

```python
d = {}
print(d)
```



### 1.3.字典的查询

​	获取字典元素的方式有两种：

```python
[]取值------>gdp['四川']
get()方法-------->gdp.get('四川')
```

- []取值和使用get()取值的区别
  - []如果字典中不存在指定的key，则抛出KeyError异常；
  - get()方法取值，如果字典中不存在指定的key，不会抛出KeyError，而是返回None，可以通过参数设置默认的value，以便指定的key不存在时返回。

```python
# 字典的获取-[]
gdp = {'四川': 5000, '湖北': 4500, '福建': 4400, '北京': 3000}
print(gdp['四川'])
# print(gdp['重庆'])  # KeyError: '重庆'

# 字典的获取-get()
s = gdp.get('四川')
print(s)
c = gdp.get('重庆')
print(c)  # None
print(gdp.get('广东', 8000))  # 8000是广东不存在是提供的默认值
```



### 1.4.字典元素的判断和元素删除

​	字典key的判断可以用in和not in来判断。

```python
# 判断元素是否存在与字典中
gdp = {'四川': 5000, '湖北': 4500, '福建': 4400, '北京': 3000}
print('福建' in gdp)
print('北京' not in gdp)
```

​	删除字典元素可以用del来删除指定元素，删除的是整个键值对：

```python
del gdp['北京']
print(gdp)
```

​	同样可以用clear()方法清空整个字典：

```python
gdp.clear()
print(gdp)
```



### 1.5.新增、修改字典元素

​	新增字典元素只需要将字典中增减对应键值对就可以了.

```python
# 新增
gdp = {'四川': 5000, '湖北': 4500, '福建': 4400, '北京': 3000}
gdp['江苏'] = 7800
print(gdp)
# 修改
gdp['江苏'] = 8000
print(gdp)
```



### 1.6.字典的视图操作

​	获取字典视图的三个方法：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202403260915841.png" alt="image-20220121214652263" style="zoom:80%;" />

```python
# 获取字典视图
gdp = {'四川': 5000, '湖北': 4500, '福建': 4400, '北京': 3000}
keys = gdp.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有key组成的视图转成列表
values = gdp.values()
print(values)
print(type(values))
print(list(values))
items = gdp.items()
print(items)
print(list(items))  # 元组
```



### 1.7.字典元素的遍历

​	遍历的方式如下：

```python
for item in gdp:
    print(item)
```

```python
# 获取字典视图
gdp = {'四川': 5000, '湖北': 4500, '福建': 4400, '北京': 3000}
for item in gdp:
    print(item, gdp[item])
```



```python
# 1. 创建
# 空
dict01 = {}
dict01 = dict()
# 默认值
dict01 = {"wj":100,"zm":80,"zr":90}
dict01 = dict([("a","b"),("c","d")])
print(dict01)

# 2.　查找元素(根据ｋｅｙ查找ｖａｌｕｅ)
print(dict01["a"])
# 如果ｋｅｙ不存在，查找时会错误.
if "xtq" in dict01:# 如果存在key
    print(dict01["qtx"])

# 3.　修改元素(之前存在ｋｅｙ)
dict01["a"] = "BB"

# 4. 添加(之前不存在ｋｅｙ)
dict01["e"] = "f"

# 5. 删除
del dict01["a"]

print(dict01)
# 6. 遍历（获取字典中所有元素）

# 遍历字典，获取key
for key in dict01:
    print(key)
    print(dict01[key])

# 遍历字典，获取value
for value in dict01.values():
    print(value)

# 遍历字典，获取键值对key value(元组).
# for item in dict01.items():
#     print(item[0])
#     print(item[1])

for k,v in dict01.items():
    print(k)
    print(v)
```



### 1.8.字典的特点

​	字典的特点有如下几个：

- 字典中所有的元素都是一个key-value对，key不允许重复，value可以重复；
- 字典中的元素是无序的；
- 字典中的key必须是不可变对象；
- 字典也可以根据需要动态伸缩；
- 字典会浪费较大的内存，是一种使用空间换时间的数据结构。

```python
# 字典的特点
student = {'name': '张三', 'name': '李四'}
print(student)
"""student = {'name': '张三', 'name': '张三'}
print(student)"""
lst = [10, 20, 30]
lst.insert(1, 100)
print(lst)
student = {lst:100}
print(student)  # TypeError: unhashable type: 'list'
```



### 1.9.使用字典生成式

​	在Python中也可以使用内置函数zip()来生成字典。它用于将可迭代对象作为参数，将对象中对应的参数打包成一个元组，然后返回这些由元组组成的列表。

```python
{k:v for k,v in zip(key,value)}
```



```python
items = ['Fruits', 'Books', 'Others']
prices = [100, 101, 102]
s = {item.upper(): price for item, price in zip(items, prices)}
print(s)
```

```python
item.upper():price是遍历出来的单个对象组成键值对的形式，并全部转换成大写；
for item,price表示遍历的变量
zip(items,prices)表示打包的列表对象。
```

```python
"""
    字典推导式
"""
# 1 2 3 4 ... 10 -> 平方
dict01 = {}
for item in range(1, 11):
    dict01[item] = item ** 2
print(dict01)
# 推导式:
dict02 = {item: item ** 2
          for item in range(1, 11)}
print(dict02)

# 只记录大于５的数字
dict01 = {}
for item in range(1, 11):
    if item >5:
        dict01[item] = item ** 2

print(dict01)

dict02 = {item: item ** 2
          for item in range(1, 11) if item >5}
print(dict02)
```



### 1.10.练习

1.在控制台中循环录入商品信息(名称,单价)，如果名称输入空字符,则停止录入，将所有信息逐行打印出来。

```python
dict_commodity_info = {}
while True:
    name = input("请输入商品名称：")
    if name == "":
        break
    price = int(input("请输入商品单价："))
    dict_commodity_info[name] = price

for key,value in dict_commodity_info.items():
    print("%s商品单价是%d"%(key,value))
```



2.在控制台中循环录入学生信息(姓名,年龄,成绩,性别)，如果名称输入空字符, 则停止录入，将所有信息逐行打印出来。

```python
"""
# 字典内嵌列表:
{
    "张无忌":[28,100,"男"],
}
"""
dict_student_info = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    dict_student_info[name] = [age, score, sex]

# 打印所有学生信息
for name,list_info in dict_student_info.items():
    print("%s的年龄是%d,成绩是%d,性别是%s"%(name,list_info[0],list_info[1],list_info[2]))
```

```python
"""
# 字典内嵌字典:
{
    "张无忌":{"age":28,"score":100,"sex":"男"},
}
"""
dict_student_info = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    dict_student_info[name] = {"age": age, "score": score, "sex": sex}

for name, dict_info in dict_student_info.items():
    print("%s的年龄是%d,成绩是%d,性别是%s" %
          (name, dict_info["age"],
           dict_info["score"], dict_info["sex"]))
```



```python
"""
# 列表内嵌字典:
[
    {"name":"张无忌","age":28,"score":100,"sex":"男"},
]
"""
list_student_info = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    dict_info = {"name": name, "age": age, "score": score, "sex": sex}
    list_student_info.append(dict_info)

for dict_info in list_student_info:
    print("%s的年龄是%d,成绩是%d,性别是%s" % (dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))
# 获取第一个学生信息
dict_info = list_student_info[0]
print("第一个录入的是：%s,年龄是%d,成绩是%d,性别是%s" % (dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))

```



- **列表和字典如何选择？**

选择策略：根据具体需求，结合优缺点，综合考虑(两害相权取其轻).
    字典：
        优点：根据键获取值，读取速度快；
        　　　代码可读性相对列表更高(根据键获取与根据索引获取).
        缺点：内存占用大；
        　　　获取值只能根据键,不灵活.
    列表：
        优点：根据索引/切片，获取元素更灵活.
                    相比字典占内存更小。
        缺点：通过索引获取，如果信息较多，可读性不高.

练习:在控制台中录入多个人的多个喜好,输入空字符停止。

```python
"""
练习:在控制台中录入多个人的多个喜好,输入空字符停止.
例如:请输入姓名：
    请输入第1个喜好：
    请输入第2个喜好：
    ...
    请输入姓名：
    ...
   最后在控制台打印所有人的所有喜好.
[
    {“无忌”:[赵敏,周芷若,小赵]}
]

list_person_bobby = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    dict_person = {name:[]}
    list_person_bobby.append(dict_person) 
    while True:
        bobby = input("请输入喜好：")
        if bobby == "":
            break
        dict_person[name].append(bobby)
"""

"""
{
    “无忌”:[赵敏,周芷若,小赵]
}
"""
dict_person_bobby = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    dict_person_bobby[name] = []
    while True:
        bobby = input("请输入喜好：")
        if bobby == "":
            break
        dict_person_bobby[name].append(bobby)

for name, list_bobby in dict_person_bobby.items():
    print("%s喜欢：" % name)
    for item in list_bobby:
        print(item)
```

作业：

1.存储全国各个城市的景区与美食(不用录入),在控制台中显示出来.
  　北京：
        景区：故宫,天安门,天坛.
        美食: 烤鸭,炸酱面,豆汁,卤煮.
    四川:
        景区：九寨沟,峨眉山,春熙路．
        美食: 火锅,串串香,兔头

## 2.元组-tuple	

​	元组是由一系列变量组成的不可变的序列容器。不可变是指一旦创建，不可以再添加/删除/修改元素。



### 2.1.元组的基本操作

- **创建元组**

  - 创建空元组

  ```python
  元组名 = ()
  元组名 = tuple()
  ```

  - 创建非空元组

  ```python
  元组名 = (10,)
  元组名 = (10,20,30)
  元组名 = 10,20,30
  元组名 = tuple(可迭代对象)
  ```

- 两个方法：

```python
count(argument)  -- 返回对应元素的个数
index(argument)  -- 返回对应元素的下标
```



- **获取元素**

  - 索引
  - 切片

- **遍历元组**

  - 正向

  ```python
  for 变量名 in 列表名:
  		变量名就是元素
  ```

  

  - 反向

  ```python
  for 索引名 in range(len(列表名)-1,-1,-1):
  		元祖名[索引名]就是元素
  ```

  ```python
  # 1.创建元组
  tuple1 = ()  # 空元组
  tuple2 = tuple()
  
  # 2.创建具有默认值的元组
  tuple3 = (1, 2, 3)
  print(tuple3)
  
  # 3.列表-->元组
  tuple1 = tuple(['a', 'b'])
  # 4.元组-->列表
  list01 = list(tuple1)
  
  # 5.如果元组只有一个元素，需要在元素后加逗号
  tuple4 = (100)
  print(type(tuple4))  # <class 'int'>
  tuple5 = (100,)
  print(type(tuple5))  # <class 'tuple'>
  
  # 6.获取元素（索引、切片）
  tuple01 = ("a", "b", "c", "d")
  e01 = tuple01[0]
  print(e01)
  print(type(e01))
  e01 = tuple01[-2:]
  print(e01)
  print(type(e01))
  
  tuple02 = (100, 200)
  a, b = tuple02
  print(a)
  print(b)
  
  # 7.遍历元组
  for item in tuple02:
      print(item)
  
  # 反向遍历
  for i in range(len(tuple02)-1, -1, -1):
      print(tuple02[i])
  ```



### 2.2.元组的作用

1. 元组与列表都可以存储一系列变量，由于列表会预留内存空间，所以可以增加元素。
2. 元组会按需分配内存，所以如果变量数量固定，建议使用元组，因为占用空间更小。
3. 应用：
   1. 变量交换的本质就是创建元组：x, y =(y, x)
   2. 格式化字符串的本质就是创建元祖："姓名:%s, 年龄:%d"  % ("micheal", 15)



### 2.3.练习

```python
"""
    练习:借助元组完成下列功能.
"""
# month = int(input("请输入月份："))
#
# if month < 1 or month > 12:
#     print("输入有误")
# elif month == 2:
#     print("２８天")
# elif month == 4 or month == 6 or month == 9\
#         or month == 11:
#     print("３０天")
# else:
#     print("３１天")

# 方式１：元组
# month = int(input("请输入月份："))
#
# if month < 1 or month > 12:
#     print("输入有误")
# elif month == 2:
#     print("２８天")
# elif month in (4,6,9,11):
#     print("３０天")
# else:
#     print("３１天")

# 方式2:
month = int(input("请输入月份："))
if month < 1 or month > 12:
    print("输入有误")
else:
    # 将每月天数存入元组
    day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    print(day_of_month[month - 1])
```

