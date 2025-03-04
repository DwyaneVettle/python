"""
    python中的数据类型
    数据类型：对象有自己所具有的某种特性
        数据类型：对象有自己所能执行的操作
        整型：int 整数 0 1 -2 -4....
        浮点型：float 浮点数 0.0 1.0 -2.0 -4.0
        字符串：str 字符串 ""  ''  包裹的所有字符,数字、汉字等
        布尔类型：bool 只有两个值 True False
"""
from decimal import Decimal
# 整型
num01 = 100
num02 = 200
num03 = -1000
num04 = 0
print(num01, num02, num03)  # 100 200 -1000
print("========================================")
print(type(num01), type(num02), type(num03), type(num04))  # <class 'int'> <class 'int'>
# 二进制 0b开头
print(0b0101)
# 八进制 0o开头
print(0o01234)
# 十六进制 0x开头
print(0xFFF78)  # 1048440

print("========================================")

# 浮点型：小数
# 浮点型的精度问题：一般不用于做数学运算，因为它会丢失精度
# 如果要做数学运算，需要用decimal来包裹
# 1.导包 from decimal import Decimal		# 2.使用Decimal包裹浮点数
f01 = 100.123
f02 = -1.34
f03 = 0.0
print(type(f01))  # <class 'float'>
print(type(f02))
print(type(f03))
print(1.1 + 2.2)  # 3.3000000000000003
print(Decimal('1.1') + Decimal('2.2'))  # 3.3
print("========================================")

"""
    布尔类型：True是 False否
    boolean
    常用与判断、循环、条件语句
"""
print(type(True))  # <class 'bool'>
print(type(False))
print(1 == 1)  # True
print(1 == 2)  # False
print(1 != 1)

# 注意
print(bool(1))
print("========================================")
"""
    字符串：str '' "" 只能在一行  '''可以换行'''
       表示不可变的字符序列
"""
s01 = '人生苦短，快学Python'
s02 = "人生苦短，快学Python"
s03 = '''
    人生苦短，快学Python
'''
print(type(s01))  # <class 'str'>
print(type(s02))
print(type(s03))




