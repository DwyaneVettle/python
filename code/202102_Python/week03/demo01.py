# 数据类型

"""
    python中的数据类型有：int,float,bool,str

"""
# int 整型
num01 = 1924245553542
print(type(num01))  # <class 'int'>
num02 = 0b01010011  # 二进制的表示用 0b
print(num02)  # 83
num03 = 0o7447775  # 八进制的表示用 0o
print(num03)  # 1986557
num04 = 0x194543859AF  # 十六进制的表示用 0x
print(num04)  # 1736579766703
print(type(num04))  # <class 'int'>

# 浮点型float
a = 3.14
print(type(a))  # <class 'float'>
# 浮点型数据是不精确的，一般不建议使用浮点型数据做数学运算
print(1.1 + 2.1)  # 3.2
print(1.1 + 2.2)  # 3.3000000000000003

# 在Python中，要用浮点型数据做数学运算，需要导入decimal
from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))  # 3.3

# 布尔型 True - 是  False - 否
# 布尔型还可以做数学运算，True-1,False-0
b01 = True
print(type(b01))  # <class 'bool'>
b02 = False
print(type(b02))  # <class 'bool'>
print(b01 + b02)  # 1
print(10 + True)  # 11

print("---------------")
# 字符串类型 String str
"""
    单引号''
    双引号""
    三双引号 """""" - 可以在里面声明多行字符串，只表示一个对象
"""
str01 = '龙小杰'
print(type(str01))  # <class 'str'>
str02 = "杨衎"
print(type(str02))  # <class 'str'>
str03 = """程东林
            谢俊杰
            桂嘉良
            张榕珊"""  # <class 'str'>
print(type(str03))
print(str03)
str04 = "'aa'"
print(str04)

# 字符串的相关操作
"""
    字符串的格式化（拼接）
    1.%拼接
    2.format()--{字符串}.format(args)
    3.f-strings--f'{arg}'
    4.单纯的两个字符串拼接直接使用+
"""
print(str02 + str04)

name = "肖锐"
age = 20.5
# print('我叫' + name + ',年龄' + age)
print('我叫%s,年龄%f岁' % (name, age))
print('我叫{},年龄{}岁'.format(name, age))
print(f'我叫{name},年龄{age}')
# replace()方法是字符串替换 str.replace(old, new, count = None)
str05 = "我叫肖锐，我的年龄是20岁"
str06 = str05.replace('我', '他')
print(str06)
# split(),分割字符串，默认返回一个列表list，加了参数后按”,“分割
str07 = "人生苦短快用Python"
str08 = str07.split('短')
print(str08)
str09 = 'a,b,c,d'
print(str09.split(','))

# strip()去除两端的空格
str10 = '  hello  '
print(str10.strip())
str11 = "####world####"
print(str11.strip('#'))

"""
    字符串切片
    任何一个字符都有自己的下标，正序第一个字符下标为0，依次递增，
    倒叙第一个字符下标为-1,依次递减
    []按索引查找
"""
str12 = 'python'
# 正序
print(str12[4])
# 倒叙
print(str12[-2])
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

