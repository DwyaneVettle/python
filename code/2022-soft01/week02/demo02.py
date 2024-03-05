"""
    python中基础的数据类型有：
        整型int、浮点型float、布尔类型bool、 字符串类型str
"""
# 整型int-正整数、负整数、零
a = 100
b = -100
c = 0  # <class 'int'>
print(type(a))
print("二进制：", 0b1)
print("八进制：", 0o34567)
print("十六进制：", 0xFFF)

# 浮点型-小数，丢失精度，一般不用于计算
f01 = 0.5
print(type(f01))  # <class 'float'>
print(1.1 + 2.2)  # 3.3000000000000003

from decimal import Decimal  # python导包
print(Decimal('1.1') + Decimal('2.2'))  # 3.3 Decimal()参数为字符串


# 布尔类型 True False 换算成整数True=1 False=0
b01 = True
b02 = False
print(type(b01))  # <class 'bool'>
print(b01, b02)
print(1 + True)

# 字符串类型-str
str01 = '人生苦短，快用Python'
str02 = "人生苦短，快用Python"
print(str01, str02)
# 如果字符串想要在多行展示，可以使用三引号
str03 = '''
        人生苦短，
        快用python
'''
print(str03)
str04 = """
        人生苦短，
        快用python
"""
print(type(str04))  # <class 'str'>

name = '龟叔'
age = 60
print("python的创始人" + name + "他的年龄是：" + str(age))
