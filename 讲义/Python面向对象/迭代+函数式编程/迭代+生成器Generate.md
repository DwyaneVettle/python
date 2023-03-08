# 迭代+生成器Generate

## 1.迭代

​	每次对过程的重复称为一次“迭代”，而每次迭代得到的结果会作为下一次迭代的初始值。例如：循环获取容器中的元素。



### 1.1.可迭代对象iterable

​	定义：具有`__iter__`函数的对象，可以返回迭代器对象。

​	语法：

```python
# 创建
class 可迭代对象名称：
	def __iter__(self):
        return 迭代器
    
    def __next__(self):
        if 没有元素:
            raise StopIteration
        return 聚合元素对象
    
# 使用
for 变量名 in 可迭代对象:
    语句
```



```python
"""
    可迭代对象
"""

# 可迭代对象  -- 容器
list01  = [43,3,4,5,567]
# 迭代过程
# for item in list01:
#     print(item)

# 迭代原理
# 面试题：for循环的原理是什么？
#        答：1. 获取迭代器
#           2. 循环获取下一个元素
#           3. 遇到异常停止迭代

#        可以被for的条件是什么？
#        答：能被for的对象必须具备__iter__方法
#        答：能被for的对象是可迭代对象

#1. 获取迭代器
iterator = list01.__iter__()
#2. 循环获取下一个元素
while True:
    try:
        item = iterator.__next__()
        print(item)
    #3. 遇到异常停止迭代
    except StopIteration:
        break# 退出循环
```

- 练习：

  1.使用迭代器原理，遍历元组("铁扇公主","铁锤公主",“扳手王子”)

```python
tuple01 = ("铁扇公主","铁锤公主","扳手王子")
# for item in tuple01:
#     print(item)


iterator = tuple01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
```



​	2.不使用for，获取字典所有数据{"铁扇公主":101,"铁锤公主":102,“扳手王子”:103}

```python
dict01 = {"铁扇公主": 101, "铁锤公主": 102, "扳手王子": 103}

iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key, dict01[key])
    except StopIteration:
        break
```



### 1.2.迭代器对象iterator

定义：可以被`next()`函数调用并返回下一个值的对象。

语法：

```python
class 迭代器类名:
    def __init__(self,聚合对象):
        self.聚合对象 = 聚合对象
        
    def __next__(self):
        if 没有元素:
            raise StopIteration
        return 聚合对象
# 聚合对象通常是容器对象
```

迭代器对象的作用：使用者只需通过一种方式，便可简洁明了的获取聚合对象中各个元素，而又无需了解其内部结构。

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171711678.jpg" style="zoom:50%;" />

```python
"""
    迭代器
"""


class Skill:
    pass


class SkillManager:
    """
        技能管理器  可迭代对象
    """

    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        # 创建一个迭代器对象,并传递需要迭代的数据。
        return SkillIterator(self.__skills)


class SkillIterator:
    """
        技能迭代器
    """

    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        # 如果没有数据了，则抛出异常
        if self.__index > len(self.__target) - 1:
            raise StopIteration

        # 返回下一个数据
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


manager = SkillManager()
manager.add_skill(Skill())
manager.add_skill(Skill())
manager.add_skill(Skill())

for item in manager:
    print(item)

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
```

- 练习：

  1.图形管理器记录多个图形，迭代图形管理器对象。

  ```python
  # 练习：图形管理器记录多个图形
  #      迭代图形管理器对象
  # 图形
  class Graphic:
      pass
  
  # 图形管理器
  class GraphicManager:
      """
          图形管理器，可迭代对象(参与for)
      """
      def __init__(self):
          self.__graphics = []
  
      def add_graphic(self, graphic):
          self.__graphics.append(graphic)
  
      def __iter__(self):
          return GraphicIterator(self.__graphics)
  
  
  class GraphicIterator:
      """
          图形迭代器（获取下一个数据）
      """
      def __init__(self, target):
          self.__target = target
          self.__index = 0
  
      def __next__(self):
          if self.__index > len(self.__target) - 1:
              raise StopIteration
          temp = self.__target[self.__index]
          self.__index += 1
          return temp
  
  
  manager = GraphicManager()
  manager.add_graphic(Graphic())
  manager.add_graphic(Graphic())
  manager.add_graphic(Graphic())
  # for item in manager:
  #     print(item)
  
  iterator = manager.__iter__()
  while True:
      try:
          item = iterator.__next__()
          print(item)
      except StopIteration:
          break
  
  ```

  2.创建员工管理器记录多个员工，迭代员工管理器

  ```python
  # author by Michealzou@126.com
  # 2022/11/1 21:41
  # 员工管理器记录多个员工，迭代员工管理器
  class Employee:
      pass
  
  
  class EmployeeManager:
      def __init__(self):
          self.employees = []
  
      def add_employee(self, emp):
          self.employees.append(emp)
  
      def __iter__(self):
          return EmployeeItrater(self.employees)
  
  class EmployeeItrater:
      def __init__(self, target):
          self.__target = target
          self.__index = 0
  
      def __next__(self):
          if self.__index > len(self.__target) - 1:
              raise StopIteration
          temp = self.__target[self.__index]
          self.__index += 1
          return temp
  
  
  # 创建对象
  employee = EmployeeManager()
  employee.add_employee(Employee())
  # 遍历
  # for emp in employee:
  #     print(emp)
  iterator = employee.__iter__()
  while True:
      try:
          items = iterator.__next__()
          print(items)
      except StopIteration:
          break
  ```

  3.练习：练习：定义MyRange类，实现下列功能
   `for item in range(10):
          print(item)`
  
  ```python
  """
      练习：定义MyRange类，实现下列功能
      for item in range(10):
          print(item)
  """
  
  
  class MyRange:
      def __init__(self, stop_value):
          self.stop_value = stop_value
  
      def __iter__(self):
          return MyRangeIterator(self.stop_value)
  
  
  class MyRangeIterator:
      def __init__(self, end_value):
          self.__end_value = end_value
          self.__number = 0
  
      def __next__(self):
          if self.__number == self.__end_value:
              raise StopIteration
  
          temp = self.__number
          self.__number += 1
          return temp
  
  # next一次，计算一次，返回一次。
  for item in MyRange(99999999999999):
      print(item)
  
  ```
  
  如上代码是通过MyRange调用了MyRangeIterator的`__next__()`方法，但MyRangeIterator类可以省略，因为它只是一种规则，标记这种规则的类需要`__next()--`方法而已。我们可以采用`yield`关键字来代替这种规则，改造后的代码如下：
  
  ```python
  """
     迭代器 --> yield
     练习: 将迭代器版本的图形管理器改为yield实现.
  """
  
  
  class MyRange:
      def __init__(self, stop_value):
          self.stop_value = stop_value
  
      def __iter__(self):
          # return MyRangeIterator(self.stop_value)
          # 0 --> self.stop_value
          # yield 作用: 将下列代码改为迭代器模式的代码.
          # 生成迭代器代码的大致规则:
          # 1. 将yield以前的语句定义在next方法中
          # 2. 将yield后面的数据作为next方法返回值
          number = 0
          while number < self.stop_value:
              yield number
              number += 1
  
          # print("准备数据")
          # yield 0
          # print("准备数据")
          # yield 1
          # print("准备数据")
          # yield 2
          # # ...
  
  """
  class MyRangeIterator:
      def __init__(self, end_value):
          self.__end_value = end_value
          self.__number = 0
  
      def __next__(self):
          if self.__number == self.__end_value:
              raise StopIteration
  
          temp = self.__number
          self.__number += 1
          return temp
  """
  
  # next一次，计算一次，返回一次。
  # for item in MyRange(10):
  #     print(item)
  
  my01 = MyRange(10)
  iterator = my01.__iter__()
  while True:
      try:
          item = iterator.__next__()
          print(item)
      except StopIteration:
          break
  ```
  
  以上`yield`的作用：将代码改为迭代器模式的代码.
   **生成迭代器代码的大致规则:**
  
          	 1. 将yield以前的语句定义在next方法中
                    	2. 将yield后面的数据作为next方法返回值

## 2.生成器generator

定义：能够动态(循环一次计算一次返回一次)提供数据的可迭代对象。

作用：在循环过程中，按照某种算法推算数据，不必创建容器存储完整的结果，从而节省内存空间。数据量越大，优势越明显。

以上作用也称之为延迟操作或惰性操作，通俗的讲就是在需要的时候才计算结果，而不是一次构建出所有结果。



### 2.1.生成器函数

定义：含有yield语句的函数，返回值为生成器对象。

语法：

```python
# 创建
def 函数名():
    ...
    yield 数据
    ...
    
# 调用
for 变量名 in 函数名():
    语句
# 调用生成器函数将返回一个生成器对象，不执行函数体。
# yield翻译为”产生”或”生成”
```

 **执行过程：**

(1) 调用生成器函数会自动创建迭代器对象。

(2) 调用迭代器对象的__next__()方法时才执行生成器函数。

(3) 每次执行到yield语句时返回数据，暂时离开。

(4) 待下次调用__next__()方法时继续从离开处继续执行。

**原理**：生成迭代器对象的大致规则如下

	- 将yield关键字以前的代码放在next方法中。
	- 将yield关键字后面的数据作为next方法的返回值。



### 2.2.内置生成器

- **枚举函数enumerate**

 语法：

```python
for 变量 in enumerate(可迭代对象):

   语句

 

for 索引, 元素in enumerate(可迭代对象):

  语句
```



作用：遍历可迭代对象时，可以将索引与元素组合为一个元组。

- **zip**

语法：

```python
for item in zip(可迭代对象1, 可迭代对象2….):

  		语句
```



作用：将多个可迭代对象中对应的元素组合成一个个元组，生成的元组个数由最小的可迭代对象决定。

```python
"""
    yield --> 生成器
"""
"""
class MyRange:
    def __init__(self, stop_value):
        self.stop_value = stop_value

    def __iter__(self):
        number = 0
        while number < self.stop_value:
            yield number
            number += 1

my01 = MyRange(10)

iterator = my01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
"""

"""
# 生成器原理
class MyGenerator:
    # 生成器 = 可迭代对象 + 迭代器
    def __init__(self,stop_value):
        self.begin = 0
        self.stop_value = stop_value
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.begin >= self.stop_value:
            raise StopIteration
            
        temp = self.begin
        self.begin+=1
        return temp
"""


def my_range(stop_value):
    number = 0
    while number < stop_value:
        yield number
        number += 1

my01 = my_range(10)
print(type(my01), dir(my01))# dir-内置函数 获取对象所有成员

print(id(my01.__iter__()), id(my01))

for item in my01:
    print(item)
```

- **练习：**使用生成器实现从列表[4,5,566,7,8,10]中选出所有偶数，结果存入另外一个列表中。

```python
# 使用生成器实现从列表[4,5,566,7,8,10]中选出所有偶数，结果存入另外一个列表中。
list01 = [4, 5, 566, 7, 8, 10]

# 第一种方式-常规方式
def get_even01():
    result = []
    for item in list01:
        if item % 2 == 0:
            result.append(item)
    return result


re = get_even01()
for item in re:
    print(item)

# 第二种方式-迭代器思想
def get_even02():
    for item in list01:
        if item % 2 == 0:
            yield item


g01 = get_even02()
for item in g01:
    print(item)

```



### 2.3.生成器表达式

定义：用推导式形式创建生成器对象。

 语法：

```python
变量 = ( 表达式 for 变量 in 可迭代对象 [if 真值表达式] )
```



