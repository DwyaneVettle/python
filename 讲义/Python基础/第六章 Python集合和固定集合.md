# 第六章 Python集合和固定集合



## 1.集合

​	列表：重复、可变

​	字典：k不重复、v重复，可变

​	集合是由一系列**不重复的不可变类型**变量组成的可变映射容器。相当于只有键没有值的字典。我们可以对它进行 同时还可以求交集、并集、补集等。**集合的定义用set()。**

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171706827.jpg" style="zoom:50%;" />

### 1.1.集合的基础操作

- **创建空集合**

```python
集合名 = set()
集合名 = set(可迭代对象)
```

- **创建有默认值的集合**

```python
集合名 = {1,2,3}
集合名 = set(可迭代对象)
```

- **添加元素**

```python
集合名.add(元素)
```

- **删除元素**

```python
集合名.discard(元素)
集合名.remove(元素)
集合名.pop()			# 删除任意一个
```

- **获取所有元素**

```python
for item in 集合名:
	print(item)
```

- **数学运算**
  - 交集&：返回共同元素
  - 并集|：返回不重复元素
  - 补集-：返回只属于前者的元素
  - 补集^:返回不同的元素
  - 子集<:判断一个集合的所有元素是否完全在另一个集合中
  - 超集>:判断一个集合是否具有另一个集合的所有元素
  - 相同或不同== !=：判断一个集合中的所有元素是否和另一个集合相同

```python
# 1.创建集合
set01 = set()
set02 = set('abc')
print(set02)
set03 = {"a", "b", "c"}
print(set03)
# 2.添加元素
set03.add("d")
print(set03)
# 3.删除元素
set03.remove("a")
print(set03)
set03.discard("b")
print(set03)
# 4.获取所有元素
for item in set03:
    print(item)
# 5.数学运算
set01 = {1, 2, 3}
set02 = {2, 3, 4}
# 交集
print(set01 & set02)
# 并集
print(set01 | set02)
# 补集
print(set01 ^ set02)
print(set01 - set02)
# 子集
set03 = {1, 2}
print(set03 < set01)
# 超集
print(set03 > set01)
```



### 1.2.练习1

在控制台中循环录入字符串，输入空字符串停止，打印所有不重复的文字

```python
# 练习1: 在控制台中循环录入字符串，输入空字符停止.
#       打印所有不重复的文字

set_result = set()
while True:
    str_input = input("请输入：")
    if str_input == "":
        break
    set_result.add(str_input)

print(set_result)
```



### 1.3.练习2

岗位练习，经理岗位的名单有曹操、刘备、孙权；技术岗位的有曹操、刘备、关羽、张飞，问

1. 是经理也是技术的有谁？
2. 是经理，不是技术的有谁?
3. 是技术，不是经理的有谁?
4. 张飞是经理吗?
5. 身兼一职的都有谁?
6. 经理和技术总共有都少人?

```python
set01 = {"曹操", "刘备", "孙权"}
set02 = {"曹操", "刘备", "张飞", "关羽"}
print(set01 & set02)
print(set01 - set02)
print(set02 - set01)
print("张飞" in set01)
print(set01 ^ set02)
print(len(set01 | set02))
```





## 2.固定集合

​	固定集合(frozenset)是指**不可变的集合**。固定集合的作用是可以作为集合的键，也可以作为集合的值。因为是固定集合，所以我们**只能创建它，而不能修改它**。并且它的运算方式和集合set是等效的。

- **创建集合**

```python
集合名 = frozenset(可迭代对象)
```

```python
"""
    固定集合
"""
set01 = frozenset([1,2,3,3,5])
list02 = list(set01)
print(set01)
print(list02)
```

