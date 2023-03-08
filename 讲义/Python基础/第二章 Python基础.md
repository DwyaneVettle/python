# 第二章 Python基础



## 1.对象

​	Python中一切皆为对象，每个对象由：标识(identity)、类型(type)、值(value)组成。它们的具体作用分别为：

- **标识：**用于唯一标识对象，通常对应于对象在计算机内存中的地址，使用内置对象id(object)可返回对象object的标识。
- **类型：**用于表示对象存储的数据类型，类型可以限制对象的取值范围，以及可执行的操作。可以使用type(object)获取对象的所属类型。
- **值：**表示对象所存储的数据信息。使用print(object)可以打印出值。

**对象的本质是一个内存块，拥有特定的值，支持特定类型的相关操作。**

```python
print(id(a))
print(id(b))
print(id(c))

print(type(a))
print(type(b))
print(type(c))

print(a)
print(b)
print(c)
# 输出结果
2415415518320
2415418637072
2415415517936
<class 'float'>
<class 'str'>
<class 'int'>
3.1415926
爱老虎油
131420
```

​	其在内存中的模式如下：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171702339.png" alt="image-20220111185122708" style="zoom:67%;" />

**引用**

​	在Python中，变量也被称为对象的引用，因为变量存储的就是对象的地址，变量通过地址引用了对象。

​	**变量位于：栈内存**

​	**对象位于：堆内存**

- **Python是动态类型语言：**变量不需要显示声明类型，根据变量引用对象，Python解释器会自动确定变量类型；
- **Python是强类型语言：**每个对象都有数据类型，只支持该类型支持的相关操作。



## 2.标识符的命名规则

​	标识符是用来声明变量、函数、类、模块等的代称，标识符的声明有如下几个规则：

1.区分大小写；

2.第一个字符必须为字母、下划线，其后可以跟字母、下划线、数字等；

3.以双下划线开头或结尾的标识符通常有特殊的含义，尽量避免这种写法。如__init__是类的构造函数；

4.不能使用关键字定义标识符，如if、else等。

可以使用Python帮助系统查看Python的关键字有哪些：

```py
>>>help()
help > keywords
```



<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171702340.png" alt="image-20220111194403284" style="zoom: 67%;" />

**在命令行模式中按F1可以打开Python官方文档进行查阅。**

以上我们列出了Python标识符的语法规则，在实际生产中，我们还要遵循以下命名规则：

| 类型       | 规则                                                         | 例子               |
| ---------- | ------------------------------------------------------------ | ------------------ |
| 模块和包名 | 全小写字母，尽量简单。若多个单词之间用下划线                 | math  os           |
| 函数名     | 全小写字母，多个单词之间用下划线隔开                         | phone, my_fun      |
| 类名       | 首字母大写，采用驼峰原则。多个单词时， 每个单词第一个字母大写，其余部分小写 | MyPhone、MyClass、 |
| 常量名     | 全大写字母，多个单词使用下划线隔开                           | SPEED、MAX_SPEED   |



## 3.变量

### 	3.1.变量的声明和赋值

变量的声明和赋值用于将一个变量绑定到一个对象上，格式如下：

```python
变量名 = 表达式
```

​	最简单的表达式就是字面量。比如：a = 123 。 运行过程中，解释器先运行右边的表达式，生成一个代表表达式运算结果的对象；然后，将这个对象地址赋值给左边的变量。

​	变量在使用之前必须先初始化--赋值：

![image-20220112194941606](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171702341.png)



### 3.2.删除变量和垃圾回收机制

​	要想删除某个变量，可以通过del语句删除不再使用的变量：

```python
del 变量名
```

```python
a = 100
print(a)
del a
print(a)
```

​	**如果对象没有变量引用，就会被垃圾回收器回收，清空内存空间。**



### 	3.3.链式赋值和系列解包赋值

​	在实际的开发过程中，为了方便多个变量的赋值，Python提供了支持链式赋值的方法，能将同一个对象赋值给多个变量：

```python
x=123
y=123
x=y=123
print(x)
print(y)
```

​	而与链式赋值类似的是系列解包赋值，系列解包赋值表示将一系列数据赋值给对应相同个数的变量，前提是个数必须保持一致：

```python
a,b,c=1,2,3					=> a=1,b=2,c=3
```

​	使用系列解包赋值就可以实现最为简单的变量值的交换：

```python
x,y=4,5
x,y=y,x
print(x,y)
```

变量内存图：

```python
# 语法：
# 变量名称　= 对象
# 例如：
name = "张无忌"
print(name)
# 语义：内存图
# 变量名：真实内存地址的别名
#        见名知意
# 赋值号：将右边对象的地址复制给左边内存空间。

name = "赵敏"
a01 = a02 = "周芷若"
b01, b02 = "苏大强", "苏明玉"
class_name = "1905"
```



![image-20220907210706462](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171702342.png)

## 4.常量

​	Python不支持常量，没有语法规则限制改变一个常量的值。我们只能约定常量的命名规则，以及在程序上不对常量的值进行修改。

​	**常量名一般采用大写的方式。**

```python
MAX_SCORE=100
print(MAX_SCORE)								# 100
MAX_SCORE=120									# 逻辑上不能限制，但实际上可以改
print(MAX_SCORE)								# 120
```



## 5.数据类型

​	Python中常见的数据类型有整型(int)、浮点型(float)、布尔型(bool)、字符串型(str)。 



### 5.1.整型

​	英文名integer，简写为int，可以表示正数、负数和零。在计算机中，整型有不同的进制表示形式，十进制是默认的进制，二进制以0b开头，八进制以0o开头，十六进制以0x开头。

| 进制     | 基本数           | 逢几进一 | 表示形式  |
| -------- | ---------------- | -------- | --------- |
| 十进制   | 0123456789       | 10       | 119       |
| 二进制   | 01               | 2        | 0b1110101 |
| 八进制   | 01234567         | 8        | 0o117     |
| 十六进制 | 0123456789ABCDEF | 16       | 0x88F     |

```python
# 整数类型，可以表示正整数、负整数和零
n1 = 90
n2 = -76
n3 = 0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
# 整数可以表示为二进制、八进制、十进制、十六进制
print('十进制', 118)
print('二进制', 0b01010001)
print('八进制', 0o117)
print('十六进制', 0x88F)
```

### 5.2.浮点类型

​	浮点类型的数据由整数部分和小数部分组成。

```python
a = 3.1415926
print(a, type(a))
```



​	在计算机中，浮点数的存储都是不精确的，使用浮点数进行计算时，可能出现小数位数不确定的情况。如：

```python
print(1.1+2.2) # 3.3000000000000003
print(1.1+2.1) # 3.2
```

​	要想解决浮点数计算不精确的问题，需要导入Python的decimal模块：

```python
from decimal import Decimal								# 导入decimal模块
print(Decimal('1.1') + Decimal('2.2'))
```



一般情况下，足够小的小数用科学计数法表示：

```python
# 科学计数法 1.235e-32
print(0.00000000000000000000000000000001235)
```



### 5.3.布尔类型

​	布尔类型即用来表示真或者假的值，用True来表示真，用False来表示假，当然，布尔值也可以转换成整数来表示，转换成整数时，True=1，False=0:

```python
b1 = True
b2 = False
print(b1,type(b1))
print(b2,type(b2))
print(1 == 1)									# True
print(1 != 1)									# False
print(True+1)									# 2
print(False+1)									# 1
```

### 5.4.字符串类型

​	字符串又被称为不可变的字符序列，可以使用单引号''，也可以使用双引号""和三引号"''"来定义，单引号和双引号定义的字符串必须在一行，三引号定义的字符串可以分布在连续的多行中。

```python
str1 = '人生苦短，快学Python'
str2 = "人生苦短，快学Python"
str3 = '''人生苦短，
        我用Python'''
str4 = """人生苦短，
        我用Python"""
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))
```

#### 	5.4.1.字符串格式化	

​	Python的字符串可通过占位符%，format()方法，f-strings三种方式实现格式化输出

- **占位符%**

  利用%占位符可以为真实值预留位置，并说明真实值应呈现的格式：

```python
name = 'Python'
print('你好，我叫%s' % name)
```

```python
# 一个字符串可以同时含多个占位符
name = 'java'
age = 27
print('我叫%s,今年%d岁了' % (name, age))
```

| 符号 | 说明                    | 符号 | 说明                    |
| ---- | ----------------------- | ---- | ----------------------- |
| %s   | 字符串                  | %X   | 十六进制整数（A-F大写） |
| %d   | 十进制整数              | %e   | 指数（底写为e）         |
| %o   | 八进制整数              | %f   | 浮点数                  |
| %x   | 十六进制整数（a-f小写） |      |                         |

​	如果使用占位符和对应的变量类型不匹配会出现异常：

```python
name = 'java'
age = '27'
print('我叫%s,今年%d岁了' % (name, age))
# TypeError: %d format: a real number is required, not str
```

- **format()方法**

  format()方法同样可以对字符串格式化输出，与占位符%不同的是，使用format()不需要关注变量的类型，其格式如下：

```python
<字符串{}>.format(<参数列表>)
```

```python
name = 'Python'
age = 31
print('你好，我的名字是:{}，今年{}岁了'.format(name, age))
```

​	如果字符串中包含多个"{}",并且{}中没有指定任何序号，那么默认按照{}出现的顺序匹配faomat()方法里的参数，如果明确指定了序号，那么按照序号对应的参数进行替换：

```python
name = 'Python'
age = 31
print('你好，我的名字是:{1}，今年{0}岁了'.format(age, name))
```

- **f-strings**

  f-strings是从Python3.6开始加入的标准库内容，它提供了更简洁的方式格式化字符串，f-strings本质上不再是字符串常量，而是在运行时运算求值的表达式，所以效率更优于%和format()：

```python
address = '成都'
print(f'欢迎来到{address}')
name = '卡卡'
age = 40
gender = '男'
print(f'我最喜欢的球星{name}，他今年{age}岁，他的性别是{gender}')
```

#### 5.4.2.字符串的常见操作

- **字符串拼接**

  字符串的拼接可以直接用"+"来实现：

```python
str1 = '人生苦短，'
str2 = '快用Python。'
print(str1 + str2)
```

- **字符串替换**

  字符串的替换可以使用replace()方法来完成，语法格式为：

```python
str.replace(old, new, count)
# count为替换次数
# 注意： 替换次数如果查出子串出现次数，则替换次数为该子串出现次数
```

```python
str3 = '我是Micheal，今年30岁了。'
str4 = str3.replace('我', '他')
print(str4)
```

​	如果字符串没有找到匹配的子串，会直接返回原来的字符串：

```python
str3 = '我是Micheal，今年30岁了。'
str4 = str3.replace('他', '我')
print(str4)
```

```python
# replace() --- 替换    需求：把and换成he
myStr = 'hello world and Python and java and php'
new_str = myStr.replace('and', 'he')
print(myStr)   # hello world and Python and java and php
print(new_str)  # hello world he Python he java he php
# 原字符串调用了replace函数后，原有字符串中的数据并没做任何修改，修改后的数据是replace函数电动的返回值
# 说明：replace函数有返回值，返回值是修改后的字符串
# 字符串是不可变数据类型，数据是否可以改变划分为：可变类型 和 不可变类型
 
 
new_str = myStr.replace('and', 'he', 1)
print(new_str)  # hello world he Python and java and php
 
new_str = myStr.replace('and', 'he', 10)
print(new_str)  # hello world he Python he java he php
# 替换次数如果超出了子串出现的次数，表示替换所有这个子串
```



- **字符串分割**

  字符串的分割采用split()方法，语法格式为：

```python
str.split(sep = None, maxsplit = -1)
# 注意： num表示的是分割字符出现的次数，即将来返回数据个数为num+1个
```

```python
str5 = '1 2 3 4 5'
print(str5.split())  # 默认返回一个列表
str6 = 'a,b,c,d,e'
print(str6.split(','))
str7 = '人生苦短，快用Python'
print(str7.split('苦'))
```

```python
# split() --- 分割 --- 返回一个列表，丢失分割字符
myStr = 'hello world and Python and java and php'
list1 = myStr.split('and')
print(list1)  # ['hello world ', ' Python ', ' java ', ' php']
 
list1 = myStr.split('and', 2)
print(list1)  # ['hello world ', ' Python ', ' java and php']
```

注意： 如果分割字符是原有字符串中的子串，分割后则丢失该子串。

- **去除字符串两侧的空格**

  用strip()方法来去除祖父穿两侧的空格，语法格式为：

```python
str.strip(chars = None)
```

```python
str8 = ' 你好 '
print(str8.strip())
str9 = '%%hello%%'
print(str9.strip('%'))
```

- **合并字符串，即将多个字符串合并为一个新的字符串**

语法格式为：

```python
字符或字串.join(字符串组成的序列)
```

```python
# join() --- 合并列表里面的字符串数据为一个大字符串
myList = ['aa', 'bb', 'cc']
 
# 需求：最终结果为： aa...bb...cc
new_list = '...'.join(myList)
print(new_list)  # aa...bb...cc
 
new_list = '/'.join(myList)
print(new_list)  # aa/bb/cc
```



#### 5.4.3.字符串拼接问题

**1.str.join(str)和str+str的区别：**

当字符串连接数少时，+号的连续效率比join高，当字符串连接数多时，join的连接效率比+号高。

**2.三种拼接方法**

方法一：直接通过+号连接

```python
website  =  'python'  +  'tab'  +  '.com'
```

方法二：join()方法连接

```python
listStr  =  [ 'python' ,  'tab' ,  '.com' ] 
website  =  ''.join(listStr)
```

方法三：%替换

```python
website  =  '%s%s%s'  %  ( 'python' ,  'tab' ,  '.com' )
```

**三种拼接方法的区别：**

**方法1**，使用简单直接，但是网上不少人说这种方法效率低

之所以说python 中使用 + 进行字符串连接的操作效率低下，是因为python中字符串是不可变的类型，使用 + 连接两个字符串时会生成一个新的字符串，生成新的字符串就需要重新申请内存，当连续相加的字符串很多时(a+b+c+d+e+f+...) ，效率低下就是必然的了；

**方法2**，使用略复杂，但对多个字符进行连接时效率高，只会有一次内存的申请。而且如果是对list的字符进行连接的时候，这种方法必须是首选；

**方法3，**字符串格式化，这种方法非常常用，本人也推荐使用该方法。





#### 5.4.4.字符串的索引和切片

- **索引**

  字符串的所以可以通过正向和逆向两种方式进行索引，正向索引从0开始索引值依次加1，逆向索引从-1开始索引值依次减1：

  <img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171702343.png" style="zoom:67%;" />

  通过字符串的索引值可以获取指定的字符：

```python
str1 = 'Python'
print(str1[0])
print(str1[-2])
```

​	需要注意的是，索引值不能越界，否则会报越界异常。

- **切片**:都是从左至右

  切片用于截取目标对象中的一部分，其语法格式为：

```python
[起始:结束:步长]
```

​	切片的默认步长为1，需要注意的是切片获取的区间属于左闭右开型，即包含起始位，但不包含结束位。

```python
# 切片：切片用于截取目标对象中的一部分-切片只正序切片，无论传递下标是整数，还是负数，切片都是从左至右
"""
    语法：str[start:end:step]-包含start,不包含end
    start-开始切片开始的下标，正数表示正序，反之倒叙
    end-表示切片结束的下标
    step-切片的步长,默认步长为1，可以不传递,传递步长包含end个数
"""
str12 = 'python'  # th
print(str12[2:4])  # 正序
print("-----------")
print(str12[-4:-2])  # 倒叙
print(str12[1:5:3])  # y o
```

- **编码转换**

  - ord()：字转数
  - chr()：数转字

  ```python
  num01 = ord('a')
  print(num01)
  
  str01 = chr(97)
  print(str01)
  ```

  

### 5.5.数据类型的转换

​	在生产环境中，客户端传递过来的数据可能不是我们服务器端匹配的数据类型，亦或是连接不同类型的数据时会报错。比如：在用户注册的时候，用户输入电话号码看起来是整数类型，但往往服务器端和数据库作存储的时候是一个字符串类型，那么我们就需要我们实现类型的转换，方便服务器的读取和数据库的存储。在Python中，给我们提供了专门用于做数据类型转换的函数，我们可以方便的进行类型转换。

| 函数名  | 作用                       | 注意事项                                                     | 举例                   |
| ------- | -------------------------- | ------------------------------------------------------------ | ---------------------- |
| str()   | 将其他数据类型转换成字符串 | 也可以用引号转换                                             | str(123), '123'        |
| int()   | 将其他数据类型转换成整形   | 1、文字类或小数类字符串无法转换成整型；2、浮点类型转换成整型会抹零取整 | int('123'), int(9.8)   |
| float() | 将其他数据类型转换成浮点型 | 1、文字无法转换；2、整型转浮点型，末尾加.0                   | float('9.9'), float(9) |

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171702344.png" alt="image-20220115174752944" style="zoom:50%;" />

```python
name = '张三'
age = 20
print(name, type(name))
print(age, type(age))
#print('我叫'+name+',今年'+age+'岁')					# 此时会报错，数据类型不匹配
# TypeError: can only concatenate str (not "int") to str
print('我叫'+name+',今年'+str(age)+'岁')				# 正确的表达方式
```

```python
# str()将其他类型转换成string
a = 10
b = 198.8
c = False
print(type(a), type(b),type(c))
print(str(a), str(b), str(c), type(str(a)), type(str(b)),type(str(c)))
```

```python
# int()将其他类型转换成整型
s1 = '123'
f1 = 12.3
s2 = '12.34'
b = True
s3 = 'hello'
print(type(s1), type(f1), type(s2), type(b), type(s3))
print(int(s1), type(int(s1)))
print(int(f1), type(int(f1)))
#print(int(s2), type(int(s2)))
print(int(b), type(int(b)))              # 1
#print(int(s3), type(int(s3)))
```

```python
# float()将其他类型转换成浮点型
s1 = '123.98'
f1 = 12
b = True
s3 = 'hello'
print(type(s1), type(f1), type(s2), type(b), type(s3))
print(float(s1), type(float(s1)))
print(float(f1), type(float(f1)))
print(float(b), type(float(b)))
# print(float(s3), type(float(s3)))
```

bool()：将其他类型转换成boolean类型：

```python
# bool() - 1,0
a = 1
b = bool(a)
print(b)  # True
print(type(b))  # <class 'bool'>

c = 0
print(bool(c))  # False
d = 3
print(bool(d))  # True
```



### 5.6.空值对象_None

1.表示不存在的特殊对象；

2.作用：占位和解除与对象的关联。

```python
# 1.None
# 接触对象赋值的关联
a = "张无忌"
a = None
# 占位
sex = None
```

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171702345.png" alt="image-20220907214038289" style="zoom:50%;" />

![image-20220928095704112](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171702346.png)

### 5.7.复数

​	Python中是有复数存在的，复数由实部和虚部组成的数字，其中虚部是以j或J结尾。如1j，1+1j，1-1J。复数在人工只能的一些公式中存在使用。在开发中很少用到，此处不再赘述。



## 6.输入函数--input()

​	我们已经知道了Python的输出函数为print()，而input就是Python的输入函数，它用于接收来自用户输入的字符。input()输入函数接收的值需要将它存到到变量中才能进行下一步的使用。

**格式：**

```python
present = input("人生苦短，快用Python")
# present是变量名
# =表示赋值关系，将input()的结果赋值给present
# input()用来接收用户输入的字符串
```

```python
present = input("人生苦短，快用Python")
print(present)
```

​	此时我们可以在pycharm的控制台去输入字符，此处我输入OK按回车就会打印OK出来：

<img src="https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171702347.png" alt="image-20220116201106016" style="zoom:50%;" />

​	**练习：输入两个任意整数，计算两个整数的和：**

```python
a = input('请输入第一个值')
a = int(a)
b = input('请输入第二个值')
b = int(b)
print("两个数的和为："+str(a+b))
```



## 7.运算符

​	Python中，运算符包括：算术运算符、赋值运算符、比较运算符、布尔运算符、位运算符，其中算术运算符包含标准算术运算符、取余运算符和幂运算符。



### 7.1.算术运算符

​	

| 运算符名称     | 运算符号           |
| -------------- | ------------------ |
| 标准算术运算符 | +、-、*、/、//整除 |
| 取余运算符     | %                  |
| 幂运算符       | **                 |

```python
# 算术运算符
print(1+1)  # 加法运算
print(2-1)  # 剑法运算
print(10*10)  # 乘法运算
print(10/10)  # 除法运算
print(11//2)  # 整除运算
print(11 % 2)  # 取模运算
print(2**5)  # 幂运算
```

**需要注意的是，在整除运算中一正一负进行运算时得到的不会是我们想要的结果，因为在Python中，一正一负的运算是向下取整的；而取余运算中一正一负的运算需要遵循：余数=被除数-除数*商：**

```python
print(9//4)  # 2
print(-9//-4)  # 2
print(-9//4)  # -3
print(9//-4)  # -3
print(9%-4)  # -3  9-(-4)*(-3)=-3
print(-9%4)  # 3
```



### 7.2.赋值运算符

​	在Python中，赋值运算符用=表示：它的执行顺序是从右向左执行。

| 链式赋值     | a=b=c=10                |
| ------------ | ----------------------- |
| 运算方式     | 运算表示                |
| 参数赋值     | +=、-=、*=、/=、//=、%= |
| 系列解包赋值 | a,b,c=10,20,30          |

```python
# 赋值运算符
a = 3+4  # 运算从右向左
print(a)  # 7

# 链式赋值
x = y = z = 100
print(x, id(x))
print(y, id(y))
print(z, id(z))

# 参数赋值
u = 10
u += 40
print(u)
```



### 7.3.比较运算符

​	Python的比较运算符和其他语言类似，都是对变量或其他表达式的结果进行大小、真假的比较。

| 定义            | 比较符号         |
| --------------- | ---------------- |
| 一般比较符      | <、>、<=、>=、!= |
| 对象value的比较 | ==               |
| 对象id的比较    | is、is not       |

```python
# 比较运算符,比较的结果为布尔值
a, b = 10, 20
print(a > b)  
print(a < b)
print(a <= b)
print(a >= b)
print(a != b)
print(a == b)
```

​	一个变量由标识、类型和值组成，==比较的是值，比较标识用is/is not

```python
x = 10
y = 10
print(x == y)  # True --a与b的value相等
print(x is y)  # Ture --a与b的值也相等
```

```python
"""
    is is not 和 == !=的区别
    is ,is not比较的是对象内存的引用 ——>  id值 
    ==,!=比较的是对象的值
    如果比较的是不可变的类型（数字、字符串、元组），is和==是没有区别的
    如果比较的是可变类型（列表、字典、集合），就有区别
    is在一般时候比==的效率要高一些，在变量和None比较时，一般用is,is not
"""
a = 10
b = 10
print(a is b, a == b)  # True True

c = ["aa", "bb"]
d = ["aa", "bb"]
print(c is d, c == d)  # False True
```



### 7.4.布尔运算符

​	布尔运算符是对布尔值之间的运算，布尔运算符号有：and、or、not、in、not in。它们的运算关系如图所示：

| 运算符 | 运算数 | 运算数 | 运算结果 | 备注                                  |
| ------ | ------ | ------ | -------- | ------------------------------------- |
| and    | Ture   | Ture   | Ture     | 当两个 运算数都为True时，结果才为True |
|        | True   | False  | False    |                                       |
|        | False  | True   | False    |                                       |
|        | False  | False  | False    |                                       |
| or     | True   | True   | True     | 只要有一个运算符为True，结果就为True  |
|        | True   | False  | True     |                                       |
|        | False  | True   | Ture     |                                       |
|        | False  | False  | False    |                                       |
| not    | True   | True   | False    | 如果运算数为True，运算结果为False     |
|        | False  | False  | True     | 如果运算数为False，运算结果为True     |

```python
# and 
a, b = 1, 2
print(a == 1 and b == 2)  # True and True = True
print(a == 1 and b < 2)  # True and False = False
print(a != 1 and b == 2)  # False and True = False
print(a != 2 and b != 3)  # False and False = False
```

```python
# or
print(a == 1 or b == 2)  # True or True = True
print(a == 1 or b < 2)  # True or False = True
print(a != 1 or b == 2)  # False or True = True
print(a != 2 or b != 3)  # False or False = False
```

```python
# not
f1 = True
f2 = False
print(not f1)  # False
print(not f2)  # True
```

```python
# in和not in 表示在不在之中
s = 'hello world'
print('w' in s)  # True
print('b' in s)  # False
print('w' not in s)  # False
```



### 7.5.位运算符

​	位运算符是将数据转成二进制进行计算，位运算符如下：

| 位运算符号     | 释义                                |
| -------------- | ----------------------------------- |
| 位与&          | 对应数位都是1结果位数才是1，否则为0 |
| 位或\|         | 对应数位都是0结果位数才是0，否则为1 |
| 左移位运算符<< | 高位溢出舍弃，低位补0               |
| 右移位运算符>> | 低位溢出舍弃，高位补0               |

```python
# 位运算符
print(4 & 8)  # 0 按位与，同为1才是1
print(4 | 8)  # 12 按位或，同为0时才为0
print(4 << 1)  # 8 左移相当于*2
print(4 >> 1)  # 2 右移相当于/2
```



### 7.6.运算符的优先级

​	运算符的优先级如下图所示：

![image-20220118162547552](https://gitee.com/zou_tangrui/note-pic/raw/master/img/202302171702348.png)

x