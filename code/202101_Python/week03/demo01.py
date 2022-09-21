"""
    数据类型：int,float,bool,str
"""
# int-整数、负数、0
# 二进制用0b、八进制用0o，十六进制0x
num01 = 0
num02 = 119
num03 = -11
print(num01)
print(num02)
print(num03)

num04 = 0b1101  # 2进制
print(num04)  # 13
num05 = 0o76543210
print(num05)  # 16434824
num06 = 0xAF9438593
print(num06)  # 47131624851
print(type(num06))  # <class 'int'>


"""
    浮点型数据不精确，一般不用来做数学运算
    如果要做数学运算
    将浮点型的数据用字符串形式表示，再用decimal来计算
    如果小数点后面的数比较长，是用科学计数法表示的
"""
f01 = 3.14
print(type(f01))  # <class 'float'>

print(1.1 + 2.1)  # 3.2
print(1.1 + 2.2)  # 3.3000000000000003
from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))  # 3.3
print(0.000000000000000000000000000000000000000000003)  # 3e-45

"""
    bool-True False
    在Python中，True可以用数字1表示，False可以使用数字0表示
    bool类型就可以做数学运算
    除了0之外的所有数字都是True
"""
b01 = True
print(type(b01))  # <class 'bool'>
b02 = False
print(type(b02))  # <class 'bool'>
print(b01 + 110)  # 111
print(b02 + 110)  # 110


"""
    字符串str
    1.单引号''
    2.双引号""
    3.三引号""""""-可以换行声明多个字符
"""
str01 = '黄东'
str02 = "黄镇涛"
str03 = """黄晓明
            黄圣依
            黄洋
"""
print(str01)  # 黄东
print(str02)  # 黄镇涛
print(str03)

"""
    字符串的相关操作
    1.格式化
        1.1.%格式化 %s字符串，%d十进制，%f浮点型
        1.2.format()-字符串{}.format(args)
        1.3.f-strings，在字符串前加f，通过{}传递参数
"""
name = "黄洋"
age = 20
print("我叫%s,年龄%d岁" % (name, age))
print("我是{},年龄{}岁".format(name, age))
print(f"我是{name},年龄{age}岁")

name = "刘德华"
age = 61
sex = "男"
salary = 1000.05
# 输出：我是刘德华，工资1000.05块，今年61，性别男-3分钟练习3种格式化
# 用%占位-需要匹配数据类型
print("我是%s，工资%f块，今年%d，性别%s" % (name, salary, age, sex))

# 字符串{}.format(args)
print("我是{}，工资{}块，今年{}，性别{}".format(name, salary, age, sex))

# f-strings - f"字符串{arg}"
print(f"我是{name}，工资{salary}块，今年{age}，性别{sex}")

"""
    拼接 
    + 在拼接比较少的元素的时候，效率更高
    join()-是在每一个元素中进行插入-拼接多个元素的时候效率较高
"""
p01 = "java"
p02 = "Python"
p03 = "PHP"
print(p01 + p02 + p03)
print(p01.join(p02))
list01 = ["java", "Python", "PHP"]
print('/'.join(list01))

"""
    分割-split()
    如果不传参数，默认以空格分隔，然后加上逗号
    传参的情况就是用逗号取代参数分隔，返回的是一个列表
"""
str04 = "hello world"
print(str04.split("l"))
myStr = 'hello world and Python and java and php'
list02 = myStr.split("and")
print(list02)

"""
    替换-replace(old, new ,count)
    count不传递，表示替换所有
"""
myStr = 'hello world and Python and java and php'
new_str = myStr.replace("and", "he", 10)
print(new_str)


"""
    去除字符串两端的空格-strip()
    如果传递参数，去除的就是参数
    默认去除空格
"""
str05 = " 刘德华 "
print(str05.strip())
str06 = "#####ldh#####"
print(str06.strip("#"))
